# Python classes & modules

# Classes in python aren't aware of each other; must be imported
from Formulas import NewClass   # Import NewClass class
import Formulas as f    # The functions are not in a class; just import
# 'as f' is essentially creating a variable to replace Formulas

messages = NewClass()   # Instantiation
messages.printMessage()

# Instantiation isn't necessary when the functions are not in a class
print(f.sum(3, 4))
print(f.difference(8, 11))
