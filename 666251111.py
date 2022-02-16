
import time

class TrafficLight:
    colors = ('red','yellow','green')
    delay = (7,2,5)

    def __init__(self):
        self.__color = 'green'

    def running(self):
        while True:
            for i in self.colors:
                self.__color = i
                print(self.__color)
                time.sleep(self.delay[self.colors.index(self.__color)])



traffic_lifht = TrafficLight()
traffic_lifht.running()


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, a, b):
        return self._length * self.width * a * b

r = Road(700,2)
print(r.weight(7,6))


class Worker:
    def __init__(self,name, surname, position,wage, prem):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage':wage,'Premia': prem}

class Position(Worker):
    def get_full_name(self):
        return '{0} {1}'.format(self.name,self.surname)

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


employee = Position('Alex','Brown','Dev',40000,5000)
print((employee.name))
print((employee.surnamename))
print((employee._income))
print((employee.get_full_name()))
print((employee.get_total_income()))

class Car:
    def __init__(self,v,col,name,police = False):
        self.v = v
        self.col = col
        self.name = name
        self.police = police

    def go(self):
        print('Go')

    def stop(self)
        print('stop')

    def turn(self,direction)
        print(f'Car turjned to {direction}')

    def show_speed(self):
        print(f'Speed is {v}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60
            print('speed limit is over')

class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('speed limit is over')
class PoliceCar(Car):
    def __init__(self,speed,col,name):
        super().__init__(speed,col,name,True)

town = TownCar(90,'red','town')
sport = SportCar(120,'green','sport')
work = WorkCar(50,'yellow','work')
police = PoliceCar(300,'blue','police')

town.show_speed()
work.show_speed()
work.speed = 30
work.show_speed()

police.turn('left')
