# Loops

# For loop - when you know how many times you want the loop to run
# for (var) in (iterable):
#   [content]

menu = ('Burger', 'Fries', 'Pop', 'Pancakes')

for food in menu:
    print(food)
    # Without stating any number, it only says whats IN menu

for num in range(10):
    print(num)
    # This range() function is a limiting condition

for num2 in range(16, 3, -1):
    # From 16-3 (not inclusive), counting by -1 (decreasing)
    print(num2)

for num3 in range(99, 0, -1):
    print(str(num3) + ' bottles of beer on the wall. Take one down and pass it around ...')
    # You cannot mix an int and string; convert to string first


# While loop - when you DON'T know how many time you want the loop to run

limit = 100

while 1 < 2:
    limit -= 1
    print('Hello! This will run this many more times: ' + str(limit))
    if limit == 0:
        break

print('Loop finished!')


goodInput = False
# Remember the syntax; true/false are capitalized

while not goodInput:
    userInput = int(input('1. Start Game   \n2. Load Game    \n3. Quit Game \n'))
    if userInput == 1:
        print('Game started')
        goodInput = True # One strategy for ending the loop
    elif userInput == 2:
        print('Game loaded')
        break # Another strategy to use
    elif userInput == 3:
        print('Game over...')
        goodInput = True
    else:
        print('Bad input. Please try again and listen this time.')