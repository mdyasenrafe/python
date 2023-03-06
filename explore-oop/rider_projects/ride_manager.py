class RideManager:
    def __init__(self):
        self.__income = 0
        self.__trip_history = []
        self.__aviailable_cars = []
        self.__available_bikes = []
        self.__available_cngs = []

    def add_a_vehicle(self, type, vehicle):
        if type == "car":
            self.__aviailable_cars.append(vehicle)
        elif type == "bike":
            self.__available_bikes.append(vehicle)
        elif type == "cng":
            self.__available_cngs.append(vehicle)

    def get_available_vehicles(self):
        return len(self.__aviailable_cars)

    def get_income(self):
        return self.__income

    def get_trip_history(self):
        return self.__trip_history

    def find_a_vehicle(self,  rider, type, destination):
        if type == "car":
            if len(self.__aviailable_cars) == 0:
                print("Sorry! No car available")
                return False
            else:
                for car in self.__aviailable_cars:
                    if abs(rider.location - car.driver.location) < 20:
                        distance = abs(rider.location - destination)
                        fare = distance * car.rate
                        if rider.balance >= fare:
                            if car.status == "available":
                                car.status = "unavailable"
                                self.__aviailable_cars.remove(car)

                                trip_info = f'match for {rider.name} for fare {fare} with {car.driver.name} started from {rider.location} to {destination}'
                                rider.start_ride(fare, trip_info)

                                self.__income += fare * 0.2
                                car.driver.start_trip(
                                    rider.location, destination, fare * 0.8, trip_info)
                                # print(trip_info)
                                return car
                            else:
                                print("No Car Available")
                        else:
                            print("Sorry! You don't have enough balance")
                    else:
                        print("Sorry! No car Found For this location")

        return self.__aviailable_cars[0]

    def get_a_vehicle(self, type):
        pass

    def match_vehicle(self):
        pass


Uber = RideManager()
