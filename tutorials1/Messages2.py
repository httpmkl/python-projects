class ChatBot:

    # Constructor - sets up the initial state of my object
    def __init__(self):
        print('ChatBot class created!')

    # Arguments are the input, returns are the outputs given to the user

    # Type 1 - No argument, no return
    def printMessage(self):  # (self) is required for methods
        print('Hello world')

    # Type 2 - Argument, no return
    def sayHiToMe(self, name):
        print(f'Hello, {name}')

    # Type 3 - No argument, return
    def sendSecretMessage(self):
        return 'I love you.'

    # Type 4 - Argument and return
    def doMyHomework(self, numOne, numTwo):
        print("OK, I'm happy to help you with that")
        # Use '' for strings, unless an ' is inside (instead use "")
        return numOne + numTwo


def nonSentientMessage():
    return 'I am not sentient'
