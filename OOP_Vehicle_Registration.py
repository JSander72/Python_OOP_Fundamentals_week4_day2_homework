### Task 1: Vehicle Registration System

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

vehicle1 = Vehicle("ABC123", "Car", "John Doe")
vehicle2 = Vehicle("XYZ789", "Motorcycle", "Jane Smith")

print(f"Vehicle 1 Owner: {vehicle1.owner}")
print(f"Vehicle 2 Owner: {vehicle2.owner}")

vehicle1.update_owner("Alice Johnson")
vehicle2.update_owner("Bob Brown")

print(f"Vehicle 1 New Owner: {vehicle1.owner}")
print(f"Vehicle 2 New Owner: {vehicle2.owner}")