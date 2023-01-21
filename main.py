import telegram
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, InputMediaPhoto
from telegram.ext import CallbackQueryHandler, CallbackContext
from telegram.ext import Updater
from telegram.ext import Dispatcher

class MyTelegramBot():
    __TOKEN = '5961429383:AAESEaDzkFL7aMEtHzMKxdc6FiBGU7s5ZI4'

    def __init__(self):
        self.bot: telegram.bot = telegram.Bot(token=self.__TOKEN)

    def check_connection(self):
        try:
            response = self.bot.get_me()
            if isinstance(response, telegram.User):
                print('Соединение установлено')
            else :
                print('Ошибка')
        except Exception as error:
            print('Ошибка: {}' .format(error))

    def start_request_processing(self):
        print('Начало обработки запросов к боту...')

    def inline_button_handler(self, update: Update, context: CallbackContext):
        pass

    def send_text(self, chat_id: int, text: str):
        pass
    def send_inline_button(self, chat_id: int, text: str):
        pass
    def send_keyboard_button(self, chat_id: int, text: str):
        pass
    def send_albuns(self, chat_id: int, caption:str):
        pass

if __name__ == '__main__':
    my_telegram_bot = MyTelegramBot()
    my_telegram_bot.check_connection()
    my_telegram_bot.start_request_processing()



