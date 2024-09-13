from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

sizes = ReplyKeyboardMarkup().add(
    KeyboardButton(text='XL'),
    KeyboardButton(text='3XL'),
    KeyboardButton(text='L')
)