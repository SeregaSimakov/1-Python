# 1

# def division(a, b):
#     try:
#         return round((a / b), 2)
#     except ZeroDivisionError:
#         return 'Деление на ноль'
#
# a,b = int(input('Введите делимое: ')), int(input('Введите частное: '))
# print(division(a, b))

# 2

# def person(name, surname, age, email, year, city, phone):
#     print(f'Меня зовут {name} {surname}, мне {age} лет. Я родился в {year} году. Живу в {city}е.'
#           f' Мои данные: Адрес почты - {email}, телефон - {phone}')
#
# person(name='Sergey', surname='Simakov', age=35, phone=89064326085, city='Краснодар', email='infser2013@gmail.com', year=1986)

# 3

# def my_func(a, b, c):
#     # создаем список из 3-чисел и сортируем, 2 последних элемента будут максимальными, затем их складываем
#     my_list = [a, b, c]
#     my_list.sort()
#     return sum(my_list[-2:])
#
# print(f'Cумма 2-х максимальных чисел равна: {my_func(10, 7, 9)}')

# 4

# def my_func1(x, y): # первая реализация через **
#     return x ** y
#
# def my_func2(x, y):  # вторая реализация через цикл
#     result = 1 # также отработает если введем степень равной 0
#     if y > 0:
#         for i in range(1, y + 1):
#             result *= x
#     elif y < 0:
#         for i in range(1, abs(y) + 1):
#             result *= (1 / x)
#     return result
#
# # проверяем вывод обеих функций
# print(my_func1(2, -3))
# print(my_func2(2, -3))

# 5
# summa = 0
# flag = True
#
# while flag: # цикл выполняется до бесконечности пока переменная True
#     user_string = input('Введите набор чисел через пробел (для выхода введите "~"): ')
#
#     if '~' in user_string: # отработка ввода спецсимвола
#         index_simbol = user_string.index('~') # находим индекс спецсимвола
#         user_string = user_string[:index_simbol] # режем строку до этого символа
#         flag = False # флагу ставим False для дальнейшего завершения цикла
#
#     list_str = user_string.split() # разбиваем строку по пробелу на отдельные значения
#     list_numbers = [int(i) for i in list_str] # переводим в числа элементы
#
#     summa += sum(list_numbers) # добавляем сумму списка к текущей сумме
#     print(summa)
#
# print(f'Итоговая сумма равна: {summa}')

# 6, 7

# # Первый вариант решения, в Python уже есть метод title

# def int_func(my_string):
#     return my_string.title()
#
# text = input('Введите текст: ')
# print(int_func(text))
#

# # Второй вариант без title
# def int_func2(my_string):
#     # создаем функцию, которая превращает строку в список, первый элемент делает заглавным, и обратно в строку
#     my_list = list(my_string)
#     my_list[0] = my_list[0].upper()
#     return ''.join(my_list)
#
# text = input('Введите текст: ')
# list_text = text.split() # разбиваем строку на список слов
# for i, word in enumerate(list_text):
#     # перебираем все слова, меняем первую букву с помощью функции, присваиваем каждому элементу измененное слово
#     word = int_func2(word)
#     list_text[i] = word
# print(' '.join(list_text))