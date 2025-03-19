from telegram import Bot
import asyncio

# Reemplaza con tu token y tu ID de Telegram
BOT_TOKEN = "7893913594:AAGRkpgC_SAcik_RyStLFPT6xHvABBr7PbE"
CHAT_ID = "5370010407"

bot = Bot(token=BOT_TOKEN)

# Función asíncrona para enviar el mensaje
async def send_message():
    await bot.send_message(chat_id=CHAT_ID, text="El bot de Fetcher está activo")

# Ejecutar la función asíncrona
asyncio.run(send_message())
from telegram import Bot

# Reemplaza con tu token y tu ID de Telegram
BOT_TOKEN = "TU_TOKEN_DE_TELEGRAM"
CHAT_ID = "TU_ID_DE_TELEGRAM"

bot = Bot(token=BOT_TOKEN)

# Prueba enviando un mensaje
bot.send_message(chat_id=CHAT_ID, text="El bot de Fetcher está activo")
from telegram import Bot

# Reemplaza con tu token y tu ID de Telegram
BOT_TOKEN = "TU_TOKEN_DE_TELEGRAM"
CHAT_ID = "TU_ID_DE_TELEGRAM"

bot = Bot(token=BOT_TOKEN)

# Prueba enviando un mensaje
bot.send_message(chat_id=CHAT_ID, text="El bot de Fetcher está activo")

