# Formulas is my module and that's all I need!

# Functions — like methods, but outside of a class
def sum(numOne, numTwo):
    return int(numOne + numTwo)


def difference(numOne, numTwo):
    return int(numOne - numTwo)


# Classes and standalone functions can coexist in a file

class NewClass:  # Creating a class; included is everything indented

    # Constructor - sets up the initial state of my object
    def __init__(self):
        print('NewClass class created!')

    # Methods
    def printMessage(self):
        print('Hello world!')
