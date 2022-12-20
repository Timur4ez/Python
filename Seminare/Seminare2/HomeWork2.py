# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*    
#     - 6782 -> 23
#     - 0,56 -> 11

num = input("Enter the number: ")
sum = 0
for i in num:
    if i!=".":
        sum = sum + int(i)
print(f"The sum of the {num} is: ", sum)

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial (number, count = 1):
    for i in range(1, number + 1):
        count *= i
    return count

n = int(input('Enter the number: '))
print(f'Set of products of numbers from 1 to {n} = ', end = '')
for i in range(1, n + 1):
    if i == n: 
        print(f'{factorial(i)}')
    else:
        print(f'{factorial(i)}', end = ', ')

# 3. Задайте список из n чисел последовательности ((1 + 1/n)  в степени n) и выведите на экран их сумму.
# *Пример:*    
#     - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

n = int(input('Enter number: ')) 
def sequence(n):
    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
print(sequence(n))
print(round(sum(sequence(n))))

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint (-10,10))
print(numbers)
def get_numbers(numbers):
    count =0 
    for element in numbers:
        count +=1
    return count
print('Number of elements: ', get_numbers(numbers))
x = int(input('Enter  position of first element: '))
y = int(input('Enter position of second element: '))
for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print(f'Mult of elements: {numbers[x -1]} * {numbers[y -1]} =', mult)

# 5. Реализуйте алгоритм перемешивания списка.

import random
def mix_list(list_original):
    list = list_original[:]
    list_length = len(list)
    for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    return list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed_list = mix_list(list)
print("Primary list: ")
print(list)
print("Mixed list: ")
print(mixed_list)