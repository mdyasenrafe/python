from abc import ABC, abstractmethod
from time import sleep


class Vehicle:
    speeds = {
        'car': 10,
        'bike': 20,
        'cng': 15
    }

    def __init__(self, plate, vehicle_type, rate, driver):
        self.plate = plate
        self.vehicle_type = vehicle_type
        self.rate = rate
        self.driver = driver
        self.speed = self.speeds[vehicle_type]
        self.status = "available"

    @abstractmethod
    def start_driving(self):
        pass

    @abstractmethod
    def trip_finished(self):
        pass


class Car(Vehicle):
    def __init__(self, plate, vehicle_type, rate, driver):
        super().__init__(plate, vehicle_type, rate, driver)

    def start_driving(self, start, destination):
        self.status = "unavailable"
        distance = abs(start - destination)
        for i in range(0, distance):
            sleep(0.5)
            print(f'{self.plate} started {i} and distance is, {distance}\n')
        self.trip_finished()

    def trip_finished(self):
        self.status = "available"
        print(self.vehicle_type, "finish")


class Bike(Vehicle):
    def __init__(self, plate, vehicle_type, rate, driver):
        super().__init__(plate, vehicle_type, rate, driver)

    def start_driving(self):
        self.status = "unavailable"
        print(self.vehicle_type, "started")

    def trip_finished(self):
        self.status = "available"
        print(self.vehicle_type, "finish")


class Cng(Vehicle):
    def __init__(self, plate, vehicle_type, rate, driver):
        super().__init__(plate, vehicle_type, rate, driver)

    def start_driving(self):
        self.status = "unavailable"
        print(self.vehicle_type, "started")

    def trip_finished(self):
        self.status = "available"
        print(self.vehicle_type, "finish")
