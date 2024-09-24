from aiogram import types, Dispatcher
from config import bot, admin

async def welcome_user(message: types.Message):
    for member in message.new_chat_members:
        await message.answer(f'Добро пожаловать, {member.full_name}\n\n'
                             f'Правило группы:\n'
                             f'Не материться!\n'
                             f'Не спамить\n')

async def pin_message(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in admin:
            await message.answer('Ты не админ!')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение!')
        else:
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)

def register_admin_group(dp: Dispatcher):
    dp.register_message_handler(welcome_user,
                                content_types=[types.ContentType.NEW_CHAT_MEMBERS])
    dp.register_message_handler(pin_message, commands=['pin'])