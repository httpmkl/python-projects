'''

Completed:

To complete:

'''

from protagonist import Player
from loadGame import SavedGame
startGame = False


# ---------- GAME DATA ----------
class Game:
    level = 0

    def __init__(self):
        pass


# ---------- MENU OPTIONS ----------
def instructions():
    if not startGame: # Brief welcome message
        pass
    # Rest of the instructions dialogue

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
        print('\n[ You must begin a game before accessing your stats! ]')
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
    # storyline here
    create_player()

def create_player():
    name = input('\n-> ENTER YOUR NAME: ')
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
                print('[ Please enter a valid input! ]')
                goodInput = False
        except ValueError:  # Typed in non-integers
            print('[ Please enter a valid input! ]')
            goodInput = False

    goodInput = False
    while not goodInput:
        try:
            goodInput = True
            secChoice = int(input('\n-> PICK YOUR SECONDARY ATTRIBUTE: '))

            # Assigns trait based on choice
            if secChoice == mainChoice:
                print('[ You have already chose this trait! ]')
                goodInput = False
            elif secChoice == 1:  # Strength
                # TODO: FIX THIS MECHANICs
                if mainChoice == 2:
                    secondaryAtr = 'strength'
                else:
                    print('[ You have already chose the opposing! ]')
                    goodInput = False
            elif secChoice == 2:  # Endurance
                secondaryAtr = 'endurance'
            elif secChoice == 3:  # Flexibility
                secondaryAtr = 'flexibility'
            elif secChoice == 4:  # Speed
                secondaryAtr = 'speed'
            elif secChoice == 5:  # Intelligence
                secondaryAtr = 'intelligence'
            elif secChoice == 6:  # Mystery
                secondaryAtr = 'mystery'
            else:  # Invalid number
                print('[ Please enter a valid input! ]')
                goodInput = False
        except ValueError:  # Typed in non-integers
            print('[ Please enter a valid input! ]')
            goodInput = False

    goodInput = False
    while not goodInput:
        try:
            goodInput = True
            thirdChoice = int(input('\n-> PICK YOUR THIRD ATTRIBUTE: '))

            # Assigns trait based on choice
            if thirdChoice == mainChoice or thirdChoice == secChoice:
                print('[ You have already chose this trait! ]')
                goodInput = False
            elif thirdChoice == 1:  # Strength
                weakAtr = 'strength'
            elif thirdChoice == 2:  # Endurance
                weakAtr = 'endurance'
            elif thirdChoice == 3:  # Flexibility
                weakAtr = 'flexibility'
            elif thirdChoice == 4:  # Speed
                weakAtr = 'speed'
            elif thirdChoice == 5:  # Intelligence
                weakAtr = 'intelligence'
            elif thirdChoice == 6:  # Mystery
                weakAtr = 'mystery'
            else:  # Invalid number
                print('[ Please enter a valid input! ]')
                goodInput = False
        except ValueError:  # Typed in non-integers
            print('[ Please enter a valid input! ]')
            goodInput = False

    traits = [mainAtr, secondaryAtr, weakAtr]
    Player(traits)
    print(Player.strength)
    
def traits_desc():
    print('\n| CHARACTERISTICS')
    print('\n1. STRENGTH: Increases your attack damage')
    print('2. ENDURANCE: Lowers your enemy\'s attack damage')
    print('\n3. FLEXIBILITY: Increases your dodge accuracy')
    print('4. SPEED: Lowers your enemy\'s dodge accuracy')
    print('\n5. INTELLIGENCE: Increases your prediction accuracy')
    print('6. MYSTERY: Lowers your enemy\'s prediction accuracy')

# ---------- START SCREEN ----------
def menu():
    # Menu screen
    print('\n---------------') # 15 dashes
    print('\nTHE SPARTAN GAMES')
    print('\n| 1. NEW GAME')
    print('| 2. LOAD GAME')
    print('| 3. PLAYER STATS')
    print('| 4. INVENTORY')
    print('| 5. INSTRUCTIONS')

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
                print('[ Please enter a valid input! ]')
                goodInput = False
        except ValueError:  # Typed in non-integers
            print('[ Please enter a valid input! ]')
            goodInput = False


if not startGame:
    instructions()
    startGame = True
    menu()