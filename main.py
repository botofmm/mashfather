
from telegram.ext import Application, CommandHandler
import os

BOT_TOKEN = os.environ.get("6692402666:AAETpnGlaW2e5sezZLq6_WSbZ9Y5e1q4myA")

async def start(update, context):
    await update.message.reply_text("Hello from Render! Your bot is running.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
