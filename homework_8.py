# 1

# import time
# class Data:
#
#     def __init__(self, date):
#         self.my_class_method(date)
#
#     @classmethod # вычисляем целые значения дня, месяца, года из строковой даты
#     def my_class_method(cls, string_date):
#         list_date = string_date.split('-')
#         list_int = [int(el) for el in list_date]
#         return list_int[0], list_int[1], list_int[2]
#
#     @staticmethod
#     def validation(date): # для проверки валидности даты лучше использовать time.strptime
#         try:
#             time.strptime(date, '%d-%m-%Y')
#             print('Valid Date')
#             return True
#         except ValueError:
#             print('Invalid Date')
#
# date_user = input('Input date dd-mm-YY: ')
#
# if Data.validation(date_user): #при условии что валидация возвращает True создаем объект с этой датой
#     obj = Data(date_user)
#     d, m, y = Data.my_class_method(date_user)
#     print(f'Day {d}, month {m}, year {y}')

#2

# class ZeroDiv(Exception):
#
#     def __init__(self, txt):
#         self.txt = txt
#
# try:
#     x, y = float(input('Введите делимое X: ')), float(input('Введите делитель Y: '))
#     if y == 0:
#         raise ZeroDiv('Вы делите на 0')
# except ValueError:
#     print('Вы ввели неверные значения')
# except ZeroDiv as zd:
#     print(zd)
# else:
#     print(f'Полученное значение X/Y = {round(x/y, 2)}')

#3

# class NoNumber(Exception):
#
#     def __str__(self):
#         return 'ввели не число'
#
# n = ''
# result = []
#
# while n != 'stop': # пока не введем stop ввод повторяется
#     try:
#         n = input('Введите целое число: ')
#         num = n # доп переменная, int от которой добавим список
#         if n[0] == '-': # если первый символ '-' переприсваиваем введеное число без него, и приплюсовываем '-' к доп переменной
#             n = n[1:]
#             num = '-' + n
#         if n.isdigit() == False: # проверка введеного числа на цифры и вызов нашего класса-исключения в противном случае
#             raise NoNumber()
#     except NoNumber as nn:  #отрабатываем наш класс-исключение и выводим на экран заданный текст
#         print(nn)
#     else: #добавляем в список int от доп переменной, что ввели (вместе с '-' если есть), в случае когда не было исключений
#         result.append(int(num))
#
# print(f'Итоговый список: {result}')

# 4, 5, 6

# class Warehouse:
#
#     def __init__(self):
#         self.id_base = [] # cписок номенклатуры
#         self.obj_base = [] # список обьектов
#
#     def validate_result(func): # функция-ДЕКОРАТОР строится именно так
#         # Если при вызове  функции func в программе произойдет ошибка,
#         # то эта функция-декоратор перехватит ее и напишет сообщение
#         def inner_func(*args):
#             try:
#                 func(*args)
#             except Exception:
#                 print('неверные входные данные')
#         return inner_func
#
#     def add_id_base(self, *args): # функция добавляения позиуии в номенклатуру
#         self.id_base.append({args[0]: [*args[1:]]})
#
#     def get_var_names(self):    # функция получения имени экземпляра класса (ЧЕСТНО ЕЕ ЗАГУГЛИЛ)
#         return [k for k, v in globals().items() if v is self]
#
#     def __str__(self): # строковое представление имени подразделения, используя функцию выше
#         return f'{self.get_var_names()}'
#
#     def get_show(self, list1): # функция отображения количества товаров в данном подразделении
#         print(f'Список объектов подразделения {self}: ')
#
#         dict_count = {} # словарь для отображения
#
#         for el in list1: # пробегаемся по элементам входного списка
#
#             if str(el) not in dict_count:
#                 ''' если строковое отображение элемента(объекта) нет в словаре, добавляем его,
#                 в значении пишем список который отображает количество штук, в данном случае 1 '''
#                 dict_count[str(el)] = [1, 'шт.']
#             else: # в противном случае, количество штук увеличиваем на 1
#                 dict_count[str(el)][0] += 1
#
#         for el, zn in dict_count.items(): # пробегаемся по итоговому словарю и выводим, построчно пару ключ-значение
#             print(el, *zn)
#
#         print()
#
#     @validate_result
#     def copy_id_base(self, name_subdivision): # функция копирования справочника для нового подразделения
#         self.id_base = name_subdivision.id_base[:]
#
#     @validate_result # навешиваем валидацию на функцию добавления объекта
#     def add_obj_base(self, art, num): # наша функция, которая добавляет объект/объекты в список по артикулу и количеству
#
#         flag = False # флаг для вывода сообщения 'нет такой позиции'
#         for j in range(num): # цикл по количеству товара
#             for i, el in enumerate(self.id_base): # цикл по каждому словарю из справочника номенклатуры
#                 if art in el.keys(): # если введеный артикул равен ключу проверяемого словаря, то создаем объект
#                     #  создаем объект по данным из номенклатуры
#                     obj = wh.id_base[i][art][0](wh.id_base[i][art][3], wh.id_base[i][art][1], wh.id_base[i][art][2], i)
#                     self.obj_base.append(obj) # добавляем к общему списку объектов
#                     flag = True # меняем флаг на True чтобы не отпринтовывать сообщение ниже
#         if not flag:
#             print(f'{art} - нет такой позици в номенклатуре')
#
#     @validate_result # также навешиваем валидацию на функцию удаления объекта
#     def sub_obj_base(self, art, num, subdivision):
#         if isinstance(subdivision, Warehouse):
#             n = 0
#             for i, el in enumerate(self.obj_base):
#                 if art == el.art:
#                     n += 1
#
#             if n >= num:
#                 for j in range(num):
#                     for i, el in enumerate(self.obj_base):
#                         if art == el.art:
#                             subdivision.add_obj_base(art, 1) # перелаем данный товар в базу объектов указанного подразделения
#                             self.obj_base.remove(el) # списываем со склада подразделения данный объект
#                 print(f'Товара арт.[{art}] отправлен в {subdivision} в размере {num} шт. Осталось {n-num} шт.\n')
#
#             elif n:
#                 print(f'Товара арт.[{art}] не хватает для отправки в размере {num} шт. На складе есть {n} шт.\n')
#
#             else:
#                 print('Такого товара  нет в наличии\n')
#         else:
#             print('Нет такого подразделения\n')
#
# class OfficeEquipment:
#
#     def __init__(self, name, cost, art):
#         self.name = name
#         self.cost = cost
#         self.art = art
#
#
# class Xerox(OfficeEquipment): # Класс ксероксов
#
#     def __init__(self, type, *args):
#         OfficeEquipment.__init__(self, *args)
#         self.type = type
#
#     def __str__(self):
#         return f'Aрт.[{self.art}] Xerox - Фирма: {self.name}. Цена: {self.cost}. Тип печати: {self.type}.'
#
#
# class Printer(OfficeEquipment): # Класс принтеров
#
#     def __init__(self, speed_print, *args):
#         OfficeEquipment.__init__(self, *args)
#         self.speed_print = speed_print
#
#     def __str__(self):
#         return f'Aрт.[{self.art}] Printer - Фирма: {self.name}. Цена: {self.cost}. Скорость печати: {self.speed_print}.'
#
# class Scaner(OfficeEquipment): # Класс сканеров
#
#     def __init__(self, formatA, *args):
#         OfficeEquipment.__init__(self, *args)
#         self.formatA = formatA
#
#     def __str__(self):
#         return f'Aрт.[{self.art}] Scaner - Фирма: {self.name}. Цена: {self.cost}. Формат: {self.formatA}.'
#
# wh = Warehouse() # строим наш склад с название wh
# # Как в любой нормальной базе данных предприятия, сначала заводятся позиции в базе с персональным кодом(артикулом)
# # а уже затем, по этой позиции добавляется/убавляется количество товара на складе
# wh.add_id_base(0, Xerox, 'Samsung', 5000, 'laser')
# wh.add_id_base(1, Xerox, 'HP', 4000, 'jet')
# wh.add_id_base(2, Printer, 'HP', 4500, 50)
# wh.add_id_base(3, Scaner, 'Epson', 3000, 'A4')
# wh.add_id_base(4, Scaner, 'Canon', 7500, 'A3')
#
# sm = Warehouse() # строим наш магазин
# sm.copy_id_base(wh) # копираем справочник номенклатуры склада, чтобы не вводить 2 раза
#
# # Наполняем склад товарами из справочника номенклатуры
# wh.add_obj_base(1, 2)
# wh.add_obj_base(3, 2)
#
# # выводим список товаров с количеством
# wh.get_show(wh.obj_base)
#
# # отправляем объекты со склада в магазин
# wh.sub_obj_base(1, 1, sm)
#
# # выводим список товаров в с количеством в обоих подразделениях
# wh.get_show(wh.obj_base)
# sm.get_show(sm.obj_base)
#
# # отправляем обратно с магазина на склад
# sm.sub_obj_base(1, 1, wh)
#
# # выводим список товаров в с количеством в обоих подразделениях
# wh.get_show(wh.obj_base)
# sm.get_show(sm.obj_base)
#
# ''' Теперь можно создавать сколько угодно подразделений, сколько угодно позиций товара в базе,
# и сколько угодно объектов в каждом подразделении используя созданные методы, и также бесконечно передавать товары
# между подразделениями, и выводя текущий остаток товаров в каждом '''

# 7
 # если конечно не использовать встроенный класс complex
class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.complex_num = f'{a}+{b}j'

    def __str__(self):
        return self.complex_num

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return f'{self.a + other.a}+{self.b + other.b}j'

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return f'{self.a*other.a - self.b*other.b}+{self.b*other.a + self.a*other.b}j'

x = ComplexNumber(3, 5)
y = ComplexNumber(2, 7)

print(x + y)
print(x * y)