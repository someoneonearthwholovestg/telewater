''' This module provides the pythonic entry point for accessing telewater.
'''


import os

from telethon import TelegramClient

from telewater.bot import ALL_EVENTS
from telewater.settings import WATERMARK, API_ID, API_HASH
from telewater.utils import download_image



def start_bot(name:str, token:str):
    os.makedirs(name, exist_ok=True)
    os.chdir(name)

    if WATERMARK:
        download_image(url=WATERMARK, filename='image.png')

    client = TelegramClient(name, API_ID, API_HASH).start(bot_token=token)

    for key, val in ALL_EVENTS.items():
        print(f'Adding event {key}')
        client.add_event_handler(*val)

    client.run_until_disconnected()
    print(f'Started bot {name}')
