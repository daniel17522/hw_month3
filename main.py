from aiogram import executor
from config import bot, dp
from handlers import start, echo, commands
start.register_start(dp)
commands.register_send_file(dp)
echo.register_echo(dp)








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)