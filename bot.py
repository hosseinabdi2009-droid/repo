import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "8962003380:AAGjfeUg9dvhHx7MfPQzkccd6ySNagQL7R0"

async def start(update, context):
    await update.message.reply_text("سلام! ربات آنلاینه 🚀")

async def echo(update, context):
    await update.message.reply_text(update.message.text)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, echo))
app.run_polling()
