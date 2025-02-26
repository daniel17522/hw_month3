from aiogram import executor
import logging
from config import bot, dp
from handlers import  echo, commands, quiz,FSM_store, fsm_store_2, webapp, admin_group, send_products
from db import db_main

async def on_startup(_):
    await db_main.sql_create()



commands.register_start(dp)
commands.register_send_file(dp)
quiz.register_quiz_1(dp)
send_products.register_send_products_handler(dp)
#FSM_store.register_FSM_store(dp)
webapp.register_handler_webapp(dp)
admin_group.register_admin_group(dp)
fsm_store_2.register_store(dp)
echo.register_echo(dp)








if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)