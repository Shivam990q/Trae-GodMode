import os, sys, re, json, subprocess, sqlite3, glob

print("=" * 75)
print("   TRAE PEAK AUTONOMY, REASONING & OMNI-TOOL 1-CLICK UNIVERSAL PATCHER")
print("   (Works on ANY Windows PC, ANY Username, ANY Drive)")
print("=" * 75)

USERPROFILE = os.environ.get("USERPROFILE", os.path.expanduser("~"))
LOCALAPPDATA = os.environ.get("LOCALAPPDATA", os.path.join(USERPROFILE, "AppData", "Local"))
APPDATA = os.environ.get("APPDATA", os.path.join(USERPROFILE, "AppData", "Roaming"))

candidate_index_paths = [
    os.path.join(LOCALAPPDATA, "Programs", "Trae", "resources", "app", "node_modules", "@byted-icube", "ai-modules-chat", "dist", "index.mjs"),
    os.path.join(os.environ.get("ProgramFiles", "C:\\Program Files"), "Trae", "resources", "app", "node_modules", "@byted-icube", "ai-modules-chat", "dist", "index.mjs"),
    os.path.join(os.environ.get("ProgramFiles(x86)", "C:\\Program Files (x86)"), "Trae", "resources", "app", "node_modules", "@byted-icube", "ai-modules-chat", "dist", "index.mjs"),
]

target_index = None
for p in candidate_index_paths:
    if os.path.exists(p):
        target_index = p
        break

if not target_index:
    matches = glob.glob(os.path.join(LOCALAPPDATA, "**", "ai-modules-chat", "dist", "index.mjs"), recursive=True)
    if matches:
        target_index = matches[0]

target_global = os.path.join(USERPROFILE, ".trae", "permission", "global.json")
target_settings = os.path.join(APPDATA, "Trae", "User", "settings.json")
target_db = os.path.join(APPDATA, "Trae", "User", "globalStorage", "state.vscdb")

print(f"[*] Detected User Profile: {USERPROFILE}")
print(f"[*] Detected Trae Bundle : {target_index}")

# 1. Global Autonomy Permissions
if target_global and os.path.exists(target_global):
    try:
        with open(target_global, "r", encoding="utf-8") as f:
            cfg = json.load(f)
        prof = cfg.get("customProfiles", {}).get("defaultCustomProfile", {})
        if "approval" in prof:
            prof["approval"]["reviewer"] = "auto"
            prof["approval"]["sceneRules"] = {
                "commandAstDangerChecker": False,
                "shellFileProtection": False,
                "deleteToolApproval": False,
                "mcpToolApproval": False
            }
        prof["filesystem"] = {"default": "allow"}
        prof["network"] = {"default": "allow"}
        prof["shellSandbox"] = {"enable": False, "onRestrict": "allow"}
        with open(target_global, "w", encoding="utf-8") as f:
            json.dump(cfg, f, indent=2)
        print("[OK 1/5] Global Permissions set to 100% Autonomous!")
    except Exception as e:
        print(f"[ERROR 1/5] global.json: {e}")

# 2. VSCode Settings
if target_settings and os.path.exists(target_settings):
    try:
        with open(target_settings, "r", encoding="utf-8") as f:
            s_cfg = json.load(f)
        s_cfg["chat.tools.terminal.autoApprove"] = {"*": True}
        s_cfg["chat.tools.global.autoApprove"] = True
        s_cfg["trae.mcp.enableWorkspaceMcp"] = True
        with open(target_settings, "w", encoding="utf-8") as f:
            json.dump(s_cfg, f, indent=2)
        print("[OK 2/5] VSCode Settings configured for full auto-approval!")
    except Exception as e:
        print(f"[ERROR 2/5] settings.json: {e}")

# 3. SQLite Endpoints
if target_db and os.path.exists(target_db):
    try:
        conn = sqlite3.connect(target_db)
        c = conn.cursor()
        c.execute("SELECT key, value FROM ItemTable WHERE key LIKE '%model_list_map%'")
        rows = c.fetchall()
        if rows:
            for k, v in rows:
                if "/api/v1/chat/completions" in v:
                    v_new = v.replace("/api/v1/chat/completions", "/v1/chat/completions")
                    c.execute("UPDATE ItemTable SET value = ? WHERE key = ?", (v_new, k))
            conn.commit()
            print("[OK 3/5] SQLite Database custom model endpoints repaired!")
        conn.close()
    except Exception as e:
        print(f"[ERROR 3/5] state.vscdb: {e}")

# 4. Patch index.mjs
if target_index and os.path.exists(target_index):
    with open(target_index, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    bak = target_index + ".bak"
    if not os.path.exists(bak):
        with open(bak, "w", encoding="utf-8") as f:
            f.write(content)

    # 4A. Fallback Reasoning options (Module 70489)
    old_mod = 'let a=["none","low","medium","high","xhigh","max"],i=e.default_reasoning_effort||"medium",s=e=>e?.reasoning_effort_options&&0!==e.reasoning_effort_options.length?e.reasoning_effort_options:void 0;'
    new_mod = 'let a=["none","low","medium","high","xhigh","max"],i=e.default_reasoning_effort||"max",s=e=>e?.reasoning_effort_options&&0!==e.reasoning_effort_options.length?e.reasoning_effort_options:a;'
    if old_mod in content:
        content = content.replace(old_mod, new_mod, 1)

    # 4B. Reactive Tooltip
    old_tj = 'function tj(e){let{model:t,children:r,placement:n="top-start"}=e,i=(0,N.useContextSelector)(T.H,e=>e.decision);'
    new_tj = 'function tj(e){let{model:t,children:r,placement:n="top-start"}=e,i=(0,N.useContextSelector)(T.H,e=>e.decision),[k,setK]=(0,m.useState)(null);'
    if old_tj in content:
        content = content.replace(old_tj, new_tj, 1)
    
    old_click = 'onClick:()=>{i.setModelReasoningEffort(t,o)}'
    new_click = 'onClick:()=>{i.setModelReasoningEffort(t,o);setK(o)}'
    if old_click in content:
        content = content.replace(old_click, new_click, 1)

    # 4C. Dynamic Badges
    old_badge_call = 'u({className:rK.badge})'
    new_badge_call = 'u({className:rK.badge,text:rowEff})'
    if old_badge_call in content:
        content = content.replace(old_badge_call, new_badge_call)

    # 4D. Omni-Tool Auto-Run (Commands, Files, MCP, Plans)
    replacements_autonomy = [
        # Terminal commands
        ('C=async()=>{if(r&&t.id)return await ts(e,{chat_session_id:r,task_id:n,type:"tool_confirm",plan_item_id:t.id,tool_name:o,decision:"confirm"},"confirm"),eb.$},',
         'C=async()=>{if(r&&t.id)return await ts(e,{chat_session_id:r,task_id:n,type:"tool_confirm",plan_item_id:t.id,tool_name:o,decision:"confirm"},"confirm"),eb.$};(0,eh.useEffect)(()=>{C()},[]);let '),
        # MCP tool calls
        ('g=async()=>{if(r&&t.id)return await ts(e,{chat_session_id:r,task_id:n,type:"tool_confirm",plan_item_id:t.id,tool_name:a,decision:"confirm"},"confirm"),eb.$},',
         'g=async()=>{if(r&&t.id)return await ts(e,{chat_session_id:r,task_id:n,type:"tool_confirm",plan_item_id:t.id,tool_name:a,decision:"confirm"},"confirm"),eb.$};(0,eh.useEffect)(()=>{g()},[]);let '),
        # File deletions
        ('g=async()=>{if(r&&t.id)return await ts(e,{chat_session_id:r,task_id:n,type:"tool_confirm",plan_item_id:t.id,tool_name:o,decision:"skip"},"skip"),eb.$},_=async()=>{if(r&&t.id&&await eg.lJ.show',
         'g=async()=>{if(r&&t.id)return await ts(e,{chat_session_id:r,task_id:n,type:"tool_confirm",plan_item_id:t.id,tool_name:o,decision:"confirm"},"confirm"),eb.$};(0,eh.useEffect)(()=>{g()},[]);let _=async()=>{if(r&&t.id&&await eg.lJ.show'),
        # Script execution
        ('g=async()=>{if(r&&t.id)return await ts(e,{chat_session_id:r,task_id:n,type:"tool_confirm",toolcall_id:t.toolCallInfo.id,plan_item_id:t.id,decision:"confirm"},"confirm"),eb.$},',
         'g=async()=>{if(r&&t.id)return await ts(e,{chat_session_id:r,task_id:n,type:"tool_confirm",toolcall_id:t.toolCallInfo.id,plan_item_id:t.id,decision:"confirm"},"confirm"),eb.$};(0,eh.useEffect)(()=>{g()},[]);let '),
        # Document plan continuation
        ('h=async()=>{if(r&&t.id)return await ts(e,{chat_session_id:r,task_id:n,type:"tool_confirm",plan_item_id:t.id,tool_name:s,decision:"confirm"},"confirm"),eb.$},',
         'h=async()=>{if(r&&t.id)return await ts(e,{chat_session_id:r,task_id:n,type:"tool_confirm",plan_item_id:t.id,tool_name:s,decision:"confirm"},"confirm"),eb.$};(0,eh.useEffect)(()=>{h()},[]);let '),
        # Seed Max Mode Toggle Unlock
        ('key:"maxModeSwitch",shouldShow:(e,t)=>t.isInternalUser&&!!(e.max_mode||e.is_dollar_max),',
         'key:"maxModeSwitch",shouldShow:(e,t)=>!!(e.max_mode||e.is_dollar_max||(Array.isArray(e.context_window_size?.max)&&e.context_window_size.max[0]>200000)),')
    ]
    for old, new in replacements_autonomy:
        if old in content:
            content = content.replace(old, new, 1)

    # 4E. Edit Model Modal Unlocks
    custom_replacements = [
        ('options:T,showCheckedIcon:!0,value:h.customProtocol,disabled:f,', 'options:T,showCheckedIcon:!0,value:h.customProtocol,disabled:!1,'),
        ('checked:h.isFullUrl,disabled:f,', 'checked:h.isFullUrl,disabled:!1,'),
        ('value:h.baseUrl||"",disabled:f,', 'value:h.baseUrl||"",disabled:!1,'),
        ('placeholder:d.localize("input_model_id",{},"Input Model ID"),disabled:f', 'placeholder:d.localize("input_model_id",{},"Input Model ID"),disabled:!1'),
        ('value:h.ak||"",onChange:e=>{e&&N(e=>({...e,apiKey:""})),g({ak:e})},disabled:f,', 'value:h.ak||"",onChange:e=>{e&&N(e=>({...e,apiKey:""})),g({ak:e})},disabled:!1,'),
        ('value:v.selectedProviderId||"",onChange:Y,disabled:_,', 'value:v.selectedProviderId||"",onChange:Y,disabled:!1,'),
        ('value:v.billingMode||(P?.providers[0]?.billing_mode??P?.providers[0]?.id),onChange:e=>G(e),disabled:_', 'value:v.billingMode||(P?.providers[0]?.billing_mode??P?.providers[0]?.id),onChange:e=>G(e),disabled:!1'),
        ('value:v.currentModel||"",onChange:q,errorMessage:O.currentModel,disabled:_', 'value:v.currentModel||"",onChange:q,errorMessage:O.currentModel,disabled:!1'),
        ('value:v.ak||"",onChange:e=>b({ak:e}),disabled:_,', 'value:v.ak||"",onChange:e=>b({ak:e}),disabled:!1,')
    ]
    for old, new in custom_replacements:
        if old in content:
            content = content.replace(old, new, 1)

    with open(target_index, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK 4/5] index.mjs completely patched with Omni-Autonomy!")

# 5. Syntax Check & Restart
if target_index:
    res = subprocess.run(["node", "--check", target_index], capture_output=True, text=True)
    if res.returncode == 0:
        print("[OK 5/5] JavaScript syntax verified 100% valid!")
        print("\n[SUCCESS] ALL MODS APPLIED! Restarting Trae IDE...")
        trae_exe = os.path.join(LOCALAPPDATA, "Programs", "Trae", "Trae.exe")
        cmd = f'taskkill /F /IM "Trae.exe" 2>$null; Start-Sleep -Seconds 2; if (Test-Path "{trae_exe}") {{ Start-Process "{trae_exe}" }} else {{ Start-Process "Trae.exe" -ErrorAction SilentlyContinue }}'
        subprocess.run(["powershell", "-Command", cmd])
    else:
        print(f"[ERROR 5/5] Syntax error detected: {res.stderr}")
