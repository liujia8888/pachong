# Railway Web Service 版 Telegram Echo Bot

## 🚀 部署步骤

### 1. 填写 `.env`
复制 `.env.sample` → 创建 `.env`

```
BOT_TOKEN=你的 Telegram Bot Token
```

### 2. 提交到 GitHub

### 3. Railway → New → Deploy from GitHub Repo

确保你看到的服务类型是：🌐 **Web Service**

### 4. Railway → Variables 添加：

```
BOT_TOKEN=你的令牌
```

### 5. Deploy 完成 → 查看 Logs → 看到：

```
🤖 Telegram Bot 正在 polling...
```

即表示运行成功！
