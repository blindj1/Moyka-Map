from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.types.web_app_info import WebAppInfo

BOT_TOKEN = '7649004045:AAFm316zw82zPpu4ZYuuWRQ6tDIB3niAuYo'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start(message: Message):

    markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Open App', web_app=WebAppInfo(url='http://localhost:63342/moyka/index.html?_ijt=gvkm1loul32n3v71u7pjqbi52l&_ij_reload=RELOAD_ON_SAVE'))]],
                                 resize_keyboard=True
                                 )

    await message.answer(text="Hey", reply_markup=markup)


if __name__ == '__main__':
    dp.run_polling(bot)
