class School:
    def __init__(self, name, address, principal):
        self.name = name
        self.address = address
        self.principal = principal
        self.grades = []

    def add_grade(self, name, teacher):
        new_grade = Grade(name, teacher)
        self.grades.append(new_grade)

    def remove_grade(self, name):
        for grade in self.grades:
            if grade.name == name:
                self.grades.remove(grade)


class Grade:
    def __init__(self, name, teacher):
        self.students = []
        self.name = name
        self.teacher = teacher

    def __repr__(self):
        return f'{self.name} with {self.teacher}'

    def __del__(self):
        print(f'{self.name} has been deleted')


oxford = School("Oxford", "London", "Mr. Smith")
oxford.add_grade("Grade 1", "Mr. John")
oxford.add_grade("Grade 2", "Mr. Peter")
oxford.add_grade("Grade 3", "Mr. Paul")
# oxford.remove_grade("Grade 2")


print(oxford.grades)
