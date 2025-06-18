from dotenv import load_dotenv
load_dotenv()

import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Привет! Бот запущен и готов.")


def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("Заполните BOT_TOKEN в .env")

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Бот запущен. Нажмите Ctrl+C для остановки.")
    app.run_polling()          # ← одна строка делает всё за нас


if __name__ == "__main__":
    main()                     # ← НЕТ asyncio.run
