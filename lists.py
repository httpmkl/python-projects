# Python introductory data structures
# Lists are heterogeneous (allow diverse data types)

# ITERABLE

# Type 1: LISTS [] (ordered, changeable, allows duplicates
data = [1,2,3,4,5]
print(data)
print(len(data)) # Prints data length
data.append(5) # Adds 5 to the end of the list
print(data)
data.insert(2, 11) # Adds 11 to the 2nd slot
print(data)
data.remove(2) # Looks for the element "2" and removes it (not the 2nd slot!)
print(data)