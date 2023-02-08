from config import dp
from aiogram import types
from wolf import qu
from random import randint as RI

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}, лови мудрость!')
    li = qu.get()
    num = RI(0, len(li)-1)
    await message.answer(li[num])