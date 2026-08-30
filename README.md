# 🌟 Trae Peak Autonomy & Multi-Key Unlimited Mod Suite

An all-in-one autonomy, reasoning unlocker, and **Multi-Key Auto-Failover Pooler** for **Trae AI IDE**.

---

## 🚀 Key Features:

1. **🔑 Multi-Account / Multi-Key Pooling & Auto-Failover (`key_pooler.py`):**
   * Multiple API keys ko ek single pool mein combine karta hai.
   * **Automatic 429 / Quota Failover:** Agar Key #1 limit ho jaye to instant Key #2, Key #3 par switch karta hai bina coding roke.
   * **Round-Robin Load Balancing:** Har account par barabar load divide karta hai.

2. **🧠 Uncapped Thinking Effort (Reasoning Levels):**
   * Unlocks all 6 reasoning depth levels: `none`, `low`, `medium`, `high`, `xhigh`, `max` across all models.
   * Defaults to `max` reasoning tokens for deep logical scratchpads.

3. **⚡ 100% Omni-Autonomy (Zero Interruption Execution):**
   * Terminal commands, MCP tools, file deletions, aur multi-step plans bina kisi popup ke **auto-execute** hote hain.

4. **💾 1 Million Token Context Memory:**
   * Unlocks 1M Max Mode for `Seed-2.1-Turbo`, `Gemini-3.1-Pro`, `Gemini-3-Flash`, and Custom Models (1,048,576 tokens).

5. **🔓 Fully Unlocked "Edit Model" Dialog:**
   * Request URL, Model ID, Full URL toggle, API Format, and API Keys are 100% editable.

---

## 🛠️ How to Use:

### Step 1: Add Your Multiple API Keys
Open [`keys.json`](file:///C:/Users/Rose/Trae_Peak_Autonomy_Mod/keys.json) and paste your keys:
```json
{
  "routes": {
    "xkiro": {
      "upstream": "https://api.xkiro.com/v1",
      "models": ["qwen/qwen3.8-max:free", "*"],
      "keys": [
        "sk-your-xkiro-key-1",
        "sk-your-xkiro-key-2",
        "sk-your-xkiro-key-3"
      ]
    }
  }
}
```

### Step 2: Start the Key Pooler
Double-click [`START_KEY_POOLER.bat`](file:///C:/Users/Rose/Trae_Peak_Autonomy_Mod/START_KEY_POOLER.bat).

### Step 3: Set URL in Trae
In Trae's **Edit Model** dialog:
* **Custom Request URL:** `http://127.0.0.1:8080/v1` (or `http://127.0.0.1:8080/xkiro/v1`)
* **API Key:** Leave as dummy or paste any key.
* **Save!** Trae is now connected to your unlimited key pool!
