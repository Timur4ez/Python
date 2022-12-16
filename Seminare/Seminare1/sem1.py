# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# a = int(input('a = '))
# b = int(input('b = '))
# if a * a == b:
#     print(True)
# else:
#     print(False)

# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# some_list = []
# for _ in range(5): # 0, 1, 2, 3, 4
#     x = int(input())
#     some_list.append(x)
# # print(max(some_list))
# maxx = some_list[0]
# for el in some_list:
#     if el > maxx:
#         maxx = el
# print(maxx)

# maxx = int(input())
# for _ in range(4):
#     x = int(input())   
#     if x > maxx:
#         maxx = x
# print(maxx)

# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# *Примеры:* - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# number = int(input('number = '))
# print('мы получили:', end = ' ') # Не обязательная строка
# print(*range(-number, number + 1, 2), sep = ', ') 

# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#    *Примеры:* - 6,78 -> 7. - 5 -> нет. - 0,34 -> 3

# number = float(input('number = '))
# if number % 1 == 0:
#     print('Нет')
# else:
#     print(int(number * 10) % 10)

# a = input()
# if '.' in a:
#     ind = a.index('.')
#     print(a[ind + 1])
# else:
#     print('нет')


# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# a = int(input())
# if (a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and a % 30 != 0:
#     print('да')
# else:
#     print('нет')

# print((a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and a % 30 != 0)