from TravelAgent import TravelAgent


def main():
    travel_agent = TravelAgent('Travel Agent')
    trip_info = travel_agent.set_trip_one_city_one_way(
        'DAC', 'PRA', '2021-12-12')

    print(trip_info[0].fight)
    print(trip_info[1])


if __name__ == "__main__":
    main()
