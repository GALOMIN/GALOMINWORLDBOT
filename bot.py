import logging
from aiogram import Bot, Dispatcher, executor, types

import config as cfg
import markups as nav

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)

def check_sub_channel(chat_member):
    return chat_member['status'] != 'left'

@dp.message_handler(content_types=["new_chat_member"])
async def user_joined(message: types.Message):
    await message.answer("Добро пожаловать в наш чат! \nЧтобы отправлять сообщения, нужно подписаться на канал", reply_markup=nav.channelMenu)

@dp.message_handler(content_types=['new_chat_members'])
async def user_joined(message: types.Message):
    await message.answer("Добро пожаловать!\nЧтобы отправлять сообщения, вам необходимо подписаться на канал!", reply_markup=nav.channelMenu)

@dp.message_handler()
async def mess_handler(message: types.Message):

    if check_sub_channel(await bot.get_chat_member(chat_id=cfg.CHANNEL_ID, user_id=message.from_user.id)):
       text = message.text.lower()
       for word in cfg.WORDS:
           if word in text:
               await message.delete()
    else:
        await message.answer("Чтобы отправлять сообщения, подпишитесь на наш канал", reply_markup=nav.channelMenu)
        await message.delete()

if __name__ == "__main__":
    executor.start_polling(dp)