import threading
import hashlib
from BRTA import BRTA
from vehicles import Car, Bike, Cng
from random import randint
from ride_manager import Uber
license_authority = BRTA()


class UserAlreadyExists(Exception):
    def __init__(self, email):
        print("User already exists with email", email)


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_encrypted = hashlib.md5(password.encode()).hexdigest()
        already_registered = False
        with open("users.txt", "r") as file:
            if email in file.read():
                already_registered = True
        file.close()
        if already_registered == False:
            with open("users.txt", 'a') as file:
                file.write(
                    f'name: {self.name} email: {self.email} password: {self.password_encrypted} \n')
                file.close()
        # print("User created")

    @staticmethod
    def log_in(email, password):
        store_pass = ''
        with open("user.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if (email in line):
                    line_split = line.split()[4]
                    if (line_split == "password:"):
                        store_pass = line.split()[5]
                else:
                    print("User not found")

            hash_pass = hashlib.md5(password.encode()).hexdigest()
            if (hash_pass == store_pass):
                # print("Logged in")
                pass
            else:
                print("Wrong password")


class Rider(User):
    def __init__(self, name, email, password, location, balance):
        self.location = location
        self.balance = balance
        self.__trip_history = []
        super().__init__(name, email, password)

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def request_ride(self, destation):
        pass

    def get_trip_history(self):
        return self.__trip_history

    def start_ride(self, fare, trip_info):
        self.balance -= fare
        self.__trip_history.append(trip_info)


class Driver(User):
    def __init__(self, name, email, password, location, licence):
        super().__init__(name, email, password)
        self.location = location
        self.licence = licence
        self.__trip_history = []
        self.earnings = 0
        self.vehicle = []
        self.valid_licence = license_authority.valided_license(
            email, self.licence)

    def take_driving_test(self):
        result = license_authority.driving_test(self.email)
        if result == True:
            self.valid_licence = True
            self.licence = license_authority.get_licence(self.email)
            # print("your licence number is", self.licence)

    def resigter_vehicle(self, type, plate, rate):
        if self.valid_licence is True:
            if type == "car":
                self.vehicle = Car(plate, type, rate, self)
            elif type == "bike":
                self.vehicle = Bike(plate, type, rate, self)
            elif type == "cng":
                self.vehicle = Cng(plate, type, rate, self)

            Uber.add_a_vehicle(type, self.vehicle)

        else:
            pass
            # print("Sorry! You need a valid licence to register a vehicle")

    def start_trip(self, start, destation, fare, info):
        self.earnings += fare
        self.location = destation
        # start a thread
        trip_thread = threading.Thread(
            target=self.vehicle.start_driving, args=(start, destation,))

        # start a thread
        trip_thread.start()

        # self.vehicle.start_driving(start, destation)
        self.__trip_history.append(info)

    def get_trip_history(self):
        return self.__trip_history

    def check_licence(self, email, licence):
        result = license_authority.valided_license(email, licence)
        if result == True:
            return True
            # print("Valid Licence")
        else:
            return False


Rider1 = Rider("Rider1", "rider@gmail.com", "rider1", 8, 10000)
Rider2 = Rider("Rider2", "rider2@gmail.com", "rider2", 9, 20000)
Rider3 = Rider("Rider3", "rider3@gmail.com", "rider3", 10, 30000)


for i in range(0, 10):
    driver1 = Driver(f"Driver{i}", f"Driver{i}@gmail.com",
                     f"driver{i}", randint(1, 30), randint(1, 10))
    driver1.take_driving_test()
    driver1.resigter_vehicle("car", randint(1, 30), randint(1, 30))

# print("get avaiable cars", Uber.get_available_vehicles())
Uber.find_a_vehicle(Rider1, "car", randint(1, 30))
Uber.find_a_vehicle(Rider2, "car", randint(1, 30))
Uber.find_a_vehicle(Rider3, "car", randint(1, 30))
# print(Uber.get_income())
# print("Rider 1 trip history", Rider1.get_trip_history())
