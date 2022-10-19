def work():
    print("I am working")


def do_something(param):
    print("start somwething")
    param()
    print("end somwething")


def practice_something():
    print("I am working something")


def learning_pything():
    print("I am learning python")

# do_something(practice_something)

def first_function():
    print("I am first function")
    def inside_function():
        print("I am inside function")
    # inside_function()
    return inside_function

first_function()()
