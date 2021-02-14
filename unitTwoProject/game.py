# Battle Arena RPG game - made by Nora Calif
startGame = False
from player import Character


# ---------- GAME START ----------

def game():
    print('\n--------------------')
    print('GAME: STARTED')
    print('--------------------')

# ----------- GAME END -----------


# Inventory
def inventory():
    print('\n---------------')
    print('Inventory\n')

    print('Under Construction')

    print('---------------')
    startScreen(True) # Loops back to ask what they want to do

# Stats
def stats():
    print('\n---------------')
    print(f'{player.getName()}\'s Stats\n')

    print(f'-> Health: {player.getHealth()}') # Shows health stat
    print(f'-> Shield: {player.getShield()}') # Shows shield stat
    print(f'-> Energy: {player.getEnergy()}%')  # Shows energy stat
    print(f'\nMONEY AVAILABLE: ${player.getMoney()}')  # Show money available

    print('---------------')
    startScreen(True)


# Start screen
def startScreen(trueOrFalse):
    hasItStarted = trueOrFalse
    goodInput = False

    while not hasItStarted: # This part only shows in the beginning of the game
        print('\n~ WELCOME TO THE BATTLE ARENA ~\n')
        name = input('Enter your name: ')
        player.setName(name)

        # Menu
        print('\nMENU:')
        print('1. Open Inventory')
        print('2. Check Stats')
        print('3. START GAME')
        break

    while not goodInput:
        try:
            goodInput = True

            # To tell whether this is the program's first run or not
            if not hasItStarted: # First run
                choice = int(input(f'\nWhat would you like to start with, {player.getName()}? \n-> '))
            else:  # Not first run
                choice = int(input(f'\nWhat would you like to do next, {player.getName()}? \n-> '))

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
    player = Character() # Creates the player
    startScreen(False)
    startGame = True
