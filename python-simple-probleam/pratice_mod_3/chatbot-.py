greet_words = ['hello', 'hi', 'hey', 'hola', 'howdy', 'hey there']
bye_words = ['bye', 'goodbye', 'see you later', 'adios', 'ciao', 'later']


def listen():
    return input("What do you want to say? ")


def respond(message):
    broken_word = message.lower().split(" ")
    for word in broken_word:
        if word in greet_words:
            talkBack("Hello, how are you?")
            break
        elif word in bye_words:
            talkBack("Goodbye, have a nice day!")
            break
        else:
            talkBack("I don't understand what you said")
            break


def talkBack(message):
    print(message)


while 1:
    message = listen()
    respond(message)
    broken_word = message.lower().split(" ")
    for word in broken_word:
        if word in bye_words:
            break
