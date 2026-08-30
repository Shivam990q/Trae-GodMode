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
[![Context Window](https://img.shields.io/badge/Context%20Window-1%2C000%2C000%20Tokens-FF6B6B?style=for-the-badge)](README.md)
[![Autonomy](https://img.shields.io/badge/Autonomy-100%25%20Zero--Friction-7952B3?style=for-the-badge)](README.md)
[![Key Pooling](https://img.shields.io/badge/Multi--Key%20Pool-Infinite%20Failover-4D96FF?style=for-the-badge)](README.md)
[![Latency Overhead](https://img.shields.io/badge/Latency-%3C0.5ms%20Pass--Through-success?style=for-the-badge)](README.md)

<p align="center">
  <b>Unleash Trae IDE to its absolute theoretical peak. No throttles. No confirmation popups. Unlimited API key pooling. 1 Million tokens memory.</b>
</p>

---

</div>

## 🌌 What is Trae-GodMode?

**Trae-GodMode** is an open-source, zero-dependency modification suite and native high-speed gateway designed specifically for **ByteDance Trae IDE & Trae Solo**. 

It transforms Trae into an **uncapped, fully autonomous, infinite-quota AI powerstation** by unlocking hidden developer tiers, automating all tool execution prompts, and pooling multiple free/paid API keys with sub-millisecond failover.

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

## 🏗️ Architecture Blueprint

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
                              │   ⚡ TRAE-GODMODE KEY POOLER      │
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
git clone https://github.com/YOUR_USERNAME/Trae-GodMode.git
cd Trae-GodMode
```

### 2. Apply God-Mode Patches to Trae:
Simply **Double-Click** [`1_CLICK_APPLY_PATCHES.bat`](1_CLICK_APPLY_PATCHES.bat).
> *Works on any Windows PC, any username, any drive (`C:`, `D:`, `E:`). Automatically backs up originals and restarts Trae.*

### 3. Setup Multi-Account Key Pool:
Open [`keys.json`](keys.json) and paste your multiple API keys for any provider:
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
├── ⚡ 1_CLICK_APPLY_PATCHES.bat   # 1-Click universal patcher for Trae updates
├── 🚀 START_KEY_POOLER.bat        # 1-Click multi-account key failover gateway
├── 🐍 apply_all_patches.py        # Dynamic AST patch engine (Multi-PC/Drive detection)
├── 🔑 key_pooler.py               # Zero-latency, 429 auto-failover proxy engine
├── 📋 keys.example.json           # Clean template for public users
├── ⚙️ keys.json                  # Local key config file
├── 🧪 verify_installation.py      # Automated self-test diagnostic suite
├── 🛡️ .gitignore                  # Prevents accidental leak of private keys
├── 📜 LICENSE                     # Official MIT Open-Source License
├── 📄 index.mjs.patched           # Standalone bundle backup
├── 🔒 global.json.backup          # Autonomous security profile
└── 📖 README.md                   # Complete documentation
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check [issues page](https://github.com/YOUR_USERNAME/Trae-GodMode/issues).

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'feat: Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

<div align="center">
  <sub>Built with ❤️ for the global AI developer community. Give it a ⭐ if it supercharged your workflow!</sub>
</div>
