#7. Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число». 
#Реализовать перегрузку методов сложения и умножения комплексных чисел. Проверить работу проекта.
#Для этого создать экземпляры класса (комплексные числа), выполнить сложение и умножение созданных
#экземпляров. Проверить корректность полученного результата.


import math


class Comp_numbers(object):

    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num
        self.res = complex(first_num, second_num)
        print(f'Комплексное число "{self.res}"')

    def __add__(self, other):
        return f'{self.res} + {other.res}: {complex((self.first_num + other.first_num), (self.second_num + other.second_num))}'
    def __mul__(self, other):
        return f'{self.res} * {other.res}: {complex((self.first_num * other.first_num), (self.second_num * other.second_num))}'

first_num = Comp_numbers(1, 2)
second_num = Comp_numbers(3, 4)
print(first_num + second_num)
print(first_num * second_num)




