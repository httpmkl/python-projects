'''

Completed:

To complete:

'''

from character import Player
from loadGame import SavedGame
import story
import time
startGame = False


# ---------- GAME DATA ----------
class Game:
    level = 0

    def __init__(self):
        pass


# ---------- MENU OPTIONS ----------
def instructions():
    # Rest of the instructions dialogue
    pass

def new_game():
    # Starts a new game
    reset = 'Level 0'
    SavedGame.writeStringOverFile(SavedGame, reset)
    newGame = SavedGame.getFileAllLines(SavedGame)
    start_game(newGame)

def load_game():
    # Opens saved game
    pastGame = SavedGame.getFileAllLines(SavedGame) # Retrieves save point data
    start_game(pastGame)

def player_stats():
    if Player.name == 'Placeholder':
        print('\n---------------')
        print('\n[ you must begin a game before accessing your stats! ]')
        menu()
    else:
        pass

def inventory():
    # Accesses inventory
    pass


# ---------- GAMEPLAY ----------
def start_game(data):
    levelNum = str(data[0]).split(' ')
    Game.level = int(levelNum[1]) # Assigns game level to Game.level
    if Game.level == 0:
        # Takes user to level one
        level_one()
    else:
        pass

def level_one():
    story.one_start()
    create_player()

def traits_desc():
    print('\n| CHARACTERISTICS')
    print('\n1. STRENGTH: Increases your attack damage')
    print('2. ENDURANCE: Lowers your enemy\'s attack damage')
    print('\n3. FLEXIBILITY: Increases your dodge accuracy')
    print('4. SPEED: Lowers your enemy\'s dodge accuracy')
    print('\n5. INTELLIGENCE: Increases your prediction accuracy')
    print('6. MYSTERY: Lowers your enemy\'s prediction accuracy')

def create_player():
    name = input('\n[ what is your name? ]\n-> ')
    traits_desc()

    goodInput = False
    while not goodInput:
        try:
            goodInput = True
            mainChoice = int(input('\n-> PICK YOUR TOP ATTRIBUTE: '))

            # Assigns trait based on choice
            if mainChoice == 1:  # Strength
                mainAtr = 'strength'
            elif mainChoice == 2:  # Endurance
                mainAtr = 'endurance'
            elif mainChoice == 3:  # Flexibility
                mainAtr = 'flexibility'
            elif mainChoice == 4:  # Speed
                mainAtr = 'speed'
            elif mainChoice == 5:  # Intelligence
                mainAtr = 'intelligence'
            elif mainChoice == 6:  # Mystery
                mainAtr = 'mystery'
            else:  # Invalid number
                print('[ please enter a valid input ]')
                goodInput = False
        except ValueError:  # Typed in non-integers
            print('[ please enter a valid input ]')
            goodInput = False

    goodInput = False
    while not goodInput:
        try:
            goodInput = True
            secChoice = int(input('\n-> PICK YOUR SECONDARY ATTRIBUTE: '))

            # Assigns trait based on choice
            if secChoice == mainChoice:
                print('[ you have already chose this trait ]')
                goodInput = False
            elif secChoice == 1:  # Strength
                if mainChoice != 2:
                    secondaryAtr = 'strength'
                else:
                    print('[ you have already chose the opposing! ]')
                    goodInput = False
            elif secChoice == 2:  # Endurance
                if mainChoice != 1:
                    secondaryAtr = 'endurance'
                else:
                    print('[ you have already chose the opposing! ]')
                    goodInput = False
            elif secChoice == 3:  # Flexibility
                if mainChoice != 4:
                    secondaryAtr = 'flexibility'
                else:
                    print('[ you have already chose the opposing! ]')
                    goodInput = False
            elif secChoice == 4:  # Speed
                if mainChoice != 3:
                    secondaryAtr = 'speed'
                else:
                    print('[ You have already chose the opposing! ]')
                    goodInput = False
            elif secChoice == 5:  # Intelligence
                if mainChoice != 6:
                    secondaryAtr = 'intelligence'
                else:
                    print('[ You have already chose the opposing! ]')
                    goodInput = False
            elif secChoice == 6:  # Mystery
                if mainChoice != 5:
                    secondaryAtr = 'mystery'
                else:
                    print('[ You have already chose the opposing! ]')
                    goodInput = False
            else:  # Invalid number
                print('[ please enter a valid input ]')
                goodInput = False
        except ValueError:  # Typed in non-integers
            print('[ please enter a valid input ]')
            goodInput = False

    goodInput = False
    while not goodInput:
        try:
            goodInput = True
            thirdChoice = int(input('\n-> PICK YOUR THIRD ATTRIBUTE: '))

            # Assigns trait based on choice
            if thirdChoice == mainChoice or thirdChoice == secChoice:
                print('[ you have already chose this trait ]')
                goodInput = False
            elif thirdChoice == 1:  # Strength
                if mainChoice != 2 and secChoice != 2:
                    weakAtr = 'strength'
                else:
                    print('[ You have already chose the opposing! ]')
                    goodInput = False
            elif thirdChoice == 2:  # Endurance
                if mainChoice != 1 and secChoice != 1:
                    weakAtr = 'endurance'
                else:
                    print('[ You have already chose the opposing! ]')
                    goodInput = False
            elif thirdChoice == 3:  # Flexibility
                if mainChoice != 4 and secChoice != 4:
                    weakAtr = 'flexibility'
                else:
                    print('[ You have already chose the opposing! ]')
                    goodInput = False
            elif thirdChoice == 4:  # Speed
                if mainChoice != 3 and secChoice != 3:
                    weakAtr = 'speed'
                else:
                    print('[ You have already chose the opposing! ]')
                    goodInput = False
            elif thirdChoice == 5:  # Intelligence
                if mainChoice != 6 and secChoice != 6:
                    weakAtr = 'intelligence'
                else:
                    print('[ You have already chose the opposing! ]')
                    goodInput = False
            elif thirdChoice == 6:  # Mystery
                if mainChoice != 5 and secChoice != 5:
                    weakAtr = 'mystery'
                else:
                    print('[ You have already chose the opposing! ]')
                    goodInput = False
            else:  # Invalid number
                print('[ please enter a valid input ]')
                goodInput = False
        except ValueError:  # Typed in non-integers
            print('[ please enter a valid input ]')
            goodInput = False

    traits = [name, mainAtr, secondaryAtr, weakAtr]
    Player(traits) # Creates player based on input
    print('\n[ You have successfully created your player! ]')


# ---------- START SCREEN ----------
def menu():
    # Menu screen
    print('\n| 1. new game')
    print('| 2. load game')
    print('| 3. player stats')
    print('| 4. inventory')
    print('| 5. instructions')

    goodInput = False

    while not goodInput:
        try:
            goodInput = True
            choice = int(input('\n-> '))

            # Redirecting based on choices
            if choice == 1:  # New game
                new_game()
            elif choice == 2:  # Load game
                load_game()
            elif choice == 3: # Player stats
                player_stats()
            elif choice == 4:  # Inventory
                inventory()
            elif choice == 5: # Instructions
                instructions()
            else: # Typed an number outside of the options
                print('[ please enter a valid input ]')
                goodInput = False
        except ValueError:  # Typed in non-integers
            print('[ please enter a valid input ]')
            goodInput = False


if not startGame:
    story.intro_start(True)
    print('\n\n---------------')  # 15 dashes
    print('\nPLAYER, WELCOME TO THE SPARTAN GAMES')
    print('\n---------------\n')
    time.sleep(4)
    instructions()
    startGame = True
    menu()