# Python arrays
# Arrays = homogenous (same type(, contiguous (side-by-side) data

import array
# Import arrays since its not a built in feature

numbers = array.array('i', [1,2,3,4,5])
print(numbers)

# Adding an extra value
numbers.append(6)
print(numbers)


# Generally speaking, arrays are not necessary in Python. Avoid them

