import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 8080))

if not TOKEN:
    raise RuntimeError("❌ BOT_TOKEN 未设置！请在 Railway → Variables 添加 BOT_TOKEN")

app = FastAPI()

@app.get("/")
async def home():
    return {"status": "running", "bot": "echo-bot"}

async def telegram_bot():
    bot_app = ApplicationBuilder().token(TOKEN).build()

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("欢迎，我是 Echo Bot！")

    async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(update.message.text)

    bot_app.add_handler(CommandHandler("start", start))
    bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("🤖 Telegram Bot 正在 polling...")
    await bot_app.run_polling()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(telegram_bot())
    uvicorn.run(app, host="0.0.0.0", port=PORT)
