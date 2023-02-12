import logging
import os

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = os.getenv("API_TELEGRAM")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def startAndHelp(message: types.Message) -> None:
    await message.reply("Works!")

