from typing import override

class Vehicle:
    def __init__(self, name: str, base_fee: float):
        self.name = name
        self.base_fee = base_fee
    
    def trip_cost(self, distance_km):
        return self.base_fee

    def __str__(self) -> str:
        return f"{self.name}, base_fee: {self.base_fee}"

class GasCar(Vehicle):
    def __init__(self, base_fee: float, liters_per_100km: float, price_per_liter: float):
        super().__init__("GasCar", base_fee)
        self.liters_per_100km = liters_per_100km
        self.price_per_liter = price_per_liter
    
    @override
    def trip_cost(self, distance_km: float) -> float:
        fuel_used = (distance_km / 100) * self.liters_per_100km
        return self.base_fee + fuel_used * self.price_per_liter
    
    @override
    def __str__(self) -> str:
        return f"{super().__str__()}, liters_per_100km: {self.liters_per_100km}, price_per_liter: {self.price_per_liter}, sample_distance(50km): {self.trip_cost(50):.2f}"

class ElectricCar(Vehicle):
    def __init__(self, base_fee: float, kwh_per_100km: float, price_per_kwh: float):
        super().__init__("ElectricCar", base_fee)
        self.kwh_per_100km = kwh_per_100km
        self.price_per_kwh = price_per_kwh
    
    @override
    def trip_cost(self, distance_km: float):
        energy_used = (distance_km / 100) * self.kwh_per_100km
        return self.base_fee + energy_used * self.price_per_kwh
    
    @override
    def __str__(self):
        return f"{super().__str__()}, kwh_per_100km: {self.kwh_per_100km}, price_per_kwh: {self.price_per_kwh}, sample_distance(50km): {self.trip_cost(50):.2f}"

class Taxi(Vehicle):
    def __init__(self, base_fee: float, price_per_km: float, is_night: bool):
        super().__init__("Taxi", base_fee)
        self.price_per_km = price_per_km
        self.is_night = is_night
    
    @override
    def trip_cost(self, distance_km: float):
        cost = self.base_fee + distance_km * self.price_per_km
        return cost * 1.2 if self.is_night else cost
    
    @override
    def __str__(self):
        return f"{super().__str__()}, price_per_km: {self.price_per_km}, is_night: {self.is_night}, sample_distance(50km): {self.trip_cost(50):.2f}"
        
if __name__ == "__main__":
    car1 = GasCar(10, 8, 1.5)
    car2 = ElectricCar(10, 15, 0.5)
    car3 = Taxi(10, 1.5, True)
    car4 = Taxi(10, 1.5, False)
    
    vehicles = [car1, car2, car3, car4]
    for vehicle in vehicles:
        print(vehicle)
    
    print("\n--- 120km Trip Costs ---")
    for vehicle in vehicles:
        print(f"{vehicle.name}: {vehicle.trip_cost(120):.2f}")