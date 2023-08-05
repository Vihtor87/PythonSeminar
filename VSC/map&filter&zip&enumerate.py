'''
В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число; квадрать числа).

Ввод: 1 2 3 5 8 15 23 38

Вывод: [(2, 4), (8, 64), (38, 1444)]
'''


# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# res = []
#
# for i in list1:
#     if i % 2 == 0:
#         res.append((i, i**2))
#
# print(res)

# То как выглядит функция map под капотом:
# def select(f, val):
#     return [f(x) for x in val]
#
# # То как выглядит функция filter под капотом:
# def where(f, val):
#     return [x for x in val if f(x)]
#
#
# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, list1)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x ** 2), res))
# print(res)


'''
Задача.
С клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел.
Этот набор чисел будет в качестве строки. Превратить list строк в list чисел.
'''
# val = input('Введите ряд чисел через пробел: ')
# val = list(map(int, val.split()))
# print(val)

# list1 = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, list1))
# print(res)

# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# list1 = [x for x in range(1, 21)]
# print(list1)
#
# list1 = list(map(lambda x: x + 10, list1))
# print(list1)


# Сокращение кода с использованием встроенных функций map & filter:

# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, list1)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# Функция zip
# users = ['user1', 'user2', 'user3', 'user4']
# ids = [4, 5, 9, 14, 7]
# res = list(zip(users, ids))
# print(f'Name & age: {res}')

# Функция enumerate
# list1 = ['Kazan', 'Smolensk', 'Fish', 'Chicago']
# res = list(enumerate(list1))
# print(res)