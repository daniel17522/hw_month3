from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from handlers.buttons import sizes


class FSM_store(StatesGroup):
    product_name = State()
    size = State()
    category = State()
    price = State()
    product_photo = State()

async def start_fsm_store(message: types.Message):
    await message.answer('введите название товара:')
    await FSM_store.product_name.set()


async def load_product_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_name'] = message.text

        await message.answer('выберите размер:', reply_markup=sizes)
        await FSM_store.next()


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

        await message.answer('укажите категорию')
        await FSM_store.next()

async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

        await message.answer('укажите желаемую цену:')
        await FSM_store.next()


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

        await message.answer('отправьте фотографию товара')
        await FSM_store.next()


async def load_product_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_photo'] = message.photo[-1].file_id
        await message.answer_photo(photo=data['product_photo'],
                                   caption=f'название: {data["product_name"]}\n'
                                           f'размер: {data["size"]}\n'
                                           f'категория: {data["category"]}\n'
                                           f'цена: {data["price"]}\n')
        await state.finish()


def register_FSM_store(dp: Dispatcher):
    dp.register_message_handler(start_fsm_store, commands=['store'])
    dp.register_message_handler(load_product_name, state=FSM_store.product_name)
    dp.register_message_handler(load_size, state=FSM_store.size)
    dp.register_message_handler(load_category, state=FSM_store.category)
    dp.register_message_handler(load_price, state=FSM_store.price)
    dp.register_message_handler(load_product_photo, state=FSM_store.product_photo,
                                content_types=['photo'])




