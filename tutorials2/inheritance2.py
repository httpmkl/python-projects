class Vehicle:

    def __init__(self, numWheels, numPassengers):
        self.numWheels = numWheels
        self.numPassengers = numPassengers

    def drive(self):
        print("I'm now driving")
        # Both child classes have this behaviour

    def changeNumPassengers(self, newMax):
        self.numPassengers = newMax
        # Again, accessible by both child classes


class Car(Vehicle):

    def __init__(self, numPassengers):
        super().__init__(4, numPassengers)
        # All cars have 4 wheels, but the amount of passengers depend on the specific car object

    def honkHorn(self):
        print('Honk honk')
        # Only cars have this behaviour


class Motorcycle(Vehicle):

    def __init__(self):
        super().__init__(2, 1)
        # All motorcycles have 2 wheels and 1 passengers
        self.leanAmount = 60

    def maxLeanAmount(self, maxLean):
        self.leanAmount = maxLean
        # Only motorcycles have this behaviour


car = Car(5)
motorcycle = Motorcycle()

print(car.numWheels)
print(motorcycle.numWheels)

car.drive()
motorcycle.drive()

car.changeNumPassengers(4)
motorcycle.changeNumPassengers(2)

car.honkHorn()
motorcycle.maxLeanAmount(5)