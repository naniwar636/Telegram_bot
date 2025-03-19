from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler
import asyncio
# Actualización menor para forzar redeploy en Railway

# Reemplaza con tu token de bot
BOT_TOKEN = "7893913594:AAGRkpGC_SAcik_RyStLFPT6xHvABBz7PDE"
CHAT_ID = "5370010407"

# Función para responder al comando /start
async def start(update: Update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="El bot de Fetcher está activo")

# Configurar el bot
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

# Ejecutar el bot
async def main():
    await app.run_polling()

import asyncio

async def main():
    await app.run_polling()

if __name__ == "__main__":
    try:
        asyncio.get_running_loop()
        asyncio.create_task(main())  # Ejecutar sin bloquear el loop
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())











