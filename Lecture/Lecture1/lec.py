# value = None
# print(type(value))
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334
# print(type(value))

# s = 'hello \nworld'
# print(a, ' - ',b, ' - ',s)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = False
# print(f)

# list = ['1', '2', '3']
# col = ['hello', 1,2,4.5,True]
# print(list)
# print(col)

# print('Введите a')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a,' + ', b, ' = ', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# a = 1.31231223
# b = 3
# c = round(a * b, 7)
# print(c)

# a = 3
# a *= 5
# print(a)

# f =  [1,2,3,4]
# # print(f)
# # print(not 2 in f)

# is_od = not f[0] % 2 == 00
# print(is_od)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#  print('Ура, это же МАША!')
# elif username == 'Марина':
#  print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#  print('Ильнар - топ)')
# else:
#  print('Привет, ', username)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# for i in range(1, 10, 2):
#     print(i)

# r = range(5) # range(0, 5)
# r = range(2, 5) # range(2, 5)
# r = range(-5, 0) # range(-5, 0)
# r = range(1, 10, 2) # range(1, 10, 2)
# r = range(100, 0, -20) # range(100, 0, -20)

# text = 'съешь ещё этих мягких французских булок'

# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#     print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e) # red green blue
# for e in colors:
#     print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
# arg = 2
# print(f(arg))
# print(type(f(arg)))