from aiogram import types
from aiogram.dispatcher.filters import Text
from random import randint as RI
from config import dp
from my_bot import my_bot

from text import text_1

users = {}


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'Приветствую тебя, {message.from_user.first_name}!\n \n/game - Начать игру 🎮  \n/help - Читать правила 👀')


@dp.message_handler(commands=['help'])
async def start(message: types.Message):
    await message.answer(text_1)
    await message.answer(f'УТЧ: Чтобы задать количество конфет в ведите /game "NUM", где NUM это желаемое кол-во 🍬 ')


@dp.message_handler(commands=['game'])
async def start(message: types.Message):

    global users
    candys = 2023

    if len(message.text) != 5 and message.text[5:].replace(' ','').isdigit():
        candys = int(message.text[5:].replace(' ',''))

    users[message.from_user.id] = [candys]
    await message.answer(f'\nДа начнутся голодные игры!\n На столе лежит {users[message.from_user.id][0]} 🍬🍬🍬')

    fate = RI(0,1)

    if fate:
        await message.answer(f'По итогам жеребьевки, первый ход за тобой 🫵, сколько возьмешь 🍬? ')
    else:
        await message.answer(f'По итогам жеребьевки, первым ходит бот')
        num = my_bot(users[message.from_user.id][0])
        users[message.from_user.id][0] -= num
        await message.answer(f'Бот взял {num} 🍬, на столе осталось {users[message.from_user.id][0]} 🍬.')


@dp.message_handler()
async def mes_all(message: types.Message):
    global users


    if message.from_user.id in users:
        if message.text.isdigit(): 
            if 0 < int(message.text) < 29:
                users[message.from_user.id][0] -= int(message.text)
                if users[message.from_user.id][0] > 0:
                    await message.answer(f'На столе осталось {users[message.from_user.id][0]} 🍬')
                    num = my_bot(users[message.from_user.id][0])
                    users[message.from_user.id][0] -= num
                    if users[message.from_user.id][0] > 0:
                        await message.answer(f'Бот взял {num} 🍬, на столе осталось {users[message.from_user.id][0]} 🍬. \nСколько возьмешь 🍬?')
                    else:

                        await message.answer('... и их забрал бот! \nПобедил бот 🤖, грядет восстание машин!')
                        
                else:
                    await message.answer(f'{message.from_user.first_name} одерживает победу🏆!')
                    users.pop(message.from_user.id)
            else:
                await message.answer('За раз можно взять не более 28 конфет!')
        else:
            await message.answer(f'Не понял, повтори')
    else:
        await message.answer('На столе нет конфет. \nЧтобы начать играть жми /game ')