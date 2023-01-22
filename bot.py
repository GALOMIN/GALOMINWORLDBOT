import logging
from aiogram import Bot, Dispatcher, executor, types
import filters
from filters import IsAdminFilter
from dotenv import load_dotenv, find_dotenv

import config as cfg
import markups as nav

# Find .env file
load_dotenv(find_dotenv())

logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)

dp.filters_factory.bind(IsAdminFilter)

# Проверка на подписку на канал
def check_sub_channel(chat_member):
    return chat_member['status'] != 'left'

# Команда ban
@dp.message_handler(is_admin=True, commands=["ban"], commands_prefix="/")
async def cmd_ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение!")

    await message.bot.delete_message(chat_id=cfg.GROUP_ID)
    await message.bot.kick_chat_member(chat_id=cfg.GROUP_ID, user_id=message.reply_to_message.from_user.id)

    await message.reply_to_message.reply("Пользователь забанен!")
    
# Удаление сообщений о приходе новых участников
@dp.message_handler(content_types=['new_chat_members'])
async def user_joined(message: types.Message):
    await message.delete()

# Приветствие нового участника
@dp.message_handler(content_types=['new_chat_members'])
async def user_joined(message: types.Message):
    await message.answer("Добро пожаловать!\nЧтобы отправлять сообщения, вам необходимо подписаться на канал!", reply_markup=nav.channelMenu)

# Если человек не подписан на канал, то он ничего не сможет писать в чате, его сообщения бот будет удалять сразу же и затем скидывать сообщений о просьбе подписаться на канал
# Только после подписки на канал вы сможете писать в чат
@dp.message_handler()
async def mess_handler(message: types.Message):

    if check_sub_channel(await bot.get_chat_member(chat_id=cfg.CHANNEL_ID, user_id=message.from_user.id)):
       text = message.text.lower() # Фильтр нецензурных выражений (сам фильтр находится в config.py)
       for word in cfg.WORDS:
           if word in text:
               await message.delete()
    else:
        await message.answer("Чтобы отправлять сообщения, подпишитесь на наш канал", reply_markup=nav.channelMenu)
        await message.delete()

#Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp)
