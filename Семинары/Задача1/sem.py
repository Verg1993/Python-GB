# Задача 1.
# 1.	Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# Примеры:
# o	5, 25 -> да
# o	4, 16 -> да
# o	25, 5 -> да
# o	8,9 -> нет

# a = int(input('a = '))
# b = int(input('b = '))

# if a == b ** 2:
#     print('да')
# elif b == a ** 2:
#     print('да')
# else:
#     print('нет')

# Задача 2
# 	Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# o	1, 4, 8, 7, 5 -> 8
# o	78, 55, 36, 90, 2 -> 90

# list = [1, 2, 6, 8, 1]
# max = list[0]

# for i in list:
#     if i > max:
#         max = i
# print(max)

# Задача 3

# 	Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# Примеры:
# o	5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# n = int(input('n = '))

# for i in range(-n, n + 1):
#     print(i, end = " ")

# Задача 4

# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:
# o	6,78 -> 7
# o	5 -> нет
# o	0,34 -> 3

# a = float(input('a = '))
# if int(a * 10 % 10) != 0:
#     print(int(a * 10 % 10))
# else:
#     print('нет')


# Задача 5
# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# a = int(input('a = '))

# if (a % 5 == 0) and (a % 10 == 0) or (a % 15 == 0) and (a % 30 != 0):
#     print('кратно')
# else:
#     print('не кратно')

# Задача 6
# удалить 2 цифру трехзначного числа
# number = 123
# a = 123 % 10
# b = number // 100
# new_number = b * 10 + a
# print(new_number)

# Задача 7
# По заданному номеру числа вывести название дня недели.
# week = ['понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

# number = int(input('день недели = '))
# if 8 > number > 0:
#     print(week[number-1])
# else:
#     print('такого дня недели нет')