from multiprocessing.sharedctypes import Value
from time import clock_getres



# print(type(a))
# print(type(b))
# value = 12345
# print(type(value))
# print(s)
# a = 123
# b = 1.23
# s = 'hello world'
# print(a, b, s)
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = ['1', '2', '3', 'hello']
# col = ['1', '2', '3', 'hello']
# print(list)
# print('Введите a')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a, ' + ', b, ' = ', a+b)
# print(f'{a} {b}')
# print('{} {}'.format(a, b))

# арифметические операции
# +, -, *. /, %, // - деление показывает только целую часть ответа, ** - возведение в степень
# **, (+), (-)
# () - сокращенные операции
# a = 1.32154
# b = 3
# c = round(a * b, 30)
# print(c)

# сокращенные операции
# a = 3
# a += 5
# print(a)

# логические операции
# >, >=, <, <=,==, !=,
# not,and, or - не путать с &, |, ^
# кое-что еще: is, is not, in, not in
# f = [1, 2, 3, 4]
# a = 1 > 4 or 2 < 5
# is_odd = not f[0] % 2
# print(is_odd)

# управляющие конструкции
# if , else 

# a = int(input('a = '))
# b = int(input('b = '))

# if a > b:
#     print(a)
# else:
#     print(b)

# управляющие конструкции
# while

# original = 23
# inverted = 0

# while original != 0:
#     inverted = inverted * 10 + (original % 10) // переворачиваем число ( ответ 32)
#     original //= 10
# print(inverted)


# original = 23
# inverted = 0

# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10

# else:
#     print('Пожалуй')
#     print('хватит')

# print(inverted)

# управляющие конструкции
# for

# for i in 1,2,3,4,10,5:
#     print(i**2)
# for i in range(1, 10, 2):
#     print(i)

# Немного о строках
# text = 'сьешь еще этих мягких французских булок'
# help(int)

# print(len(text))
# print('еще' in text)
# print(text.isdigit())
# print(text.islower())
# print(text.replace('еще', 'ЕЩЕ'))

# for с in text:
#     print(с)

# Списки

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))

# print(f'{len(numbers)} len')
# numbers[0] = 10
# print(numbers)
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)

# colors = ['red, green, blue']

# for e in colors:
#     print(e)

# for e in colors:
#     print(e*2)

# colors.append('grey')
# print(colors == ['red', 'green', 'blue', 'gray'])
# colors.remove('red')

# функции

# def f(x):
#     if x == 1:
#         return 'целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 1
# print(f(arg))
# print(type(f(arg)))

