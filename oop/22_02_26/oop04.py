

class SpaceShip:
    MAX_FUEL = 1000
    MIN_FUEL = 0
    launch_count = 0

    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel
        SpaceShip.launch_count += 1
    
    @property
    def fuel(self):
        return self.__fuel
    
    @fuel.setter
    def fuel(self, value):
        if value > self.MAX_FUEL:
            self.__fuel = self.MAX_FUEL
        elif value < self.MIN_FUEL:
            self.__fuel = self.MIN_FUEL
        else:
            self.__fuel = value
    
    @staticmethod
    def is_valid_mission(distance):
        if distance < 50 or distance > 10000:
            return False
        return True
    
    @classmethod
    def from_emergency_mode(cls, name):
        return cls(name, 100)
    
    def launch(self):
        if self.fuel < 100:
            print(f"{self.name} Not enough fuel to launch")
        else:
            self.fuel -= 100
            SpaceShip.launch_count += 1
            print(f"{self.name} has launched!")
    
    def refuel(self, amount):
        self.fuel += amount
    
    def display_status(self):
        print(f"Ship: {self.name} | Fuel: {self.fuel} | Total Launches: {SpaceShip.launch_count}")

if __name__ == "__main__":
    # 1. Create 2 normal ships
    ship1 = SpaceShip("Alpha", 500)
    ship2 = SpaceShip("Bravo", 1000)

    # 2. Create 1 ship using from_emergency_mode
    emergency_ship = SpaceShip.from_emergency_mode("Rescue-1")

    # 3. Try launching them
    print("--- Launching Phase ---")
    ship1.launch()          # Should work
    emergency_ship.launch() # Should work (has 100 fuel)
    emergency_ship.launch() # Should fail (fuel is now 0)

    # 4. Try invalid fuel values (Testing the Setter)
    print("\n--- Testing Fuel Limits ---")
    ship1.fuel = 5000       # Should be capped at 1000
    print(f"Ship1 Fuel (after setting 5000): {ship1.fuel}")
    
    ship2.fuel = -100       # Should be capped at 0
    print(f"Ship2 Fuel (after setting -100): {ship2.fuel}")

    # 5. Test is_valid_mission() with different distances
    print("\n--- Mission Validation ---")
    distances = [20, 500, 15000]
    for d in distances:
        valid = SpaceShip.is_valid_mission(d)
        status = "Valid" if valid else "Invalid"
        print(f"Distance {d}km: {status}")

    # 6. Final Status check
    print("\n--- Final Status ---")
    ship1.display_status()