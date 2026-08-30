# ⚡ Trae-GodMode 体验指南 (中文版)
### *为 ByteDance Trae AI IDE 解锁 100万 Token 超大上下文、全自主运行与无限制多账号密钥池*

---

## 📖 项目简介

**Trae-GodMode** 是专为字节跳动 **Trae AI IDE** 打造的终极增强模块与毫秒级密钥分发网关。通过动态 AST 补丁与本地零延迟代理，彻底解除原生 IDE 的各种限制。

---

## ⚡ 五大核心能力

| 特性 | 原生 Trae | ⚡ GodMode 开启后 |
| :--- | :---: | :--- |
| 🧠 **深度思考 (CoT)** | 隐藏 / 锁定 | **完整 6 级调节 (`none` → `max`)**，默认最深思考 |
| ⚡ **全自主免确认** | 频繁弹窗询问 | **100% 自动执行** 终端命令、文件读写与 MCP 工具 |
| 💾 **100万 Token 上下文** | 受限 200k | **解锁 1,048,576 Tokens (1M)**，轻松容纳超大代码库 |
| 🔄 **多账号密钥池** | 单账号易 429 限流 | **<0.5ms 毫秒级故障转移**，支持汇聚 5~50+ 免费账号 |
| 🔓 **模型工坊解锁** | 字段置灰只读 | **完全可编辑** 自定义 URL、模型名称、协议与密钥 |

---

## 🚀 3 步快速上手

### 第 1 步：克隆仓库
```bash
git clone https://github.com/Shivam990q/Trae-GodMode.git
cd Trae-GodMode
```

### 第 2 步：一键应用补丁
双击运行 **`1_CLICK_APPLY_PATCHES.bat`**
> 🛡️ *自动检索任意磁盘上的 Trae 安装目录，自动备份原文件，注入补丁并瞬间重启 Trae。*

### 第 3 步：配置密钥池并启动
复制模板生成 `keys.json`：
```json
{
  "routes": {
    "xkiro": {
      "upstream": "https://api.xkiro.com/v1",
      "models": ["qwen/qwen3.8-max:free", "*"],
      "keys": [
        "sk-your-key-1",
        "sk-your-key-2"
      ]
    }
  }
}
```
双击运行 **`START_KEY_POOLER.bat`**，在 Trae 的「Edit Model」中将请求地址设置为 `http://127.0.0.1:8080/xkiro/v1` 即可畅享无限制 AI 编程！

---

## 📜 开源协议

基于 **MIT License** 开源。
