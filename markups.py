from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config as cfg
from dotenv import load_dotenv, find_dotenv

# Find .env file
load_dotenv(find_dotenv())

btnUrlChannel = InlineKeyboardButton(text='Подписаться', url=cfg.CHANNEL_URL)
channelMenu = InlineKeyboardMarkup(row_width=1)
channelMenu.insert(btnUrlChannel)
