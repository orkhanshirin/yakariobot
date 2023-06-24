from constants import API_KEY, BOT_USERNAME
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import responses as resp
import logging

LOG = logging.getLogger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm Yakari.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Type something hot to get started!")

async def handle_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg_type: str = update.message.chat.type
    text: str = update.message.text
    
    LOG.info(f"User ({update.message.chat.id} in {msg_type}: '{text}')")
    
    if msg_type == "group":
        if BOT_USERNAME in text:
            text.replace(BOT_USERNAME, "").strip()
            response: str = resp.sample_responses(text)
        else:
            return
    else:
        response: str = resp.sample_responses(text)
    
    LOG.info("Bot:", response)
    await update.message.reply_text(response)

async def logs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    LOG.info(f"[ERROR] Update {update}, caused an error {context.error}")


if __name__=="__main__":
    LOG.info("Yakari on the board!")

    app = ApplicationBuilder().token(API_KEY).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_msg))

    # Errors
    app.add_error_handler(logs)

    # Polls the bot
    LOG.info("Polling...")
    app.run_polling(poll_interval=3)
