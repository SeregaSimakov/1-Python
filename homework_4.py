# 1

# from sys import argv
#
# def salary(hours, rate_per_hour, premium):
#     return (hours * rate_per_hour) + premium
# try:
#     print('Заработная плата составляет: ', salary(int(argv[1]), int(argv[2]), int(argv[3])))
# except Exception:
#     print('Введите корректные данные (3 целых числа через пробел)')

# 2

# from random import randint
#
# my_list = [randint(0, 1000) for i in range(10)] # генератор списка из 10 случайных элементов от 0 до 999
# new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]] # генерим целевой список
#
# print(my_list)
# print(new_list)

# 3

# print(*[i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]) # обязательно до 241, чтобы 240 включилось

# 4

# from random import randint
#
# my_list = [randint(0, 10) for i in range(10)] # генератор списка из 10 случайных элементов от 0 до 9
# print(my_list)
# # генерим список из элементов начального списка счетчик count которых равен 1, т. е. число в списке встречается 1 раз
# print([x for x in my_list if my_list.count(x) == 1])

# 5

# from functools import reduce
#
# my_list = [i for i in range(100, 1001) if i % 2 == 0] # генерим список из четных чисел от 100 до 1000
# print(my_list)
#
# def my_func(prev_el, el):
#     return prev_el * el
#
# print(reduce(my_func, my_list))

# 6.1

# from itertools import count
#
# def count_func(a, b): # функция которая итерирует с и до указанных значений
#     for el in count(a):
#         if el > b:
#             break
#         else:
#             print(el)
#
# count_func(3, 10) # указываем значения 3 и 10 как в задании


# 6.2

# from itertools import cycle
#
# my_list = [1, 'abc', None, True, False, 456, 'QWE'] # произвольный список
#
# def cycle_func(a): # создаем функцию циклического вывода с 1 параметром, ограничивающим число итераций
#     с = 0
#     for el in cycle(my_list):
#         if с > a:
#             break
#         print(el)
#         с += 1
#
# cycle_func(20) # вызываем функцию и указываем нужное количество итераций

# 7

# def fact(n): #функция факториала
#     s = 1
#     for i in range (1, n + 1):
#         s *= i
#         yield s
#
# n = 6 # выбираем число, факториал которого будет последнем элементом(1....n)
# for el in fact(n):# формируем цикл для следующей итерации функции fact и вывода на экран
#     print(el)
