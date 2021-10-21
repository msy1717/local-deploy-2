# < (c) 2021 @Godmrunal >

import logging
from os import remove

import requests
from decouple import config
from telethon import Button, TelegramClient, events

BOT_TOKEN = '2064536076:AAHdciaJTq3DH2XclNyWBqLgb8pFCF630E8'
logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

bot = TelegramClient(None, api_id=6, api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e").start(
    bot_token=("BOT_TOKEN")
)

logging.info("Starting bot...")


@bot.on(events.NewMessage(incoming=True, pattern="^/start"))
async def start_(event):
    await event.reply(
        "Hi {}!\nI am a simple bot. \n\n**Usage:** This bot will help to start first bot in python!".format(
            (await bot.get_entity(event.sender_id)).first_name
        ),
        buttons=[
            [
                Button.url("Repo", url="https://github.com/msy1717/startBot"),
                Button.url(
                    "Developer", url="https://t.me/Godmrunal"
                ),
            ],
            [Button.url("Channel", url="https://t.me/Botz_Official")],
        ],
    )




logging.info("\n\nBot has started.\n(c) @Godmrunal")

bot.run_until_disconnected()
