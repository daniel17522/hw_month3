from aiogram import types, Dispatcher
from config import bot, dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton





async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text='next', callback_data='next1')
    markup.add(button1)
    question = "Mercedes или BMW"
    variants = ['Mercedes', 'BMW']
    await bot.send_poll(chat_id=message.from_user.id, question=question, options=variants,
                        is_anonymous=True,
                        type='quiz',
                        correct_option_id=1,
                        explanation='под индексом 1',
                        open_period=60,
                        reply_markup=markup
                        )



async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text='next', callback_data='next2')
    markup.add(button1)
    question = "Fanta или Sprite"
    variants = ['Fanta', 'Sprite']
    await bot.send_poll(chat_id=call.from_user.id, question=question, options=variants,
                        is_anonymous=True,
                        type='quiz',
                        correct_option_id=0,
                        explanation='под индексом 1',
                        open_period=60,
                        )


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text='next', callback_data='next3')
    markup.add(button1)
    question = "friend или girlfriend"
    variants = ['friend', 'girlfriend']
    await bot.send_poll(chat_id=call.from_user.id, question=question, options=variants,
                        is_anonymous=True,
                        type='quiz',
                        correct_option_id=0,
                        explanation='под индексом 1',
                        open_period=60,
                        )



def register_quiz_1(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text='next1')
    dp.register_callback_query_handler(quiz_3, text='next2')
