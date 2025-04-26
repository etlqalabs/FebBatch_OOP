from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self,noOfTires):
        self.noOfTires = noOfTires

    def stop_engine(self):
        print("engines stop..")

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def __init__(self):
        super().__init__(4)

    #def start_engine(self):
    #    print("Car starts...")
class ElectricCar(Car):
    def start_engine(self):
        print("Electtic Car starts...")


class Bike(Vehicle):
    def __init__(self):
        super().__init__(2)

    def start_engine(self):
        print("Bike starts...")

'''
# absstract class can't have objects created
veh = Vehicle(2)
print(veh.noOfTires)
veh.start_engine()
veh.stop_engine()
'''

car = ElectricCar()
print(car.noOfTires)
car.start_engine()
car.stop_engine()

bike = Bike()
print(bike.noOfTires)
bike.start_engine()
bike.stop_engine()

