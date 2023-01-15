# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Пример:
#     Входные данные: 'ываабв лповап абвцукв алоабвабв ываываыв'
#     Выходные данные: 'лповап ываываыв'


txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')





# Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит 2023 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#     a) Добавьте игру против бота
#     б) Подумайте, как наделить бота "интеллектом"

# Тут вариант человек против бота:
# from random import randint

def input_dat(name):
    x = int(
        input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def p_print(name, k, counter, value):
    print(
        f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0, 2)  # флаг очередности
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = randint(1, 29)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")





# Создайте программу для игры в ""Крестики-нолики"".

import random
from tkinter import *

root = Tk()         # делаем окно с заголовком
root.title('Крестики-нолики')

game_run = True     # если будет победитель, будет False
field = []          # в массиве храним состояние поля
cross_count = 0     # Подсчитываем количество крестиков на поле, максимально 5


def new_game():     # поле и переменные обнуляются
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0

def click(row, col):        # ставим крестик и считаем
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')      # проверка на победу
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')  # проверка на победу

# проверка победы по всем направлениям

def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)

# на входе три поля и символ, если символ есть в этих трех полях,
# то меняем цвет полей на розовый и остановка игры

def check_line(a1, a2, a3, smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global game_run
        game_run = False

def can_win(a1, a2, a3, smb):   # проверка на победу
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res

def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return

    while True:  # случ. образом перебираются поля, пока не выпадет свободное
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break

for row in range(3):  # создаем поле кнопок
    line = []
    for col in range(3):
        button = Button(text=' ', width=6, height=3,
                        font=('Verdana', 22, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)

new_button = Button(text='Новая игра', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

root.mainloop()




# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
#     На сжатие входные данные: 
#         WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
#     Выходные данные:          
#         12W1B12W3B24W1B14W



def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res


def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")