<div align="center">

```
 _____                 _____           _ __  __           _      
|_   _| __ __ _   ___ / ____|         | |  \/  |         | |     
  | || '__/ _` | / _ \ |  __  ___   __| | \  / | ___   __| | ___ 
  | || | | (_| ||  __/ | |_ |/ _ \ / _` | |\/| |/ _ \ / _` |/ _ \
  |_||_|  \__,_| \___|\_____|\___/ \__,_|_|  |_|\___/ \__,_|\___/
```

# ⚡ Trae-GodMode (Trae Unchained)
### *The Ultimate 1-Click Peak Autonomy Unlocker, 1M Context Expander & Multi-Key Failover Gateway for Trae AI IDE*

[![GitHub License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Trae Version](https://img.shields.io/badge/Trae-v1.x%20Compatible-00D26A?style=for-the-badge&logo=visualstudiocode)](https://www.trae.ai)
[![Context Window](https://img.shields.io/badge/Context%20Window-1%2C000%2C000%20Tokens-FF6B6B?style=for-the-badge)](docs/ARCHITECTURE.md)
[![Autonomy](https://img.shields.io/badge/Autonomy-100%25%20Zero--Friction-7952B3?style=for-the-badge)](docs/ARCHITECTURE.md)
[![Key Pooling](https://img.shields.io/badge/Multi--Key%20Pool-Infinite%20Failover-4D96FF?style=for-the-badge)](docs/MULTI_ACCOUNT_GUIDE.md)
[![Latency Overhead](https://img.shields.io/badge/Latency-%3C0.5ms%20Pass--Through-success?style=for-the-badge)](docs/BENCHMARKS.md)

<p align="center">
  <b>Transform Trae IDE into an uncapped, fully autonomous, infinite-quota AI powerstation. No throttles. No confirmation popups. Unlimited API key pooling. 1 Million tokens memory.</b>
</p>

---

</div>

## 🌌 Overview

**Trae-GodMode** is an open-source, zero-dependency modification suite and native high-speed gateway designed specifically for **ByteDance Trae IDE & Trae Solo**. 

It unlocks hidden developer tiers, automates all tool execution prompts, expands context windows to **1,000,000 tokens**, and pools multiple free/paid API keys with sub-millisecond failover.

---

## 🔥 Superpowers Unlocked:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 1. ALL-TIER THINKING REASONING UNLOCKED                                  │
│    • Unlocks all 6 reasoning depth levels: none, low, medium, high, xhigh,  │
│      and max CoT (Chain-of-Thought) across all models.                      │
│    • Dynamic reactive badges reflecting actual active thinking levels.      │
├─────────────────────────────────────────────────────────────────────────────┤
│ ⚡ 2. 100% ZERO-FRICTION OMNI-AUTONOMY                                      │
│    • No more "Is it allowed to run this command?" confirmation dialogs.     │
│    • Auto-approves terminal commands, file deletions, multi-step doc plans,  │
│      and MCP tools (SQLite, Browser, GitHub) with 0 friction.               │
├─────────────────────────────────────────────────────────────────────────────┤
│ 💾 3. 1 MILLION TOKEN (1M) HYPER-CONTEXT EXPANDER                           │
│    • Unlocks the 1,000,000 token Max Mode Toggle for Seed-2.1-Turbo,        │
│      Gemini 3.1 Pro, Gemini 3 Flash, and custom router models.              │
├─────────────────────────────────────────────────────────────────────────────┤
│ 🔄 4. INFINITE MULTI-KEY POOLER & 429 AUTO-FAILOVER GATEWAY                 │
│    • Combines 5 to 50+ accounts into ONE single super-account.              │
│    • Instant 1ms failover on 429 Rate-Limits, 401/402 Quota Exhaustion.     │
│    • Round-Robin load balancing distributes load equally across keys.       │
├─────────────────────────────────────────────────────────────────────────────┤
│ 🔓 5. UNRESTRICTED MODEL STUDIO MODAL                                       │
│    • Removes all disabled form locks in the "Edit Model" dialog.            │
│    • Custom Request URLs, Model IDs, Full URL switches & API Keys are       │
│      100% editable on the fly.                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🏗️ Architecture & Documentation

For detailed architectural specifications and guides:
* 📐 [**System Architecture & Flowcharts**](docs/ARCHITECTURE.md)
* 🔑 [**Multi-Account Key Pooling Guide (50+ Accounts)**](docs/MULTI_ACCOUNT_GUIDE.md)
* 📊 [**Latency & Throughput Benchmarks**](docs/BENCHMARKS.md)
* 🛠️ [**Troubleshooting & FAQ**](docs/TROUBLESHOOTING.md)

```
                              ┌───────────────────────────────────┐
                              │       TRAE IDE (AUTONOMOUS)       │
                              │ • 1M Context Memory               │
                              │ • Max Thinking Effort CoT         │
                              │ • 0-Prompt Auto Tool Execution    │
                              └─────────────────┬─────────────────┘
                                                │ Streaming SSE
                                                ▼
                              ┌───────────────────────────────────┐
                              │   ⚡ TRAE-GODMODE GATEWAY         │
                              │   (http://127.0.0.1:8080/v1)      │
                              ├───────────────────────────────────┤
                              │ 🔑 Key Pool:                      │
                              │   • Account 1 (Active)            │
                              │   • Account 2 (Standby)           │
                              │   • Account 3 (Standby)...        │
                              └─────────────────┬─────────────────┘
                                                │
                      ┌─────────────────────────┴─────────────────────────┐
                      │                                                   │
               [Normal Query]                                    [Rate Limit / 429 Hit]
                      ▼                                                   ▼
         Target Upstream Provider                          ⚡ 1ms Failover to Key #2!
            (api.xkiro.com)                                (Stream continues uninterrupted)
```

---

## ⚡ Quickstart (1-Click Setup)

### 1. Clone the Repository:
```bash
git clone https://github.com/Shivam990q/Trae-GodMode.git
cd Trae-GodMode
```

### 2. Apply God-Mode Patches to Trae:
Simply **Double-Click** [`1_CLICK_APPLY_PATCHES.bat`](1_CLICK_APPLY_PATCHES.bat).
> *Works on any Windows PC, any username, any drive (`C:`, `D:`, `E:`). Automatically backs up originals and restarts Trae.*

### 3. Setup Multi-Account Key Pool:
Open [`keys.json`](keys.json) (or copy from [`config/keys.example.json`](config/keys.example.json)) and paste your keys:
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

### 4. Launch Key Gateway:
Double-click [`START_KEY_POOLER.bat`](START_KEY_POOLER.bat).

In Trae **Model Management $\to$ Edit Model**:
* **Custom Request URL:** `http://127.0.0.1:8080/xkiro/v1` (or `http://127.0.0.1:8080/v1`)
* **API Key:** `dummy`
* **Click Save!** You now have non-stop unlimited coding.

---

## 📊 Benchmark & Comparison

| Feature | Standard Trae | Cursor / Windsurf | ⚡ Trae-GodMode |
| :--- | :---: | :---: | :---: |
| **Max Context Window** | 200k (Capped) | 128k – 200k | 🟢 **1,000,000 Tokens (1M)** |
| **Reasoning Depth Selector** | Hidden (`null`) | Static | 🟢 **6 Levels (`none` $\to$ `max`)** |
| **Terminal Auto-Run** | Requires click | Partial | 🟢 **100% Autonomous** |
| **MCP Tool Approval** | Prompts user | Prompts user | 🟢 **Auto-Approved** |
| **Multi-Key Failover** | ❌ None | ❌ None | 🟢 **Native Instant Auto-Failover** |
| **RAM Footprint** | N/A | N/A | 🟢 **< 15 MB (Ultra-Lightweight)** |

---

## 📁 Repository Structure

```
Trae-GodMode/
├── .github/                       # GitHub Actions CI/CD & Issue Templates
│   ├── workflows/
│   │   ├── ci.yml                 # Automated Python syntax & path test suite
│   │   └── release.yml            # Automated GitHub release packager
│   ├── ISSUE_TEMPLATE/            # Bug report & feature request forms
│   └── PULL_REQUEST_TEMPLATE.md
├── core/                          # Modular Python Engine
│   ├── __init__.py
│   ├── patcher.py                 # Core AST & regex patcher engine
│   ├── gateway.py                 # Pure raw pass-through HTTP key pooler
│   └── models.py                  # Model hyper-parameters & context matrix
├── config/                        # Configuration Templates
│   ├── keys.example.json          # Multi-account route templates
│   └── permissions.template.json  # 100% autonomous global permission profile
├── docs/                          # In-Depth Technical Documentation
│   ├── ARCHITECTURE.md            # System specifications & flowcharts
│   ├── MULTI_ACCOUNT_GUIDE.md     # How to pool 50+ free keys (xKiro, Bynara, KiraAI)
│   ├── BENCHMARKS.md              # Latency & throughput benchmarks
│   └── TROUBLESHOOTING.md         # Common issues & fixes
├── scripts/                       # Standalone CLI Scripts
│   ├── apply_all_patches.py       # Universal dynamic patcher
│   ├── key_pooler.py              # Standalone gateway runner
│   └── verify_installation.py     # Cross-device diagnostic suite
├── 1_CLICK_APPLY_PATCHES.bat      # Root 1-Click Patcher Launcher
├── START_KEY_POOLER.bat           # Root 1-Click Gateway Launcher
├── CHANGELOG.md                   # Version release notes
├── CONTRIBUTING.md                # Open-source contribution guide
├── SECURITY.md                    # Security & privacy policy
├── LICENSE                        # Official MIT License
└── README.md                      # Crown-jewel documentation
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://github.com/Shivam990q/Trae-GodMode/issues).

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

<div align="center">
  <sub>Built with ❤️ for the global AI developer community. Give it a ⭐ if it supercharged your workflow!</sub>
</div>
