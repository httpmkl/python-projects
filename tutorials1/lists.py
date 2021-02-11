# Python introductory data structures
# Lists are heterogeneous (allow diverse data types)

# ITERABLE

# Type 1: LISTS [] — ordered, changeable, allows duplicates
data = [1,2,3,4,5]
print(data)
print(len(data)) # Prints data length
data.append(5) # Adds 5 to the end of the list
print(data)
data.insert(2, 11) # Adds 11 to the 2nd slot
print(data)
data.remove(2) # Looks for the element "2" and removes it (not the 2nd slot!)
print(data)

data2 = [1,2,3,4,5,2,7]
print(data2)
data2.sort() # Orders from lowest to greatest
print(data2)
data2.sort(reverse=True) # Orders from greatest to lowest
print(data2)

data3 = ['apple', 'orange', 'zoo', 'panda', 'apple']
data3.sort() # Sorts into alphabetical order
print(data3)
data3.sort(reverse=True) # Sorts into reverse alphabetical order
print(data3)
print(data3.index('zoo')) # Looks for where 'zoo' is located


# Type 2: TUPLES () — ordered, unchangeable, allows duplicates
dataTuple = (1,2,3,4,5,1,1,) # Notice the () and not []
print(dataTuple)
print(type(dataTuple))
print(dataTuple.index(3))
print(dataTuple.count(1))

# Tuples are unchangeable and can be helpful for this attribute
# However, if a change is needed, we can convert it to a list
dataTuple2 = ('Name', 'Phone Number', 5, 28.99)
listConvert = list(dataTuple2)
print(listConvert)
listConvert[3] = 32.99
print(listConvert)
dataTuple2 = tuple(listConvert)
print(dataTuple2)


# Type 3: SET {} — unordered, semi-changeable, no duplicates
dataSet = {1,2,3,4,5,5,5} # Output = {1,2,3,4,5}
print(dataSet)
# Helpful for locating all of the elements w/o duplicates