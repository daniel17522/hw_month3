from aiogram import types, Dispatcher
from config import bot, dp

async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Hello daniel!')


def register_start(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])


async def send_file(message: types.Message):
    await bot.send_document(chat_id=message.from_user.id, document=open('req.txt', 'rb'))



def register_send_file(dp: Dispatcher):
    dp.register_message_handler(send_file, commands=['file'])