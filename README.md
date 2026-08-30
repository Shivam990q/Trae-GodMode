<div align="center">

<img src="assets/banner.png" alt="Trae GodMode Official Banner" width="100%" style="border-radius: 10px;" />

<br/><br/>

<h3 align="center">The open-source modification suite & sub-millisecond failover gateway for "ByteDance" Trae AI IDE.</h3>

<p align="center">
  <b>1,000,000 Token Memory &nbsp;•&nbsp; Zero Confirmation Popups &nbsp;•&nbsp; Uncapped Reasoning CoT &nbsp;•&nbsp; Infinite Key Pool</b>
</p>

<p align="center">
  <a href="docs/ARCHITECTURE.md"><img src="https://img.shields.io/badge/📘_USER_GUIDE-v1.0.0_·_ENGLISH-0078D4?style=for-the-badge&labelColor=1e293b" alt="English Guide" /></a>&nbsp;
  <a href="docs/ZH_CN_GUIDE.md"><img src="https://img.shields.io/badge/📙_体验指南-v1.0.0_·_中文-f97316?style=for-the-badge&labelColor=1e293b" alt="Chinese Guide" /></a>&nbsp;
  <a href="docs/MULTI_ACCOUNT_GUIDE.md"><img src="https://img.shields.io/badge/⚡_KEY_POOL-50+_ACCOUNTS-8b5cf6?style=for-the-badge&labelColor=1e293b" alt="Key Pooling" /></a>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-22c55e?style=flat-square&labelColor=0f172a" alt="License" /></a>&nbsp;
  <a href="https://platform.openai.com/docs/api-reference"><img src="https://img.shields.io/badge/Protocol-OpenAI_v1_SSE-6366f1?style=flat-square&labelColor=0f172a" alt="OpenAI Compatible" /></a>&nbsp;
  <a href="docs/ARCHITECTURE.md"><img src="https://img.shields.io/badge/Context-1M_Tokens-f43f5e?style=flat-square&labelColor=0f172a" alt="Context" /></a>&nbsp;
  <a href="docs/BENCHMARKS.md"><img src="https://img.shields.io/badge/Failover-%3C0.5ms-00F08B?style=flat-square&labelColor=0f172a" alt="Latency" /></a>&nbsp;
  <a href="https://www.trae.ai"><img src="https://img.shields.io/badge/Trae_IDE-v1.x_✓-06b6d4?style=flat-square&labelColor=0f172a" alt="Trae Ready" /></a>&nbsp;
  <a href="https://github.com/Shivam990q/Trae-GodMode"><img src="https://img.shields.io/badge/Windows-10_%2F_11-0078D4?style=flat-square&labelColor=0f172a" alt="Platform" /></a>
</p>

<p align="center">
  <a href="https://github.com/Shivam990q/Trae-GodMode/discussions"><img src="https://img.shields.io/badge/💬_COMMUNITY-DISCUSSIONS-5865F2?style=flat-square&labelColor=0f172a" alt="Community" /></a>&nbsp;
  <a href="https://github.com/Shivam990q/Trae-GodMode/issues"><img src="https://img.shields.io/badge/🐞_ISSUES-BUG_REPORTS-e11d48?style=flat-square&labelColor=0f172a" alt="Issues" /></a>&nbsp;
  <a href="https://github.com/Shivam990q/Trae-GodMode/releases"><img src="https://img.shields.io/badge/🚀_RELEASE-v1.0.0-10b981?style=flat-square&labelColor=0f172a" alt="Release" /></a>&nbsp;
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white&labelColor=0f172a" alt="Python" />&nbsp;
  <img src="https://img.shields.io/badge/AST-Engine-f59e0b?style=flat-square&labelColor=0f172a" alt="AST" />
</p>

<p align="center">
  <a href="#-the-5-godmode-superpowers"><b>⚡ Features</b></a> &nbsp;&nbsp;•&nbsp;&nbsp;
  <a href="#-instant-quickstart-3-steps"><b>🚀 Quickstart</b></a> &nbsp;&nbsp;•&nbsp;&nbsp;
  <a href="#-live-gateway-simulation-in-action"><b>🔄 Gateway</b></a> &nbsp;&nbsp;•&nbsp;&nbsp;
  <a href="#-deep-competitor-comparison"><b>📊 Comparisons</b></a> &nbsp;&nbsp;•&nbsp;&nbsp;
  <a href="#-in-depth-documentation"><b>📖 Docs</b></a>
</p>

---

</div>

<br/>

## ⚡ The 5 GodMode Superpowers

> **Think of Trae IDE as a supercar with an electronic speed limiter.** Out of the box it's fast — but the top gear is locked, context memory is throttled, and it stops to ask for your permission before taking every turn. **Trae-GodMode removes every limiter and gives you total, uninterrupted flow.**

<br/>

<div align="center">

| Superpower | Default Trae | ⚡ With GodMode Active | Technical Reference |
| :--- | :---: | :---: | :--- |
| 🧠 **All-Tier Reasoning** | Hidden / Locked | **6 Levels (`none` → `max`)** | [Chain-of-Thought Dispatcher](docs/ARCHITECTURE.md#subsystem-1-in-memory-patcher) |
| ⚡ **Omni-Autonomy** | Prompts Confirmation | **100% Zero-Prompt Auto** | [Tool Permission Bypass Hooks](docs/ARCHITECTURE.md#subsystem-1-in-memory-patcher) |
| 💾 **Hyper-Context** | 200k Capped | **1,048,576 Tokens (1M)** | [1M Max Mode Allocator](docs/ARCHITECTURE.md#memory-expansion) |
| 🔄 **Infinite Key Pool** | 1 Key (Hits Limits) | **Sub-ms Auto-Failover** | [Zero-Latency Proxy Engine](docs/MULTI_ACCOUNT_GUIDE.md) |
| 🔓 **Model Studio** | Disabled / Greyed | **100% Fully Editable** | [UI Customizer Unlocker](docs/ARCHITECTURE.md#ui-patches) |

</div>

---

## 🏗️ Architecture Blueprint

```text
                  ╭─────────────────────────────────────────────────────────╮
                  │              ⚡ TRAE IDE (GOD-MODE ACTIVE)              │
                  │  • 1,000,000 Token Hyper-Memory                         │
                  │  • Max Chain-of-Thought (CoT) Thinking                  │
                  │  • 100% Zero-Prompt Autonomous Execution                │
                  ╰────────────────────────────┬────────────────────────────╯
                                               │
                                               │  ⚡ OpenAI-Compatible Streaming SSE
                                               │  POST /v1/chat/completions
                                               ▼
                  ╭─────────────────────────────────────────────────────────╮
                  │      ⚡ TRAE-GODMODE MULTI-GATEWAY (:8080)              │
                  │  • Sub-millisecond Raw Byte Pass-Through                │
                  │  • Automatic 60s Rate-Limit Cooldown Engine             │
                  │  • Round-Robin Multi-Account Pool Router                │
                  ╰────────────────────────────┬────────────────────────────╯
                                               │
               ┌───────────────────────────────┼───────────────────────────────┐
               │                               │                               │
               ▼                               ▼                               ▼
╭─────────────────────────────╮ ╭─────────────────────────────╮ ╭─────────────────────────────╮
│    🌐 xKiro AI Router       │ │    🌐 Bynara AI Router      │ │   🌐 DeepSeek / OpenRouter  │
├─────────────────────────────┤ ├─────────────────────────────┤ ├─────────────────────────────┤
│ 🔑 Account 1 (Active)       │ │ 🔑 Account 1 (Active)       │ │ 🔑 Account 1 (Active)       │
│ 🔑 Account 2 (Standby)      │ │ 🔑 Account 2 (Standby)      │ │ 🔑 Account 2 (Standby)      │
│ 🔑 Account 3 (Standby)...   │ │ 🔑 Account 3 (Standby)...   │ │ 🔑 Account 3 (Standby)...   │
╰──────────────┬──────────────╯ ╰──────────────┬──────────────╯ ╰──────────────┬──────────────╯
               │                               │                               │
       ┌───────┴───────┐                       │                               │
       │               │                       │                               │
[200 OK Stream] [429 Limit Hit]                ▼                               ▼
       │               │                 [Auto-Rotates]                  [Auto-Rotates]
       ▼               ▼
 Code to Trae   ⚡ 1ms Failover to Key #2
             (Stream Never Breaks!)
```

> 🔌 **100% [OpenAI API Protocol](https://platform.openai.com/docs/api-reference/chat) Compatible** — Trae-GodMode Gateway natively supports standard `POST /v1/chat/completions` with bearer token authentication. Complies with [W3C Server-Sent Events (SSE)](https://html.spec.whatwg.org/multipage/server-sent-events.html) standards for zero-latency streaming. Works with Trae, Cursor, VSCode, LangChain, or custom Python/TypeScript tooling.

---

## 🎬 Live Gateway Simulation in Action

```bash
# ⚡ TRAE-GODMODE MULTI-KEY GATEWAY RUNNING ON http://127.0.0.1:8080/v1
[12:00:01] 📥 [REQUEST]    POST /v1/chat/completions | Model: qwen3.8-max | 🔑 Key #1: sk-xkiro-acc1...
[12:00:02] ⚠️ [RATE-LIMIT] HTTP 429 (Too Many Requests) received from upstream router.
[12:00:02] 🔄 [FAILOVER]   Key #1 on 60s cooldown ➔ ⚡ Switching to Key #2 in 0.38ms!
[12:00:02] 📥 [REQUEST]    POST /v1/chat/completions | Model: qwen3.8-max | 🔑 Key #2: sk-xkiro-acc2...
[12:00:03] 🚀 [STREAMING]  200 OK ➔ Raw SSE stream delivering code to Trae with ZERO interruptions!
```

---

## 📊 Deep Competitor Comparison

### 🏆 1. IDE Power & Autonomy (Trae-GodMode vs Cursor & Windsurf)

| Feature & Metric | Standard [Trae](https://www.trae.ai) | [Cursor Pro](https://www.cursor.com) ($20/mo) | [Windsurf](https://codeium.com/windsurf) ($20/mo) | ⚡ Trae-GodMode ($0) |
| :--- | :---: | :---: | :---: | :---: |
| **Monthly Subscription** | Free Tier Limits | $20 / month | $20 / month | 🟢 **$0 (100% Free & Unlimited)** |
| **Max Working Context** | 200,000 Tokens | 128k – 200k | 128k – 200k | 🟢 **1,048,576 Tokens (1M)** |
| **Reasoning Control** | Hidden (`null`) | Static Toggle | Static Toggle | 🟢 **6 Levels (`none` → `max`)** |
| **Terminal Autonomy** | Requires Confirmation | Partial Permission | Partial Permission | 🟢 **100% Zero-Prompt Auto-Run** |
| **MCP Tool Execution** | Confirmation Modal | Prompts User | Prompts User | 🟢 **100% Auto-Approved** |
| **Model Customizer** | Disabled Fields | Fixed | Fixed | 🟢 **100% Unlocked Studio** |

<br/>

### ⚡ 2. Proxy Engine & Gateway Architecture (vs One-API, LiteLLM & OmniRouter)

| Gateway Metric | [One-API](https://github.com/songquanpeng/one-api) (20k+ ⭐) | [LiteLLM](https://github.com/BerriAI/litellm) (16k+ ⭐) | [OmniRouter](https://github.com/Bedrock-AI/OmniRouter) | ⚡ **[Trae-GodMode Gateway](docs/BENCHMARKS.md)** |
| :--- | :---: | :---: | :---: | :---: |
| **Failover Switching Latency** | ~8 – 15 ms | ~15 – 30 ms | ~5 – 10 ms | 🟢 **< 0.5 ms (Sub-millisecond)** |
| **Memory Footprint (RAM)** | ~280 MB | ~200 MB | ~120 MB | 🟢 **< 12 MB (Ultra-Lightweight)** |
| **SSE Streaming Handling** | Buffered / Chunked | Re-encoded | Buffered | 🟢 **Raw Byte Pass-Through** |
| **Tool-Calling Headers** | Partial | Can Drop Headers | Partial | 🟢 **100% Native Byte Integrity** |
| **Setup & Dependencies** | Docker + MySQL + Redis | 50+ Python Packages | Node + SQLite | 🟢 **Zero Dependencies (Python StdLib)** |
| **Launch Speed** | 30–60 minutes | 15–30 minutes | 10–15 minutes | 🟢 **Instant (< 2 seconds via .BAT)** |

<br/>

### 💡 3. Honest Architectural Fit: Which Should You Choose?

| Your Real-World Scenario | Best Solution | Why |
| :--- | :--- | :--- |
| **Enterprise with 100+ Team Members** | [One-API](https://github.com/songquanpeng/one-api) / [LiteLLM](https://github.com/BerriAI/litellm) | Provides multi-tenant RBAC, billing dashboards, and team token quotas. |
| **Solo Developer or Pair-Programmer** | ⚡ **Trae-GodMode** | Pure zero-latency speed, no Docker/DB setup, runs locally with 12MB RAM. |
| **Total IDE Superpowers (1M Context + Autonomy)** | ⚡ **Trae-GodMode** | **The only open-source tool** that patches the IDE runtime itself. |

---

## 🌐 Multi-Provider & Router Support Matrix

Trae-GodMode supports any endpoint compatible with the **[OpenAI `/v1/chat/completions` API specification](https://platform.openai.com/docs/api-reference/chat)**:

| Category | Provider / Router | Base URL | Top Supported Models | References |
| :--- | :--- | :--- | :--- | :--- |
| **⚡ Free Routers** | **xKiro AI** | `https://api.xkiro.com/v1` | `qwen/qwen3.8-max:free`, `deepseek-v3`, `deepseek-r1` | [Qwen LM Specs](https://qwenlm.github.io) |
| | **Bynara** | `https://router.bynara.id/v1` | `minimax-m3-free`, `qwen3.8-27b`, `glm-5.3-flash` | [GLM Architecture](https://github.com/THUDM/GLM) |
| | **KiraAI** | `https://kiraai.vn/v1` | `mimo-v2.5`, `tencent-hy3-free`, `kimi-k2.5` | [Moonshot Kimi Docs](https://platform.moonshot.cn) |
| **💎 Premium APIs** | **OpenRouter** | `https://openrouter.ai/api/v1` | `anthropic/claude-4`, `google/gemini-3.1-pro` | [OpenRouter API Docs](https://openrouter.ai/docs) |
| | **DeepSeek Official** | `https://api.deepseek.com/v1` | `deepseek-chat`, `deepseek-reasoner` | [DeepSeek Technical Specs](https://www.deepseek.com) |
| | **Groq Cloud** | `https://api.groq.com/openai/v1` | `llama-3.3-70b-versatile`, `mixtral-8x22b` | [Groq LPU Acceleration](https://groq.com) |
| | **OpenAI** | `https://api.openai.com/v1` | `gpt-4o`, `gpt-4.1`, `o3-mini` | [OpenAI Reference](https://platform.openai.com) |
| **💻 Local LLMs** | **Ollama / vLLM / LMStudio** | `http://127.0.0.1:11434/v1` | `qwen2.5-coder:32b`, `deepseek-coder:33b` | [Ollama Docs](https://ollama.com) • [vLLM Project](https://github.com/vllm-project/vllm) |

---

## 🚀 Instant Quickstart (3 Steps)

### Step 1: Clone the Repository
```bash
git clone https://github.com/Shivam990q/Trae-GodMode.git
cd Trae-GodMode
```

### Step 2: 1-Click Patch Trae
Double-click **`1_CLICK_APPLY_PATCHES.bat`**
> 🛡️ *Auto-detects your Trae installation across any Windows drive (`C:`, `D:`, `E:`), backs up your original files, applies patches, and restarts Trae instantly.*

### Step 3: Configure Your Key Pool
Create your local `keys.json` (or copy from [`config/keys.example.json`](config/keys.example.json)):
```json
{
  "routes": {
    "xkiro": {
      "upstream": "https://api.xkiro.com/v1",
      "models": ["qwen/qwen3.8-max:free", "*"],
      "keys": [
        "sk-xkiro-account1-key...",
        "sk-xkiro-account2-key...",
        "sk-xkiro-account3-key..."
      ]
    }
  }
}
```
Double-click **`START_KEY_POOLER.bat`**, set Trae's Custom URL to `http://127.0.0.1:8080/xkiro/v1`, and start coding unlimitedly!

---

## 📁 Repository Structure

```
Trae-GodMode/
├── 📂 .github/                    # CI/CD Workflows & Interactive Issue Forms
│   ├── workflows/ci.yml           # Automated cross-device testing on every push
│   └── ISSUE_TEMPLATE/            # Bug report & feature request templates
│
├── 📂 core/                       # Core Modular Python Engine
│   ├── patcher.py                 # AST & regex bundle modification engine
│   ├── gateway.py                 # Zero-latency multi-key proxy & failover engine
│   └── models.py                  # Capability matrix for uncapped models
│
├── 📂 config/                     # Safe Configuration Templates
│   ├── keys.example.json          # Multi-account pool routing template
│   └── permissions.template.json  # 100% autonomous global permission profile
│
├── 📂 docs/                       # In-Depth Technical Guides
│   ├── ARCHITECTURE.md            # Deep-dive system specifications & AST hooks
│   ├── MULTI_ACCOUNT_GUIDE.md     # How to pool 50+ free keys for infinite coding
│   ├── BENCHMARKS.md              # Latency & throughput profiling data
│   ├── TROUBLESHOOTING.md         # Common questions, FAQs & fixes
│   ├── README_DESIGN_GUIDE.md     # Masterclass formula for top 0.01% GitHub READMEs
│   └── ZH_CN_GUIDE.md             # Chinese language guide (中文体验指南)
│
├── 📂 scripts/                    # Standalone CLI Scripts
│   ├── apply_all_patches.py       # Universal dynamic patcher script
│   ├── key_pooler.py              # Standalone gateway runner
│   └── verify_installation.py     # Cross-device self-test verification suite
│
├── ⚡ 1_CLICK_APPLY_PATCHES.bat   # 1-Click Patcher Launcher (Root entry point)
├── 🚀 START_KEY_POOLER.bat        # 1-Click Gateway Launcher (Root entry point)
├── 📜 CHANGELOG.md                # Detailed release notes
├── 🤝 CONTRIBUTING.md             # Contribution guidelines
├── 🔒 SECURITY.md                 # Local-only privacy & key protection policy
├── ⚖️ LICENSE                     # Official MIT License
└── 📖 README.md                   # You are here
```

---

## 📚 In-Depth Documentation

<details>
<summary><b>📖 Click to explore full documentation library</b></summary>

<br/>

* 🏛️ [**System Architecture & Subsystems**](docs/ARCHITECTURE.md) — Learn how AST patches intercept bundle hooks in memory.
* 🔑 [**Multi-Account Key Pooling Guide**](docs/MULTI_ACCOUNT_GUIDE.md) — Step-by-step setup to bypass rate-limits across all free routers.
* 📊 [**Latency & Throughput Benchmarks**](docs/BENCHMARKS.md) — In-depth profiling comparing GodMode with LiteLLM and One-API.
* 🛠️ [**Troubleshooting & FAQ**](docs/TROUBLESHOOTING.md) — Answers to updates, rollbacks, and connection setup.
* 🎨 [**Master README Design Playbook**](docs/README_DESIGN_GUIDE.md) — The exact formula and templates to build god-tier READMEs.
* 🇨🇳 [**中文使用指南 (Chinese Guide)**](docs/ZH_CN_GUIDE.md) — 简体中文快速上手与多账号配置教程。

</details>

---

## 🤝 Contributing

Contributions, feature suggestions, and pull requests are welcomed!  
See [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

```bash
# Fork & clone
git checkout -b feature/AmazingSuperpower
python scripts/verify_installation.py
git commit -m "feat: add AmazingSuperpower"
git push origin feature/AmazingSuperpower
```

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

<br/>

<div align="center">

**Built with ❤️ for the global AI coding community.**<br/>
*If Trae-GodMode leveled up your development workflow, please give it a* ⭐ *on GitHub!*

</div>
