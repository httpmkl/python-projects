# Python methods and functions intro

# You don't have to define the type of data that comes in
def myFunction(var1, var2):
    sum = var1 + var2
    return sum


print(myFunction(1, 2))  # Calls the function
print(myFunction('1', '2'))
# As you can see, issues arise with this flexibility
