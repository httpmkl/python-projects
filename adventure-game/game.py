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


# ---------- GAMEPLAY ----------
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
        print("\n---------------")
        print('\n[ You must begin a game before accessing your stats! ]')
        menu()
    else:
        pass

def inventory():
    # Accesses inventory
    pass

def start_game(data):
    levelNum = str(data[0]).split(' ')
    Game.level = int(levelNum[1])
    print(Game.level)


# ---------- START SCREEN ----------
def menu():
    # Menu screen
    print("\n---------------") # 15 dashes
    print("\nTHE SPARTAN GAMES")
    print("\n| 1. NEW GAME")
    print("| 2. LOAD GAME")
    print("| 3. PLAYER STATS")
    print("| 4. INVENTORY")
    print("| 5. INSTRUCTIONS")

    goodInput = False

    while not goodInput:
        try:
            goodInput = True
            choice = int(input("\n-> "))

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
                print("[ Please enter a valid input! ]")
                goodInput = False
        except ValueError:  # Typed in non-integers
            print("[ Please enter a valid input! ]")
            goodInput = False


if not startGame:
    instructions()
    startGame = True
    menu()