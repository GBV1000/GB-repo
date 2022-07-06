"""
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:

    __in_data = {
        'wage': 77000,
        'bonus': 33
                }

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self.in_data = self.__in_data


class Position(Worker):

    def get_full_name(self):
        print(f'Cотрудник ООО "Рога и Копыта": {self.name} {self.surname}\n')

    def get_total_income(self):
        zp = self.in_data['wage']
        bonus = (self.in_data['wage']*25)//100
        print(f"Зарплата за месяц составляет {zp}руб. + премия {bonus}руб. Итого к выплате {zp + bonus}руб")


user = Position('Иванов', 'Шульгин', 'Директор по развитию')
user.get_full_name()
print(f'{user.name} {user.surname}. Должность в организации - {user.position}')
user.get_total_income()
