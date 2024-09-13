from aiogram import executor
import logging
from config import bot, dp
from handlers import start, echo, commands, quiz, FSM_store
start.register_start(dp)
commands.register_send_file(dp)
quiz.register_quiz_1(dp)
FSM_store.register_FSM_store(dp)
echo.register_echo(dp)








if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)