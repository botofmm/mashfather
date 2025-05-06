
from telegram.ext import Application, CommandHandler
import os

BOT_TOKEN = os.environ.get("8083903273:AAHSMjhrF7Hpi-9YSmi6ZwLoLQyspAkuorA")

async def start(update, context):
    await update.message.reply_text("Hello from Render! Your bot is running.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
