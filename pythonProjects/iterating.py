# Python introductory data structure
# Iterating over data

data = ['apple',1,'orange',4,'zoo',True,'panda',3.14]
print(data)

# Prints each entry one at a time
for item in data: # Item is a variable; could be anything
    print(item)


numData = [1,2,3,4,5]

for num in numData:
    num += 1
    print(num)

print(numData) # Output = [1,2,3,4,5]
# The effects of that "for" loop is limited to within the loop

# Using this strategy, change can actually occur
for num in range(len(numData)):
    numData[num] += 1

print(numData) # Output = [2,3,4,5,6]


# Going back to data = ['apple',1,'orange',4,'zoo',True,'panda',3.14]

for val in data:
    if isinstance(val, int):
        print(f"Int {val}")
    elif isinstance(val, str):
        print(f"String {val}")
    elif isinstance(val, bool):
        print(f"Bool {val}")
        # Output: Int True
        # Booleans can be interpreted as a int b/c True = 1 & False = 0
    elif isinstance(val, float):
        print(f"Float {val}")

