from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

async def reply_webapp(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    whatsapp = KeyboardButton('Whatsapp', web_app=types.WebAppInfo(url='https://web.whatsapp.com/'))

    instagram = KeyboardButton('Insta', web_app=types.WebAppInfo(url='https://www.instagram.com/'))

    youtube = KeyboardButton('Youtube', web_app=types.WebAppInfo(url='https://www.youtube.com/'))

    mangalib = KeyboardButton('Mangalib', web_app=types.WebAppInfo(url='https://mangalib.me/'))

    vk = KeyboardButton('Vk', web_app=types.WebAppInfo(url='https://vk.com/feed'))

    keyboard.add(whatsapp, instagram, youtube, mangalib, vk)

    await message.answer(text='WebApp кнопки:', reply_markup=keyboard)

def register_handler_webapp(dp: Dispatcher):
    dp.register_message_handler(reply_webapp, commands=['webapp'])
