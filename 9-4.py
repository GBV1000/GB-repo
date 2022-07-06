"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:


    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'{self.name} трогается с места')
    def show_speed(self):
        print(f'{self.name} скорость на спидометре {self.speed} км/ч')
    def turn(self, direction):
        print(f'{self.name} совершила {direction}')
    def stop(self):
        print('Остановка')
    def stop_alarm(self):
        print('Авария')
    def stop_service(self):
        print("Меняет колесо")

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'{self.name} - на спидометре  {self.speed}')
        if 79 > self.speed > 60:
            print(f'Превышение разрешенной скорости на {self.speed - 60} км/ч')
            print('Не наказуемое нарушение до 79 км/ч')
        elif 120 > self.speed > 79:
            print(f'Превышение разрешенной скорости на {self.speed - 60} км/ч')
            print(f'Штраф 500р')
        elif self.speed >= 120:
            print(f'Превышение разрешенной скорости на {self.speed - 60} км/ч')
            print(f'Штраф 5000р')

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'{self.name} на спидометре {self.speed}')
        if 59 >= self.speed > 40:
            print(f'Превышение разрешенной скорости на {self.speed - 40} км/ч')
            print('Не наказуемое нарушение до 59 км/ч')
        elif 79 >= self.speed > 59:
            print(f'Превышение разрешенной скорости на {self.speed - 40} км/ч')
            print(f'Штраф 500р')
        elif self.speed > 79:
            print(f'Превышение разрешенной скорости на {self.speed - 40} км/ч')
            print(f'Штраф 5000р')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


car_town = TownCar(119, 'green', 'Альфа Ромео')
car_town.go()
car_town.show_speed()
car_town.turn('разворот')
car_town.stop()

print('===\n')

car_sport = SportCar(140, 'gold', 'Мустанг')
car_sport.go()
car_sport.show_speed()
car_sport.turn('дрифт')
car_sport.stop_alarm()
car_sport.stop()

print('===\n')

car_work = WorkCar(35, 'blue', 'Потчтовый фургон')
car_work.go()
car_work.show_speed()
car_work.stop()
car_work.stop_service()

print('===\n')

car_police = PoliceCar(150, 'white', 'Лада ДПС')
car_police.go()
car_police.show_speed()
car_police.turn(f'дрифт за {car_sport.name}')
car_police.stop_alarm()
car_police.stop()

