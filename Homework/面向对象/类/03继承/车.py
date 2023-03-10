class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


class Electrocar(Car):
    def __init__(self, brand, speed, capacity, power):
        super().__init__(brand, speed)
        self.capacity = capacity
        self.power = power


c01 = Car("奔驰", 180)
e01 = Electrocar("小牛", 25, 100, 25)

