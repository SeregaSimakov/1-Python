# 1
# from itertools import cycle
# from time import sleep
#
# class TrafficLight:
#     colors = ('red', 'yellow', 'green')
#     time_color = (7, 2, 5)
#
#     def __init__(self, color):
#         self.__color = color
#
#     def running(self):
#         my_cycle = cycle(self.colors) # перебираем все цвета циклично
#         for i in my_cycle:
#              if self.__color == i: # ключевое условие для выравнивания цикличности с того цвета, который задали при создании объекта
#                 print('light', self.colors[self.colors.index(self.__color)])
#                 sleep(self.time_color[self.colors.index(self.__color)])
#                 self.__color = next(my_cycle)
#
# tl1 = TrafficLight('green') # стартуем с нужного цвета сохраненного в приватную переменную self.__color
# tl1.running()

# 2
# class Road:

#     def __init__(self, length, width):
#         self._length = length
#         self._width = width

#     def payment(self, weight, thickness):
#         summa = self._length * self._width * weight * thickness
#         print(f'Для дороги потребуется {round(summa/1000)} т асфальта')

# road1 = Road(20, 5000)
# road1.payment(25, 5)

# 3
# class Worker:

#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}

# class Position:

#     def __init__(self, *args):
#         Worker.__init__(self, *args)

#     def get_full_name(self):
#         return f'{self.name} {self.surname}'

#     def get_total_income(self):
#         return self._income['wage'] + self._income['bonus']

# person_1 = Position('Vasiliy', 'Petrov', 'director', 50000, 70000)
# print(person_1.position)
# print('Full name is', person_1.get_full_name())
# print(f'Salary {person_1.get_full_name()} is {person_1.get_total_income()}')

# 4
# class Car:

#     def __init__(self, *args):
#         self.speed = args[0]
#         self.color = args[1]
#         self.name = args[2]
#         self.is_police = args[3]

#     def go(self):
#         print(f"{self.name} goes")

#     def stop(self):
#         print(f"{self.name} stops")

#     def turn(self, direction):
#         print(f"{self.name} turns on the {direction}")

#     def show_speed(self):
#         print(f'Current speed of {self.name} is {self.speed}')

# class SportCar(Car):
#     def __init__(self, *args):
#         Car.__init__(self, *args)

# class PoliceCar(Car):
#     def __init__(self, *args):
#         Car.__init__(self, *args)
#         if self.is_police != True:
#             print(f'{self.name} is not police auto')

# class TownCar(Car):
#     def __init__(self, *args):
#         Car.__init__(self, *args)

#     def show_speed(self):
#         Car.show_speed(self)
#         if self.speed > 60:
#             print('Speed exceeded')

# class WorkCar(Car):
#     def __init__(self, *args):
#         Car.__init__(self, *args)

#     def show_speed(self):
#         Car.show_speed(self)
#         if self.speed > 40:
#             print('Speed exceeded')

# sport_car1 = SportCar(110, 'black', 'BMW', False)
# sport_car1.go()
# sport_car1.turn('right')
# sport_car1.show_speed()

# work_car1 = WorkCar(41, 'red', 'Mazda', False)
# work_car1.show_speed()

# town_car1 = TownCar(60, 'blue', 'Nissan', False)
# town_car1.show_speed()

# police_car1 = PoliceCar(60,'black-white', 'Ford', False)
# police_car1.turn('right')
# police_car1.stop()

# # 5
# class Stationery:
#     def __init__(self, *args):
#         self.title = args[0]

#     def draw(self):
#         print('Start rendering')

# class Pen(Stationery):
#     def __init__(self, *args):
#         Stationery.__init__(self, *args)

#     def draw(self):
#         Stationery.draw(self)
#         print(f'{self.title} start rendering with pen')

# class Pencil(Stationery):
#     def __init__(self, *args):
#         Stationery.__init__(self, *args)

#     def draw(self):
#         Stationery.draw(self)
#         print(f'{self.title} start rendering with pencil')

# class Handle(Stationery):
#     def __init__(self, *args):
#         Stationery.__init__(self, *args)

#     def draw(self):
#         Stationery.draw(self)
#         print(f'{self.title} start rendering with handle')

# picture1 = Pen('Cool name')
# picture1.draw()

# picture2 = Pencil('Fine name')
# picture2.draw()

# picture3 = Handle('Wonderful name')
# picture3.draw()