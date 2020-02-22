# 1st class
class Vehicle:
    def __init__(self):
        pass

# 2nd class
class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass

# 3rd class
class Starship(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass

# 3rd class
class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass

# 2nd class
class GroundVehicle(Vehicle):
    def __init__(self, num_wheels = 4):
        super().__init__()
        self.num_wheels = num_wheels

    def drive(self):
        return "vroooom"

# 3rd class
class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass

# 3rd class
class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels = 2):
        super().__init__()
        self.num_wheels = num_wheels

    def drive(self):
        return "BRAAAP!!"

# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

# class GroundVehicle():
#     def __init__(self, num_wheels):
#         self.num_wheels = num_wheels

    # TODO


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO

for veh in vehicles:
    print(veh.drive())