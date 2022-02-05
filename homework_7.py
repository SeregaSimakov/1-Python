# 1
# import copy
#
# class Matrix:
#
#     def __init__(self, matrix):
#         self.matrix = matrix
#
#     def __str__(self):
#         main_string = ''
#         for el in self.matrix:
#             main_string += ', '.join(map(str, el)) + '\n'
#         return main_string
#
#     def __add__(self, other):
#
#         new_matrix = copy.deepcopy(self.matrix) # глубокое копирование для создания аналогичной матрицы, с такими же размерами
#         for i in range(len(self.matrix)):
#             for j in range(len(other.matrix[0])):
#                 # замена каждого элемента новой матрицы на сумму соответствующих элементов 2-х матриц
#                 new_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
#             result = new_matrix
#         return Matrix(result)
#
# a = Matrix([[3, 1, 2], [4, 5, 6], [7, 8, 0]])
# b = Matrix([[2, 7, 5], [1, 1, 1], [0, 2, 3]])
#
# print(a)
# print(b)
# print(a + b)
# print(a) # благодаря глубокому копированию не изменилась начальная матрица

# 2
# from abc import ABC, abstractmethod
#
# class Clothes(ABC):
#
#     def __init__(self, param):
#         self.param = param
#
#     @abstractmethod
#     def consumption(self):
#         pass
#
# class Coat(Clothes):
#
#     def __init__(self, param):
#         Clothes.__init__(self, param)
#
#     @property
#     def consumption(self):
#         return round((self.param/6.5 +  + 0.5), 1)
#
# class Costume(Clothes):
#
#     def __init__(self, param):
#         Clothes.__init__(self, param)
#
#     @property
#     def consumption(self):
#         return 2 * self.param + 0.3
#
# coat_1 = Coat(80)
# costume_1 = Costume(60)
#
# print('Общий расход ткани: ', coat_1.consumption + costume_1.consumption)

# 3

# class Cell:
#
#     def __init__(self, n):
#         self.n = n
#
#     def __add__(self, other):
#         if isinstance(other, Cell):
#             return Cell(self.n + other.n)
#
#     def __sub__(self, other):
#         if isinstance(other, Cell):
#             if self.n - other.n > 0:
#                 return Cell(self.n - other.n)
#             else:
#                 return 'incorrect'
#
#     def __mul__(self, other):
#         if isinstance(other, Cell):
#             return Cell(self.n * other.n)
#
#     def __truediv__(self, other):
#         if isinstance(other, Cell):
#             return Cell(self.n // other.n)
#
#     def make_order(self, param):
#         for num, char in enumerate(self.n * '*'):
#             if (num + 1) % param == 0:
#                 char += '\n'
#             print(char, end='')
#
# a1 = Cell(27)
# a2 = Cell(12)
#
# print(a1 - a2)
# a2.make_order(7)