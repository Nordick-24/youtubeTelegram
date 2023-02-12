#!/usr/bin/env python3
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


@dp.message_handler(commands=['download'])
async def download(message: aiogram.types.Message) -> None:
    await message.answer("Write A link")


    @dp.message_handler()
    async def getLink(message: aiogram.types.Message) -> None:
        await message.reply(f"Processing for You!")


        youtube_video = YouTube(message.text)
        youtube_video = youtube_video.streams.get_highest_resolution()
        youtube_video.download(output_path="video/", filename="video.mp4")

        with open("video/video.mp4", 'rb') as donwloaded_video:
            await bot.send_video(message.from_user.id, donwloaded_video)



