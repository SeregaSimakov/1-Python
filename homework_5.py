# 1
# file = open('file1.txt', 'w', encoding='utf-8')
#
# user_string = ' ' # непустая строка для запуска работы цикла ввода ниже.
# n = 1 # счетчик номера строки
# while user_string: # создаем цикл ввода и записи в файл построчно, когда будет введена пустая строка, цикл прервется
#     user_string = input(f'Введите {n}-ю строку: ')
#     n += 1
#     file.writelines([user_string, '\n'])
#
# file.close()

# 2
# file = open('file2.txt', encoding='utf-8')
# my_list = file.readlines() #список из строк по методу readlines
#
# for n, elem_string in enumerate(my_list): #нумеруем и перебираем каждую строку, делим на слова по пробелу
#     words_in_string = elem_string.split()
#     #выводим номер строки, количество слов, и саму строку целиком в скобках(отрезав справа символы переносов и пробелов)
#     print(f'Количество слов в {n+1}-й строке равно {len(words_in_string)} ({elem_string.rstrip()})')
# print(f'\nКоличество строк равно: {len(my_list)}') #выводим количество строк
# file.close()

# 3
# with open('file3.txt', encoding='utf-8') as file:
#     s = 0 # сумма дохода всех сотрудников
#     n = 0 # количество сотрудников
#     for line in file.readlines(): # пробегаем циклом построчно
#         # обрезаем перенос справа строки и делим по пробелу на фамилию и доход
#         surname, salary = line.rstrip('\n').split(' ')
#         fl_salary = float(salary) # переводим строку с доходом в число
#         if fl_salary < 20000: # печатаем всех, чей доход меньше 20000
#             print(surname, format(fl_salary, ".2f")) # два знака после запятой для дохода
#         s += fl_salary # прибавляем доход сотрудника к общему доходу
#         n += 1 # увеличиваем счетчик сотрудников на 1
#
#     print('\nСредний размер дохода: ', round(s / n, 2)) # вычисляем средний доход

# 4
# with open('file4.txt', encoding='utf-8') as file_r, open ('file4_1.txt', 'w', encoding='utf-8') as file_w:
#     # создаем словарь где ключ  - число на английском, значение - число на русском
#     my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
#     for line in file_r.readlines():  # пробегаем циклом построчно
#         number, other = line.rstrip('\n').split(' — ') # делим строку на 2 части по ' — ' и отрезаем перенос
#         if number in my_dict:
#             # если название числа соответсвует ключу в словаре, то названию числа присваиваем значение от этого ключа
#             number = my_dict[number]
#         file_w.write(f'{number} — {other}\n') # записываем построчно в другой файл

# 5
# file = open('file5.txt', 'w+', encoding='utf-8') #открываем файл с w+ для записи и чтения
# string_input = input('Введите набор чисел через пробел: ') # вводим строку с числами через пробел
# file.write(string_input) # записываес строку в файл
# file.seek(0) # устанавливаем курсор на начало для прочтения файла
# string_output = file.read() # считываем из файла в строку
# my_list = string_output.split() # сплитим строку в список
# # выводим сумму сгенерированного списка где приведены к числу все элементы предыдущего списка
# print('Сумма чисел равна: ', sum([int(c) for c in my_list]))
# file.close()

# 6
# with open('file6.txt', encoding='utf-8') as file:
#     my_dict = {} #целевой словарь
#     for line in file: # перебираем файл по строкам
#         my_list = line.split(':') # делим на список по ':' первый элемент название предмета, второй - все остальное
#         num_list = [] # список, куда будем включать только числа из второй части строки
#         num = '' # задаем пусто число в строковом выражении
#         for char in my_list[1]: # перебирем все символы в оставшейся части строки (отделенной от названия предмета)
#             if char.isdigit(): # если символ - цифра , добавляем его к числу в строковом выражении
#                 num += char
#             else:
#                 if num != '': # если число есть,то добавляем в список и приводим со строкового в числовое значение
#                     num_list.append(int(num))
#                     num = '' # сбрасываем число на пустое значение (для дальнейшего создания новых чисел)
#
#         my_dict[my_list[0]] = sum(num_list) # добавляем в словарь по ключу(предмет), значение(сумма полученных чисел)
#
# print(my_dict)

# 7
# import json
#
# with open('file7.txt', encoding='utf-8') as file:
#     list_all = [] # итоговый список
#     dict_profit ={} # словарь с прибылями(убытками)
#     n = 0 # количество фирм с прибылью
#     sum_profit = 0 # общая сумма прибыли
#     profit = 0 # прибыль(убыток) одной компании
#     for line in file: # перебираем файл по строкам
#         firm_list = line.split() # делаем список , делим строку по пробелам
#         profit = int(firm_list[2]) - int(firm_list[3]) # вычисляем прибыль(убыток)
#         if int(firm_list[2]) > int(firm_list[3]):
#             # если прибыль есть, суммируем в общую прибыль и увеличиваем счетчик компаний с прибылью
#             sum_profit += profit
#             n += 1
#         dict_profit[firm_list[0]] = profit # добавляем в словарь ключ - название фирмы, и значение - прибыль/убыток
#
#     list_all.append(dict_profit) # добавляем в итоговый список словарь
#
#     average_profit = round(sum_profit / n) # высчитываем среднюю прибыль
#     list_all.append({'average_profit': average_profit}) # добавялем среднюю прибыль в итоговый список
#
#     print(list_all)
#
# with open('file7.json', 'w', encoding='utf-8') as f: # итоговый лист переводим в json и записываем в сответствующий файл
#     json.dump(list_all, f)

