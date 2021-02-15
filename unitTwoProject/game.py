'''
    Completed:
    - Created menu screen
    - Created intro game screen w/ enemy description & options
    - Set up enemy -> player -> enemy loop for matches (that checks for death)
    - Figured out how to set the status of enemies (show alive/dead in their character desc)

    To-Do:
    - Create enemy moves
    - Create player moves
    - Figure out how to acquire/buy items + the inventory on the menu screen
    - Figure out how to conclude the game once all enemies are dead

'''


# Battle Arena RPG gameIntro - made by Nora Calif
startGame = False
from player import Character
from enemy import Enemy


# Starting screen for battle
def gameIntro(trueOrFalse):
    hasItStarted = trueOrFalse
    introDone = True

    # Only shows when the game first starts
    while not hasItStarted:
        print('\n--------------------\n')
        print('NEW GAME STARTED')

        # Dialogue
        print(f'\nWelcome to the Battle Arena, {player.name}!')
        print('Here, you face off against enemies to see who can come out victorious')
        print('Do you think you can survive until the end?')
        hasItStarted = True

    # Loop for showing enemy options
    while introDone:
        print('\nENEMIES: the Warrior, the Trickster, the Wizard')
        choice = input('-> Type in the opponent\'s name for a brief description \n')

        if choice == 'Warrior' or choice == 'warrior':  # Chose warrior
            # Warrior desc
            print('\n----------')
            print('\nTHE WARRIOR')
            print('\nThis one is a formidable opponent! Powerful attacks, though reluctant \n'
                  'to dodge; you\'ll hardly be able to make it out alive with the Warrior!')
            print('\nType: Offense-oriented')
            print('Strongest aspect: Strength')
            print('Difficulty rating: Easy')

            war = Enemy('Warrior')
            if not war.checkIsDead():
                print('Status: ALIVE')
            else: # Warrior is dead
                print('Status: DEAD')

            print('\n----------')

            # Choice to attack or go back
            print('\nWould you like to go back or start a match with the Warrior?')
            print('1. Go back \n2. Start match')
            introDone = False

            while not introDone:  # So the content below gets looped if invalid
                try:
                    choice2 = int(input())
                    if choice2 > 2 or choice2 < 1:
                        print('Invalid input!')
                    elif choice2 == 1:
                        introDone = True
                    else:
                        print(f'\n[ {player.name} vs. Warrior: START ]')
                        game('Warrior')
                        break
                        # Takes us to game function
                except ValueError:
                    print('Invalid input!')
        elif choice == 'Trickster' or choice == 'trickster':  # Chose trickster
            # Trickster desc
            print('\n----------')
            print('\nTHE TRICKSTER')
            print('\nA sneaky opponent they are! You\'ll hardly be able to get an attack\n'
                  'in with their sly dodges. They\'ll evade you before you can even blink!')
            print('\nType: Defense-oriented')
            print('Strongest aspect: Speed')
            print('Difficulty rating: Medium')

            trick = Enemy('Trickster')
            if not trick.checkIsDead():
                print('Status: ALIVE')
            else:  # Trickster is dead
                print('Status: DEAD')

            print('\n----------')

            # Choice to attack or go back
            print('\nWould you like to go back or start a match with the Trickster?')
            print('1. Go back \n2. Start match')
            introDone = False

            while not introDone:  # Looped if invalid
                try:
                    choice2 = int(input())
                    if choice2 > 2 or choice2 < 1:
                        print('Invalid input!')
                    elif choice2 == 1:
                        introDone = True
                    else:
                        print(f'\n[ {player.name} vs. Trickster: START ]')
                        game('Trickster')
                        break
                        # Takes us to game function
                except ValueError:
                    print('Invalid input!')
        elif choice == 'Wizard' or choice == 'wizard':  # Chose wizard
            # Wizard desc
            print('\n----------')
            print('\nTHE WIZARD')
            print('\nThis one is certainly challenging! They watch your move, then calculates \n'
                  'the best course of action from there. How can you possibly defeat them?')
            print('\nType: Offense-oriented & defense-oriented')
            print('Strongest aspect: Intelligence')
            print('Difficulty rating: Hard')

            wiz = Enemy('Wizard')
            if not wiz.checkIsDead():
                print('Status: ALIVE')
            else:  # Wizard is dead
                print('Status: DEAD')

            print('\n----------')

            # Choice to attack or go back
            print('\nWould you like to go back or start a match with the Wizard?')
            print('1. Go back \n2. Start match')
            introDone = False

            while not introDone:  # Looped if invalid
                try:
                    choice2 = int(input())
                    if choice2 > 2 or choice2 < 1:
                        print('Invalid input!')
                    elif choice2 == 1:
                        introDone = True
                    else:
                        print(f'\n[ {player.name} vs. Wizard: START ]')
                        game('Wizard')
                        break
                        # Takes us to game function
                except ValueError:
                    print('Invalid input!')
        else:  # They didn't type the name
            print('\nInvalid input!')


# Gameplay
def game(enemyName):
    enemy = Enemy(enemyName)

    # Creates an enemy -> player -> enemy loop for the turns
    while player.didTurn and not enemy.didTurn: # Player just went
        enemy.doTurn()

        # Checks to see if player is dead after enemy's move
        if player.isDead:
            print(f'[ {player.name} died ] \nGAME OVER')
            gameIntro(True)
        else:
            enemy.didTurn = True
            player.didTurn = False

        while enemy.didTurn and not player.didTurn: # Enemy just went
            player.doTurn()

            # Checks to see if enemy is dead after player's move
            if enemy.checkIsDead():
                print(f'[ {enemy.name} died ] \nGAME OVER')
                gameIntro(True)
            else:
                player.didTurn = True
                enemy.didTurn = False


# Inventory
def inventory():
    print('\n---------------')
    print('Inventory\n')

    print('Under Construction')

    print('---------------')
    menuScreen(True)  # Loops back to ask what they want to do


# Stats
def stats():
    print('\n---------------')
    print(f'{player.name}\'s Stats\n')

    print(f'-> Health: {player.health}')  # Shows health stat
    print(f'-> Shield: {player.shield}')  # Shows shield stat
    print(f'-> Energy: {player.energy}%')  # Shows energy stat
    print(f'\nMONEY AVAILABLE: ${player.money}')  # Show money available

    print('---------------')
    menuScreen(True)


# Menu screen
def menuScreen(trueOrFalse):
    hasItStarted = trueOrFalse
    goodInput = False

    while not goodInput:
        try:
            goodInput = True

            # To tell whether this is the program's first run or not
            if not hasItStarted:  # First run
                choice = int(input(f'\nWhat would you like to start with, {player.name}? \n-> '))
            else:  # Not first run
                choice = int(input(f'\nWhat would you like to do next, {player.name}? \n-> '))

            # Redirecting based on choices
            if choice > 3 or choice < 0:  # Typed an number outside of the options
                print('\nPlease enter a valid input!')
                goodInput = False
            elif choice == 1:  # Chose inventory
                hasItStarted = True
                inventory()
            elif choice == 2:  # Chose stats
                hasItStarted = True
                stats()
            else:  # Chose gameIntro
                hasItStarted = True
                gameIntro(False)
        except ValueError:  # Typed in non-integers
            print('\nPlease enter a valid input!')
            goodInput = False


# Beginning screen
if not startGame:
    print('\n~ WELCOME TO THE BATTLE ARENA ~\n')
    name = input('Enter your name: ')
    player = Character(name)

    # Menu
    print('\nMENU:')
    print('1. Open Inventory')
    print('2. Check Stats')
    print('3. START GAME')

    startGame = True
    menuScreen(False)