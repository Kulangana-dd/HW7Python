# 4) Реализуйте базовый класс Car. 
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
# А также методы: go, stop, turn(direction), 
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
# Для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. 
# Выполните доступ к атрибутам, выведите результат. 
# Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехал.'

    def stop(self):
        return f'{self.name} остановился.'

    def turn(self, direction):
        return f'{self.name} сделал поворот {direction}.'

    def show_speed(self):
        return f'Скорость {self.speed} км/ч.'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Скорость {self.speed} км/ч - превышены разрешённые 60 км/ч.'
        else:
            return f'Скорость {self.speed}.'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Скорость {self.speed} км/ч - превышены разрешённые 40 км/ч.'
        else:
            return f'Скорость {self.speed}.'


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass

car_1 = TownCar('Ford', 'сафари', 80, False)
car_2 = WorkCar('VAZ', 'опал', 50, False)
car_3 = SportCar('Ferrari', 'коралл', 200, False)
car_4 = PoliceCar('Chevrolet', 'мокрый асфальт', 90, True)

print(f'{car_1.name} - цвет {car_1.color}')
print(f'{car_2.name} - цвет {car_2.color}')
print(f'{car_3.name} - скорость {car_3.speed} км/ч')
print(f'{car_4.name} полицейская машина? - {car_4.is_police}')

print('\n' + car_1.go(), car_1.show_speed(), car_1.stop())

print('\n' + car_2.go(), car_2.show_speed(), car_2.stop())

print('\n' + car_3.go(), car_3.show_speed(), car_3.turn('налево'), car_3.stop())

print('\n' + car_4.go(), car_4.show_speed(), car_4.turn('направо'), car_4.stop())