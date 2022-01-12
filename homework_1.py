# 1 Задание

# a = 1
# b = 'Hi'
# print(a, b)
# x, y = int(input('Введите первое число: ')), int(input('Введите второе число: '))
# print(f'Первое число {x}, второе число {y}')
# s1, s2 = input('Введите первую строку: '), input('Введите вторую строку: ')
# print(f'Первая строка "{s1}", вторая строка "{s2}"')

# 2 Задание

# time = int(input('Введите количество секунд: '))
# temp_minutes = time // 60 # промежуточная переменная включающая число часов+минут в минутах
#
# seconds = time % 60
# if seconds < 10:# для отображения в формате CC, можно создать и функцию для избежания дублирования, но мы не проходили:)
#     seconds = '0' + str(seconds)
# hours = temp_minutes // 60
# if hours < 10:
#     hours = '0' + str(hours)
# minutes = temp_minutes % 60
# if minutes < 10:
#     minutes = '0' + str(minutes)
#
# print(f'Время в формате чч:мм:сс - {hours}:{minutes}:{seconds}')

# 3 Задание

# n = int(input('Введите число n: '))
# print('Сумма n + nn + nnn равна', n + (n + n * 10) + (n + n * 10 + n * 100))

# 4 Задание

# n = int(input('Введите целое положительное число: '))
# max_digit = 0
# while n > 0:
#     last_digit = n % 10
#     n = n // 10
#     if last_digit >= max_digit:
#         max_digit = last_digit
#
# print('Максимальная цифра числа равна: ', max_digit)

# 5 Задание

# proceeds = int(input('Введите значение выручки: '))
# costs = int(input('Введите значение издержек: '))
# profit = proceeds - costs
# if proceeds <= costs:
#     print('Нет прибыли, баланс: ', profit)
# else:
#     print('Прибыль составила: ', profit)
#     number = int(input('Введите количество сотрудников: '))
#     print('Прибыль фирмы в расчете на 1 сотрудника: {0:.3f}'.format(profit / number))

# 6 Задание

# a = int(input('Количество километров в первый день: '))
# b = int(input('Желаемый результат в км: '))
# i = 1 # счетчик дней
# print('{0}-й день: {1}'.format(i, a))
# while a < b:
#     a += a * 0.1
#     i += 1
#     print('{0}-й день: {1:.2f}'.format(i, a))
#
# print(f'На {i}-й день спортсмен достиг результата - не менее {b} км.')