import random


def save_student_with_unique(name, mark):
    # create dictionary
    student = {}
    student['name'] = name
    student['mark'] = mark
    # genrate unique id using random
    student['student_id '] = random.randint(1000, 9999)
    # create dict file with txt
    with open('student.txt', 'a') as file:
        file.write(str(student))
        file.write('\n')
    print('student saved')


name = input('Enter student name: ')
mark = input('Enter student mark: ')
save_student_with_unique(name, mark)
