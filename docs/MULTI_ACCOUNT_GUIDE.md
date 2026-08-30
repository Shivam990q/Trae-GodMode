# 🔑 Multi-Account API Key Pooling Guide

This guide explains how to pool 10 to 50+ free/paid accounts of the same AI provider to achieve **infinite 24/7 uninterrupted coding**.

---

## 🎯 The Strategy

Free AI providers (like xKiro, Bynara, KiraAI, Groq, OpenRouter) enforce rate limits:
* **Single Account Limit:** ~20 Requests per minute (RPM) or 100k daily tokens.
* **10 Accounts Pooled:** $10 \times 20\text{ RPM} = \mathbf{200\text{ RPM}}$ and $\mathbf{1\text{ Million Tokens/Day}}$!

---

## 🛠️ Step-by-Step Configuration:

### 1. Open `config/keys.json`
Add your accounts under the corresponding route name:
```json
{
  "routes": {
    "xkiro": {
      "upstream": "https://api.xkiro.com/v1",
      "models": ["qwen/qwen3.8-max:free", "qwen3.8-max", "*"],
      "keys": [
        "sk-xkiro-account-1",
        "sk-xkiro-account-2",
        "sk-xkiro-account-3",
        "sk-xkiro-account-4",
        "sk-xkiro-account-5"
      ]
    }
  }
}
```

### 2. Start Gateway
Run `START_KEY_POOLER.bat` in the root folder.

### 3. Point Trae to Local Gateway
In Trae's **Edit Model** dialog:
* **Custom Request URL:** `http://127.0.0.1:8080/xkiro/v1`
* **API Key:** `dummy`
* **Save!**

Whenever Account #1 hits a rate limit, the gateway automatically rotates to Account #2 in **1 millisecond**!
