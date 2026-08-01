import os, threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = os.environ.get("BOT_TOKEN", "")

class Ping(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok")
    def log_message(self, *a):
        pass

def run_http():
    HTTPServer(("0.0.0.0", int(os.environ.get("PORT", 8000))), Ping).serve_forever()

async def start(update, context):
    await update.message.reply_text("سلام! ربات آنلاینه ✅")

async def echo(update, context):
    await update.message.reply_text(update.message.text)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, echo))

threading.Thread(target=run_http, daemon=True).start()
app.run_polling()
