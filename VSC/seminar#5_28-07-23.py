'''Задача №31.
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ...,
где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
'''


# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fib(n - 2) + fib(n - 1)
#
# print(fib(int(input('Введите число: '))))


# def fib_while(n):
#     if n == 1 or n == 2:
#         return 1
#     a0 = 1
#     a1 = 1
#     temp = a0 + a1
#     count = 3
#     while count < n:
#         a0 = a1
#         a1 = temp
#         temp = a0 +a1
#         count += 1
#     return temp
# print(fib_while(int(input('Введите число: '))))

'''Задача №33.
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
Input: 5 -> 4 8 9 1 2
Output: 4 8 1 1 2
'''

# num = [4, 8, 9, 1, 2]
# maxx = max(num)
# minn = min(num)
#
# for i in range(0, len(num)):
#     if num[i] == maxx:
#         num[i] = minn
#
# print(num)

'''
Задача №35.
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n (само число)
Input: 5
Output: yes
'''

# num = int(input('Введите число: '))
# for div in range(2, num // 2 + 1):
#     if num % div == 0:
#         print('NO')
#         break
# else:
#     print('YES')


'''
Задача №37.
Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять списки и использовать циклы (даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
'''
# def change(n):
#     if n == 0:
#         return ''
#     num = int(input('Введите число: '))
#     return change(n - 1) + f' {num}'
#
# n = int(input('Введите кол-во элементов: '))
# print(change(n))