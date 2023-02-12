from pytube import YouTube

from loguru import logger
import logging

import os
import aiogram


api_token = os.getenv("API_TELEGRAM")

logging.basicConfig(level=logging.INFO)

bot = aiogram.Bot(token=api_token)
dp = aiogram.Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: aiogram.types.Message) -> None:
    await message.answer(f"Hello {message.from_user.first_name}, its bot for download the videos from Youtube")


if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)

