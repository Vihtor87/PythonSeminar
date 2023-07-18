# Цикл While

# Выведите слово Hello 10 раз

# i = 0
# while i < 10:
#     print('Hello')
#     i += 1


# Вводятся числа, пока не введут 0. Определите кол-во четных чисел из введенной последовательности

# count = 0
# while True:
#     number = int(input())
#     if number == 0:
#         break
#     if number % 2 == 0:
#         count += 1
# print(count)

# count = 0
# number = int(input())
# while number != 0:
#     if number % 2 == 0:
#         count += 1
#     number = int(input())
# print(count)

# Цикл for
# Переменная - итератор используется

# for i in 'hello world!':
#     print(i)

# for j in range(5):  # 0, 1, 2, 3, 4
#     print(j)

# for j in range(5, 10):
#     print(j)

# for j in range(5, 10, 2):
#     print(j)

# for j in range(10, 5, -1):
#     print(j, end=' ')


# some_str = 'привет мир!'
# # for i in some_str:
# #     print(i)
#
# for ind in range(0, len(some_str), 2):  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#     print(some_str[ind])
#
# for ind in range(len(some_str) - 1, -1, -1):
#     print(some_str[ind], end='')

# Переменная итератор не используется

# Вывести hello 10 раз

# for _ in range(10):  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#     print('hello')

# Вывести слово hello n раз

# n = int(input())
# for _ in range(n):
#     print('hello')

# Вводится кол-во чисел, затем сами числа. Найти произведение нечетных чисел.

# count = int(input('Введите количество чисел: '))
# temp = 1
# for _ in range(count):
#     num = int(input('Введите число: '))
#     if num % 2 != 0:
#         temp = temp * num
# print(temp)


"""
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
"""

# n = int(input('Введите число: '))
# mylt = 1
# while n > 0:
#     mylt *= n
#     n -= 1
# print(mylt)

# second variant
# n = int(input('Введите число: '))
# mylt = 1
# for i in range(1, n + 1):
#     mylt = mylt * i
# print(mylt)


"""
Дано натуральное число A > 1. Определите, каким по 
счету числом Фибоначчи оно является, то есть 
выведите такое число n, что φ(n)=A. Если А не 
является числом Фибоначчи, выведите число -1.
"""

# a = int(input("Введите число: "))
# f_first = 0
# f_second = 1
# f_next = f_first + f_second
# count = 3
# while a > f_next:
#     f_first = f_second
#     f_second = f_next
#     f_next = f_first + f_second
#     count += 1
# if a == f_next:
#     print(count)
# else:
#     print(-1)

"""
Напишите программу, помогающую синоптикам в работе.
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел.
Каждое число – среднесуточная температура в соответствующий день.
Температуры – целые числа и лежат в диапазоне от –50 до 50
"""
# value_day = int(input('Введите количество дней: '))
# count_day = 0
# max_count_day = 0
# for _ in range(value_day):
#     temp = int(input('Введите дневную темпераратуру: '))
#     if temp >= 0:
#         count_day += 1
#     else:
#         if count_day > max_count_day:
#             max_count_day = count_day
#         count_day = 0
# if count_day > max_count_day:
#     max_count_day = count_day
# print(max_count_day)

"""
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
Но вот незадача: арбузов слишком много и он не знает как же выбрать 
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов.
Вторая строка содержит N чисел, записанных на новой строчке каждое.
Здесь каждое число – это масса соответствующего арбуза
"""

# n = int(input('Введите количество арбузов: '))
# w_min = int(input('Введите вес арбуза: '))
# w_max = 0
# for _ in range(n - 1):
#     w = int(input('Введите вес арбуза: '))
#     if w > w_max:
#         w_max = w
#     elif w < w_min:
#         w_min = w
# print(w_min, w_max)
