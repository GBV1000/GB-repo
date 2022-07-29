#2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
#Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.



class Textil:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_palto(self):
        return round(self.width / 6.5 + 0.5, 2)

    def get_square_kostum(self):
        return round(self.height * 2 + 0.3, 2)

    @property
    def get_sq_full(self):
        return str(f'Общая площадь полотна ткани \n'
                   f' {round(self.width / 6.5 + 0.5, 2) + round(self.height * 2 + 0.3, 2)}')


class Palto(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5, 2)

    def __str__(self):
        return f'Площадь полотна для пальто {round(self.square_c, 2)}'

class Kostum(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3, 2)

    def __str__(self):
        return f'Площадь полотна для костюма {round(self.square_j, 2)}'

palto = Palto(2, 4)
kostum = Kostum(1, 2)
print(palto)
print(kostum)
print(palto.get_sq_full)
print(kostum.get_sq_full)
print(kostum.get_square_palto())
print(kostum.get_square_kostum())
