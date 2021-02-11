'''
Java variables are statically typed
ex. int num = 3;

Python variables are dynamically typed
ex. num = 3
'''

# Ints
num = 3
print(type(num))

# Floats
num = 3.14
print(type(num))

# Strings
num = "hello"
print(type(num))

# Booleans
num = True
print(type(num))

'''
As shown above, a variable can be used to represent several different types of data
However, this can also be an issue when troubleshooting, so be careful with this!

'''

var = 3
print(type(var))

# "Casting" an int variable to a float
var = float(var)
print(type(var))

# Float -> string
var = str(var)
print(type(var))
print(var)

# String -> int
word = '100'
word = int(word)
print(type(word))
print(word)