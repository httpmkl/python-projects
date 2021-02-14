# Battle Arena RPG game - made by Nora Calif
startGame = False
from statistics import UserStats


# ---------- GAME START ----------

def game():
    print('\nGAME: STARTED')

# ----------- GAME END -----------


# Inventory
def inventory():
    print('\n---------------')
    print('INVENTORY\n')

    print('Under Construction')

    print('---------------')
    startScreen(True) # Loops back to ask what they want to do

# Stats
def stats():
    stats = UserStats()

    print('\n---------------')
    print('USER STATS\n')

    print(f'-> Health: {stats.getHealth()}') # Prints health
    print(f'-> Defense: {stats.getShield()}') # Prints shield

    print('---------------')
    startScreen(True)


# Start screen
def startScreen(trueOrFalse):
    hasItStarted = trueOrFalse
    goodInput = False

    while not hasItStarted: # This part only shows in the beginning of the game
        print('\n~ WELCOME TO THE BATTLE ARENA ~\n')

        # Menu
        print('MENU:')
        print('1. Open Inventory')
        print('2. Check Stats')
        print('3. START GAME')
        break

    while not goodInput:
        try:
            goodInput = True

            # To tell whether this is the program's first run or not
            if not hasItStarted: # First run
                choice = int(input('\nWhat would you like to start with, player? \n-> '))
            else:  # Not first run
                choice = int(input('\nWhat would you like to do next, player? \n-> '))

            # Redirecting based on choices
            if choice > 3 or choice < 0: # Typed an number outside of the options
                print('\nPlease enter a valid input!')
                goodInput = False
            elif choice == 1: # Chose inventory
                hasItStarted = True
                inventory()
            elif choice == 2: # Chose stats
                hasItStarted = True
                stats()
            else: # Chose game
                hasItStarted = True
                game()
        except ValueError: # Typed in non-integers
            print('\nPlease enter a valid input!')
            goodInput = False


# Starts game at the beginning
if not startGame:
    startScreen(False)
    startGame = True
