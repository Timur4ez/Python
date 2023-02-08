from aiogram import executor
from handler import dp
from wolf import qu


async def startup(_):
    qu.open()
    print('Бот запущен')

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=startup)