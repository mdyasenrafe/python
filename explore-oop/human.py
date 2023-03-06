class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Police(Person):
    def __init__(self, name, age, gender, case, nationality):
        super().__init__(name, age, gender)
        self.nationality = nationality

        # if the user give the case as a string, don't crash the program
        if not isinstance(case, bool):
            print("The case must be an boolean")
            self.case = None
            return
        self.case = case


Rahim = Police(" Rahim", 25, "Male", "True", "Bangladeshi")
print(Rahim.case)
