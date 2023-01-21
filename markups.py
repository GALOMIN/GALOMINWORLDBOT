from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config as cfg

btnUrlChannel = InlineKeyboardButton(text='Подписаться', url=cfg.CHANNEL_URL)
channelMenu = InlineKeyboardMarkup(row_width=1)
channelMenu.insert(btnUrlChannel)