"""
CP1404/CP5632 Practical
Car class
"""


class Car:
    """ represent a car object """

    def __init__(self, name, fuel=0):
        """ initialise a Car instance """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return "{}, fuel={}, odo={}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """ add amount to the car's fuel"""
        self.fuel += amount
        return self.fuel

    def drive(self, distance):
        """ drive the car a given distance if it has enough fuel or drive until fuel runs out
        return the distance actually driven """
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
            distance_driven = distance
        self.odometer += distance_driven
        return distance_driven

class UnreliableCar(Car):
    import random

    def __init__(self, name, fuel):
        super().__init__(name, fuel)

    def __str__(self):
        "{}, fuel={}, odo={}".format(self.name, self.fuel, self.odometer)

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        self.reliability = 4
        self.drive = 5
        # self.reliability = float(random.uniform(0, 100))
        # self.drive = float(random.uniform(0, 100))
        if self.drive > self.reliability:
            distance_driven = super().drive(distance)
            return distance
        else:
            distance_driven = 0
            return distance


class Taxi(Car):
    """ specialised version of a Car that includes fare costs """

    def __init__(self, name, fuel):
        """ initialise a Taxi instance, based on parent class Car """
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """ return a string representation like a car but with current fare distance"""
        return "{}, {}km on current fare, ${:.2f}/km, total fare is ${}".format(super().__str__(), self.current_fare_distance, self.taxi_price_per_km, self.get_fare())

    def taxi_price_per_km(self):
        taxi_price_per_km = 1.2
        return taxi_price_per_km

    def get_fare(self):
        """ get the price for the taxi trip """
        return self.taxi_price_per_km() * self.current_fare_distance

    def start_fare(self):
        """ begin a new fare """
        self.current_fare_distance = 0

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven