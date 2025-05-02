class Car:
    def __init__(self,license_number, brand):
        self.license_number = license_number
        self.brand= brand

class ElectricCar(Car):
    def __init__(self, license_number, brand, battery_capacity):
        super().__init__(license_number, brand)
        self.battery_capacity = battery_capacity


e = ElectricCar("ABC123", "Tesla", 100)
print(e.__dict__)

