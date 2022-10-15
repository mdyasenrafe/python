import pyjokes


def tell_some_jokes():
    return pyjokes.get_joke()


while True:
    ans = input("Do you want to hear a joke? (y/n) ")
    if ans == "y":
        print(tell_some_jokes())
    else:
        print("Ok, bye!")
        break
