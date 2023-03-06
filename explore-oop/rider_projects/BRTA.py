import random


class BRTA:
    def __init__(self):
        self.__licences = {}

    def driving_test(self, email):
        score = random.randint(0, 100)
        if score > 33:
            license_number = random.randint(100000, 999999)
            self.__licences[email] = license_number
            # print(
            #     "Congratulations! You have passed the driving test. Your license number is", license_number)
            return True

        else:
            # print("Sorry! You have failed the driving test.")
            return False

    def valided_license(self, email, license_number):
        for key, value in self.__licences.items():
            # print(key, value)
            if key == email and value == license_number:
                return True
            else:
                return False

    def get_licence(self, email):
        return self.__licences[email]
