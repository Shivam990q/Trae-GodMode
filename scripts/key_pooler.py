import os, sys, json, time, threading, urllib.request, urllib.error, http.server, socketserver

# Set UTF-8 encoding for Windows console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PORT = 8080
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keys.json")

DEFAULT_CONFIG = {
    "routes": {
        "xkiro": {
            "upstream": "https://api.xkiro.com/v1",
            "models": ["qwen/qwen3.8-max:free", "qwen3.8-max", "*"],
            "keys": [
                "sk-paste-your-first-xkiro-key-here",
                "sk-paste-your-second-xkiro-key-here"
            ]
        },
        "bynara": {
            "upstream": "https://router.bynara.id/v1",
            "models": ["minimax-m3-free", "qwen3.8-27b", "glm-5.3-flash-free", "nemotron-3-ultra", "*"],
            "keys": [
                "sk-paste-your-first-bynara-key-here",
                "sk-paste-your-second-bynara-key-here"
            ]
        },
        "kiraai": {
            "upstream": "https://kiraai.vn/v1",
            "models": ["mimo-v2.5", "hy3", "*"],
            "keys": [
                "sk-paste-your-first-kiraai-key-here",
                "sk-paste-your-second-kiraai-key-here"
            ]
        }
    }
}

class KeyPoolManager:
    def __init__(self, config_path):
        self.config_path = config_path
        self.routes = {}
        self.key_indices = {}
        self.cooldowns = {}
        self.lock = threading.Lock()
        self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_path):
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(DEFAULT_CONFIG, f, indent=2)
            print(f"[CONFIG] Initialized default key config at: {self.config_path}")

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.routes = data.get("routes", {})
            for r_name in self.routes:
                if r_name not in self.key_indices:
                    self.key_indices[r_name] = 0
            print(f"[CONFIG] Loaded {len(self.routes)} route provider pools.")
        except Exception as e:
            print(f"[ERROR] Failed to load {self.config_path}: {e}")

    def get_route_and_key(self, path, model_name=None, requested_key=None):
        now = time.time()
        with self.lock:
            # 1. Comma-separated keys passed directly from Trae UI
            if requested_key and "," in requested_key:
                raw_keys = [k.strip() for k in requested_key.split(",") if k.strip()]
                for k in raw_keys:
                    if self.cooldowns.get(k, 0) < now:
                        return None, k, raw_keys
                return None, raw_keys[0], raw_keys

            # 2. Match route by path prefix (e.g. /xkiro/v1/...)
            for r_name, r_cfg in self.routes.items():
                if path.startswith(f"/{r_name}"):
                    upstream = r_cfg.get("upstream", "")
                    keys = [k for k in r_cfg.get("keys", []) if not k.startswith("sk-paste-your")]
                    if not keys:
                        return upstream, requested_key or "", []
                    healthy_keys = [k for k in keys if self.cooldowns.get(k, 0) < now] or keys
                    idx = self.key_indices[r_name] % len(healthy_keys)
                    selected_key = healthy_keys[idx]
                    self.key_indices[r_name] = (idx + 1) % len(healthy_keys)
                    return upstream, selected_key, keys

            # 3. Match route by model name
            for r_name, r_cfg in self.routes.items():
                models = r_cfg.get("models", [])
                if model_name and any(m == model_name or m in model_name for m in models):
                    upstream = r_cfg.get("upstream", "")
                    keys = [k for k in r_cfg.get("keys", []) if not k.startswith("sk-paste-your")]
                    if not keys: return upstream, requested_key or "", []
                    healthy_keys = [k for k in keys if self.cooldowns.get(k, 0) < now] or keys
                    idx = self.key_indices[r_name] % len(healthy_keys)
                    selected_key = healthy_keys[idx]
                    self.key_indices[r_name] = (idx + 1) % len(healthy_keys)
                    return upstream, selected_key, keys

            # Default fallback
            if self.routes:
                first_r = list(self.routes.keys())[0]
                r_cfg = self.routes[first_r]
                upstream = r_cfg.get("upstream", "")
                keys = [k for k in r_cfg.get("keys", []) if not k.startswith("sk-paste-your")]
                if keys:
                    healthy_keys = [k for k in keys if self.cooldowns.get(k, 0) < now] or keys
                    selected_key = healthy_keys[0]
                    return upstream, selected_key, keys

            return None, requested_key or "", []

    def mark_cooldown(self, key, seconds=60):
        with self.lock:
            self.cooldowns[key] = time.time() + seconds
            masked = key[:8] + "..." + key[-4:] if len(key) > 12 else key
            print(f"[FAILOVER] Key {masked} hit rate-limit/error. Cooldown for {seconds}s.")

pool_manager = KeyPoolManager(CONFIG_FILE)

class MicroPoolerHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass # Clean custom logging

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.end_headers()

    def do_GET(self):
        self.handle_proxy_request("GET")

    def do_POST(self):
        self.handle_proxy_request("POST")

    def handle_proxy_request(self, method):
        content_len = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_len) if content_len > 0 else b""
        
        model_name = None
        if body:
            try:
                j = json.loads(body.decode("utf-8"))
                model_name = j.get("model")
            except Exception:
                pass

        req_auth = self.headers.get("Authorization", "")
        raw_key = req_auth.replace("Bearer ", "").strip() if req_auth else ""

        upstream, key, pool = pool_manager.get_route_and_key(self.path, model_name, raw_key)
        
        sub_path = self.path
        for r_name in pool_manager.routes:
            if sub_path.startswith(f"/{r_name}"):
                sub_path = sub_path[len(f"/{r_name}"):]
                if not sub_path.startswith("/"): sub_path = "/" + sub_path
                break

        if not upstream:
            first_cfg = list(pool_manager.routes.values())[0] if pool_manager.routes else {}
            upstream = first_cfg.get("upstream", "https://api.xkiro.com/v1")

        target_url = upstream.rstrip("/") + ("/" + sub_path.lstrip("/"))
        keys_to_try = [key] + [k for k in pool if k != key] if pool else [key]
        
        for attempt_idx, attempt_key in enumerate(keys_to_try):
            masked_key = attempt_key[:8] + "..." + attempt_key[-4:] if len(attempt_key) > 12 else attempt_key
            print(f"[REQUEST] {method} -> {target_url} | Model: {model_name or 'N/A'} | Key #{attempt_idx+1}: {masked_key}")
            
            headers = {}
            for k, v in self.headers.items():
                if k.lower() not in ["host", "authorization", "content-length"]:
                    headers[k] = v
            headers["Authorization"] = f"Bearer {attempt_key}"
            headers["Content-Type"] = self.headers.get("Content-Type", "application/json")

            req = urllib.request.Request(target_url, data=body if method == "POST" else None, headers=headers, method=method)
            
            try:
                with urllib.request.urlopen(req, timeout=120) as resp:
                    self.send_response(resp.status)
                    for hk, hv in resp.getheaders():
                        if hk.lower() not in ["content-length", "transfer-encoding", "content-encoding"]:
                            self.send_header(hk, hv)
                    self.send_header("Access-Control-Allow-Origin", "*")
                    self.end_headers()

                    # Raw byte streaming pass-through directly to Trae
                    while True:
                        chunk = resp.read(1024)
                        if not chunk: break
                        self.wfile.write(chunk)
                        self.wfile.flush()
                    return

            except urllib.error.HTTPError as e:
                if e.code in [429, 401, 402, 503] and len(keys_to_try) > attempt_idx + 1:
                    pool_manager.mark_cooldown(attempt_key, 60)
                    print(f"[RETRY] Error {e.code}. Retrying instantly with next key in pool...")
                    continue
                else:
                    self.send_response(e.code)
                    self.send_header("Content-Type", "application/json")
                    self.send_header("Access-Control-Allow-Origin", "*")
                    self.end_headers()
                    err_body = e.read()
                    self.wfile.write(err_body)
                    return
            except Exception as e:
                print(f"[CONN ERROR] {e}")
                if len(keys_to_try) > attempt_idx + 1:
                    pool_manager.mark_cooldown(attempt_key, 30)
                    continue
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
                return

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

def start_server():
    server = ThreadedHTTPServer(("127.0.0.1", PORT), MicroPoolerHandler)
    print("=" * 75)
    print(f"   TRAE MULTI-KEY POOLER & AUTO-FAILOVER GATEWAY ACTIVE")
    print(f"   Listening on: http://127.0.0.1:{PORT}/v1")
    print(f"   Config Path : {CONFIG_FILE}")
    print("=" * 75)
    server.serve_forever()

if __name__ == "__main__":
    start_server()
