from abc import ABC, abstractmethod
from typing import override

class Chargeable(ABC):
    @abstractmethod
    def charge(self):
        pass

class Drivable(ABC):
    @abstractmethod
    def drive(self):
        pass

class Vehicle(ABC):
    def __init__(self, model: str):
        self.model = model

    def __str__(self):
        return f"Vehicle: {self.model}"
    
    @abstractmethod
    def move(self):
        pass

class ElectricCar(Vehicle, Chargeable, Drivable):
    def __init__(self, model: str, battery_level: int):
        super().__init__(model)
        self.battery_level = battery_level

    def __str__(self):
        return f"ElectricCar: {self.model}, Battery: {self.battery_level}"
    
    @override
    def move(self):
        print(f"{self.model} is moving silently")
    
    def charge(self):
        print(f"{self.model} is charging")
    
    def drive(self):
        print(f"{self.model} is driving")

class ElectricScooter(Vehicle, Chargeable):
    def __init__(self, model: str, max_speed: int):
        super().__init__(model)
        self.max_speed = max_speed
    
    def __str__(self):
        return f"ElectricScooter: model({self.model}), max_speed({self.max_speed})"
    
    @override
    def move(self):
        print(f"{self.model} is moving")
    
    def charge(self):
        print(f"{self.model} is charging")


if __name__ == "__main__":
    print("--- Testing ElectricCar ---")
    # 1. Create an ElectricCar
    my_car = ElectricCar("Tesla Model S", 85)
    print(my_car)
    
    # 2. Test behaviors
    my_car.move()    # From Vehicle
    my_car.drive()   # From Drivable
    my_car.charge()  # From Chargeable

    print("\n--- Testing ElectricScooter ---")
    # 3. Create an ElectricScooter
    my_scooter = ElectricScooter("Ninebot G30", 30)
    print(my_scooter)
    
    # 4. Test behaviors
    my_scooter.move()    # From Vehicle
    my_scooter.charge()  # From Chargeable
    
    # Note: my_scooter.drive() would raise an AttributeError 
    # because Scooter does not implement Drivable!
