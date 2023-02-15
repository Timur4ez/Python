from aiogram import executor
from handler import dp

async def start_bot(_):
    print('Бот запущен')

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_bot)