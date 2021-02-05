print("Testing w/ mathematical operators")

'''
Mathematical operators
    + (add)
    - (subtract)
    * (multiply)
    / (divide)
    // (base division)
    ** (exponentiate)
    % (modulo)
'''


a = 3
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
# Unlike Java, the / is expressed as a decimal
# Remember that data types are inferred!
print(a // b) # Produces an int
print(a ** b) # a^b
print(a % b)


print("Testing w/ relational operators")

'''
Relational operators
    == (equals)
    != (does not equa;)
    > (greater than)
    < (less than)
    >= (greater than or equal to)
    <= (less than or equal to)
'''

c = 5
d = 3

print(c == d)
print(c != d)
print(c > d)
print(c < d)
print(c >= d)
print(c <= d)
# These all return as True or False

print("Using relational operators for strings")

e = 'Apple'
f = 'Zoo'
g = 'Apple'

print(e == f)
print(e != f)
print(e > f)
print(e == g)