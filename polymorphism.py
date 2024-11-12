class Vehicle:
    # Base class with an abstract method move()
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    # Car class overrides the move method
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    # Plane class overrides the move method
    def move(self):
        print("Flying ✈️")

class Bicycle(Vehicle):
    # Bicycle class overrides the move method
    def move(self):
        print("Pedaling 🚲")

# Function to demonstrate polymorphism
def demonstrate_movement(vehicle):
    vehicle.move()

# Example usage of polymorphism
vehicles = [Car(), Plane(), Bicycle()]

for vehicle in vehicles:
    demonstrate_movement(vehicle)
