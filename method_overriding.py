#Real-world scenario: Vehicle rental system
# Parent class: Vehicle
class Vehicle:
    def __init__(self, vehicle_type, base_rate):
        self.vehicle_type = vehicle_type
        self.base_rate = base_rate

    def rent(self, days):
        cost = self.base_rate * days
        print(f"Renting {self.vehicle_type} for {days} days. Total cost: ${cost}")

# Child class: Car
class Car(Vehicle):
    def rent(self, days):
        insurance_fee = 50
        cost = (self.base_rate * days) + insurance_fee
        print(f"Renting Car for {days} days with insurance. Total cost: ${cost}")

# Child class: Bike
class Bike(Vehicle):
    def rent(self, days):
        helmet_fee = 10
        cost = (self.base_rate * days) + helmet_fee
        print(f"Renting Bike for {days} days with helmet. Total cost: ${cost}")

# Child class: Truck
class Truck(Vehicle):
    def rent(self, days):
        maintenance_fee = 150
        cost = (self.base_rate * days) + maintenance_fee
        print(f"Renting Truck for {days} days with maintenance fee. Total cost: ${cost}")

# Sample rental vehicles
car = Car("Car", 100)
bike = Bike("Bike", 40)
truck = Truck("Truck", 200)

# Test rentals
car.rent(3)     # Car rental
bike.rent(2)    # Bike rental
truck.rent(1)   # Truck rental
