# list

# some_list = []
# print(type(some_list))
#
# some_list = [1, 3.44, 'hello', True, [1, 2, 3]]
# print(some_list)
#
# print(some_list[-1])
#
# print(some_list[::-1])

# Вводится количество чисел, затем сами числа

# count = int(input('Введите кол-во чисел: '))
# some_list = []
# for _ in range(count):
#     num = int(input())
#     if  num % 2 == 0:
#         some_list.append(num)
# print(some_list)


# Задачки:

import random

# count = int(input('Введите кол-во элементов: '))
# some_list = []
# for _ in range(count):
#     number = random.randint(0, 10)
#     some_list.append(number)
# print(some_list)

'''
1.Создайте список из случайных чисел.
Найдите номер его последнего локального максимума
(локальный максимум — это элемент, который больше любого из своих соседей).
'''

# Идём с начала:
# some_list = [1, 10, 2, 0, 7, 4, 8, 6]
# local_max = None
# for ind in range(1, len(some_list) - 1):
#     if some_list[ind - 1] < some_list[ind] > some_list[ind + 1]:
#         local_max = ind
# print(local_max)

# Идём с конца:
# some_list = [1, 10, 2, 0, 7, 4, 8, 6]
# local_max = None
# for ind in range(len(some_list) - 2, 0, -1):
#     if some_list[ind - 1] < some_list[ind] > some_list[ind + 1]:
#         local_max = ind
#         break
# print(local_max)

'''
Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.
'''

# some_list = [1, 2, 3, 1, 5, 6, 2, 2, 2]
# max_count = 0
# for el in some_list:
#     count = 0
#     for i in some_list:
#         if el == i:
#             count += 1
#     if count > max_count:
#         max_count = count
# print(max_count)

'''
Задача №17.
Решение в группах
Дан список чисел. Определите, сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
'''

# some_list = [1, 1, 2, 0, -1, 3, 4, 4, 8, 8]
# new_list = []
# for el in some_list:
#     if el not in new_list:
#         new_list.append(el)
# print(len(new_list))

'''
Задача №19.
Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
(сдвиг - циклический) на K элементов вправо, K – положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
'''

# some_list = [1, 2, 3, 4, 5]
# k = int(input('Введите число: '))
# print(some_list[k:] + some_list[:k])

'''
Задача №23
Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество 
элементов массива, больших предыдущего (элемента с предыдущим номером) 
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
'''

# some_list = [0, -1, 5, 2, 3]
# count = 0
# for ind in range(1, len(some_list)):
#     if some_list[ind - 1] < some_list[ind]:
#         count += 1
# print(count)