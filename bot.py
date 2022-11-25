import logging
from decouple import config
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome to bot program!')

app = ApplicationBuilder().token(config('TOKEN')).build()

app.add_handler(CommandHandler("start", start))


if __name__ == "__main__":
    app.run_polling()
