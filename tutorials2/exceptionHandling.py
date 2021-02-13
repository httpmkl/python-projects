'''
    Python Exception Handling - try/except
    Several types of errors illustrated below
    Take it out of the brackets if you wish to run it
'''


# 1. Generic
'''
goodInput = False

while not goodInput:
    try:
        num = int(input('Enter a number: '))
        # Functionality below doesn't process if not an int
        print(f'You entered: {num}')
        goodInput = True
    except:
        # This is where we end up if there is an error
        print('You typed in something dumb.')
'''

# 2. ValueError (string to int)
'''
goodInput = False

while not goodInput:
    try:
        num = int(input('Enter a number: '))
        # Functionality below doesn't process if not an int
        print(f'You entered: {num}')
        goodInput = True
    except ValueError: # Only looks for ValueError
        # This is where we end up if there is an error
        print('You typed in something dumb.')
'''

# 3. TypeError
'''
data = [1, 2, 3, 4]

for x in range(len(data)):
    data[x] += 1

print(data)

# Data with mixed
data2 = [1, 2, 3, 4, '5']

try:
    for x in range(len(data2)):
        data2[x] += 1
except TypeError:
    print('This entry is not an int so ignore it')
    # It prints (value + 1) for every value except for the string

print(data2)  # Returns TypeError without try/except
'''

# 4. ZeroDivisionError
'''
num = int(input('Type in a number to divide into 5: '))
result = 5/num
print(result)
# If '0' is typed, error occurs

# Put this in a while loop with a boolean if you want an except loop
try:
    num2 = int(input('Type in a number to divide into 5: '))
    result2 = 5/num2
    print(result2)
except ZeroDivisionError:
    print('Do not divide by 0 silly!')
'''

# 5. IndexError
'''
data = [1,2,3,4,'5']

try:
    for x in range(6): # IndexError; out of range
        data[x] += 1
except IndexError: # If range is more than data length
    print('You went out of bounds again ...')
except TypeError: # If a data type is not an int
    print('Wrong type!')
'''