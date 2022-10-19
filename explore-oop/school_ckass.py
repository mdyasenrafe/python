class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher


class Teacher:
    def __init__(self, name, course):
        self.name = name
        self.course = course
