from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from dotenv import load_dotenv, find_dotenv

# Find .env file
load_dotenv(find_dotenv())

class IsAdminFilter(BoundFilter):
    key = "is_admin"

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, message: types.Message):
        member = await message.bot.get_chat_member(message.chat_id, message.from_user.id)
        return member.is_chat_admin()
