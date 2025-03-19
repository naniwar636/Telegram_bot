from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

# Reemplaza con tu token de bot
BOT_TOKEN = "7893913594:AAGRkpGC_SAcik_RyStLFPT6xHvABBz7PbE"
CHAT_ID = "5370010407"

# Función para responder al comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="El bot de Fetcher está activo")

# Configurar el bot
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

# Ejecutar el bot
import asyncio

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())







