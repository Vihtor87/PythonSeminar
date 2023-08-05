# Вводим список из строки, содержащей цифры. Нужно преобразовать строковые значения в числовые.

# Обычный способ:

# list1 = ['1', '2', '3']
#
# for i in range(len(list1)):
#     list1[i] = int(list1[i])
#
# print(list1)
#
# # Функция map
#
# list2 = ['1', '2', '3']
# new_list2 = list(map(int, list2))
# print(list2)

################################################################################

# list1 = [1, 2, 3]
# new_list1 = list(map(lambda x: x ** 3, list1))
#
# print(list1)

# list1 = [1, 2, 3, 4]
# new_list1 = list(filter(lambda x: x % 2 == 0, list1))
# print(new_list1)

'''
Задача №47.
У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
'''

# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transormed_values = list(map(transformation, values))
# print(values)

'''
Задача №49. 
Планеты вращаются вокруг звезд по эллиптическим орбитам. 
Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь.
Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит 
планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у 
вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты.
Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты.
Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса.
При решении задачи используйте списочные выражения.
Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса,
а затем найти и сам эллипс, имеющий такую площадь.
Гарантируется, что самая далекая планета ровно одна!

Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
Вывод:
2.5 10

'''
# def find_farthest_orbit(val):
#     S_max = 0
#     temp = 0
#     for el in val:
#         for i in range(len(el)):
#             if el[0] != el[1]:
#                 S = el[0] * el[1]
#                 if S_max < S:
#                     S_max = S
#                     temp = el
#     return temp


# def find_farthest_orbit(orbits):
#     s_list = [i[0] * i[1] for i in orbits if i[0] != i[1]]
#     max_s = s_list.index(max(s_list))
#     return orbits[max_s]
#
#     maxx = orbits[0]
#     for el in orbits:
#         if el[0] != el[1] and el[0] * el[1] > maxx[0] * maxx[1]:
#             maxx = el
#     return maxx


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

'''
Задача №51.
Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его
характеристику.

Ввод:
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
print("same")
else:
print("different")

Вывод: same
'''
def same_by(characteristic, objects):
    new_objects = list(filter(characteristic, objects))
    if len(new_objects) == len(objects) or len(new_objects) == 0:
        return True
    else:
        return False


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")