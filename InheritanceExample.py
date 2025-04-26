#1.  Car class with static attributes
'''
class Car:
    brand = "Honda"
    model = "Honda Civic"
    def start_engine(self):
        print("Car starts...")

    def stop_engine(self):
        print("Car stops...")

car1 = Car()
print(car1.model)
print(car1.brand)
car1.start_engine()
car1.stop_engine()


#2. Car class with dynamic attributes
class Car:
    #Parameterized constructior
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand


    def start_engine(self):
        print("Car starts...")

    def stop_engine(self):
        print("Car stops...")

hondaCivic = Car("Honda Civic","Honda")
print(hondaCivic.model)
print(hondaCivic.brand)
hondaCivic.start_engine()
hondaCivic.stop_engine()


tesla = Car("ModelS","Tesla")
print(tesla.model)
print(tesla.brand)
tesla.start_engine()
tesla.stop_engine()


#3. Car class without Inheritance feature
class Vehicle:
    #Parameterized constructior
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand


    def start_engine(self):
        print("Car starts...")

    def stop_engine(self):
        print("Car stops...")

class Car:
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand


    def start_engine(self):
        print("Car starts...")

    def stop_engine(self):
        print("Car stops...")

    def honk(self):
        print("Car honks")

tesla = Car("ModelS","Tesla")
print(tesla.model)
print(tesla.brand)
tesla.start_engine()
tesla.stop_engine()
tesla.honk()
'''

#4. Car class with Inheritance feature
class Vehicle:
    #Parameterized constructior
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand


    def start_engine(self):
        print("Car starts...")

    def stop_engine(self):
        print("Car stops...")

class Car(Vehicle):
    def __init__(self,model,brand,fuel_type):
        super().__init__(model,brand)
        self.fuel_type = fuel_type


    def honk(self):
        print("Car honks")

honda = Car("Honda Civic","Honda","Petrol")
print(honda.model)
print(honda.brand)
print(honda.fuel_type)
honda.start_engine()
honda.stop_engine()
honda.honk()