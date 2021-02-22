'''
    Completed:
    - Created menu screen
    - Created intro game screen w/ enemy description & options
    - Set up enemy -> player -> enemy loop for matches (that checks for death)
    - Figured out how to track the status of enemies (show alive/dead in their character desc)
    - Created warrior moves
    - Figured out how to make player take damage
    - Figured out how to track and set the status of player (alive/dead)
    - Created attack/retreat/check stat methods for player
    - Created trickster moves
    - Figured out how to access the enemy class in the player class without circular import error
    - Figure out how to make enemy take damage
    - Create check enemy stats method for player
    - Created wizard moves
    - Set up tools & special abilities
    - Created functionality for the protein drink

    To-Do:
    - Create functionality for other tools
    - Figure out how to conclude the game once all enemies are dead
    - Create instructions screen
    - Give hints about the enemy throughout the battle
    - Make gameIntro controlled by only introDone (not hasItStarted)
        - Look at player class for how to do it (doTurn)
    - Make everything (esp. enemy class) more modular
    - (if time available) Implement some additional features for the gameplay & design a better UI
        - Add more descriptions and vividness during the battles

'''

# Battle Arena RPG gameIntro - made by Nora Calif
startGame = False
from player import Player
from enemy import Enemy


# Starting screen for battle
def gameIntro(trueOrFalse):
    hasItStarted = trueOrFalse
    introDone = True

    # Only shows when the game first starts
    while not hasItStarted:
        print('\n--------------------\n')
        print('NEW GAME STARTED')
        print('\n--------------------')

        # Dialogue
        print(f'\n\n-> Welcome to the Battle Arena, {player.name}!')
        print('-> Here, you face off against enemies to see who can come out victorious')
        print('-> Do you think you can survive until the end?')
        hasItStarted = True

    # Loop for showing enemy options
    while introDone:
        print('\n\nENEMIES: the Warrior, the Trickster, the Wizard')
        choice = input('[ Type in the opponent\'s name for a brief description ]\n')

        if choice == 'Warrior' or choice == 'warrior':  # Chose warrior
            warriorDesc()
        elif choice == 'Trickster' or choice == 'trickster':  # Chose trickster
            tricksterDesc()
        elif choice == 'Wizard' or choice == 'wizard':  # Chose wizard
            wizardDesc()
        else:  # They didn't type the name
            print('\n-> Invalid input!')


def warriorDesc():
    print('\n\n--------------------')
    print('\nTHE WARRIOR')
    print('\nThis one is a formidable opponent! Powerful attacks, though reluctant \n'
          'to dodge; you\'ll hardly be able to make it out alive with the Warrior!')
    print('\nType: Offense-oriented')
    print('Strongest aspect: Strength')
    print('Difficulty rating: Easy')

    war = Enemy('Warrior')
    if not war.checkIsDead():
        print('Status: ALIVE')
    else:  # Warrior is dead
        print('Status: DEAD')

    print('\n--------------------\n')

    # Choice to attack or go back
    print('\nWould you like to go back or start a match with the Warrior?')
    print('1. BACK TO OPTIONS \n2. START MATCH')
    introDone = False

    while not introDone:  # So the content below gets looped if invalid
        try:
            choice2 = int(input())
            if choice2 > 2 or choice2 < 1:
                print('Invalid input!')
            elif choice2 == 1:
                introDone = True
            else:
                print(f'\n\n[ {player.name} vs. Warrior: START ]\n')
                game('Warrior')
                break
                # Takes us to game function
        except ValueError:
            print('Invalid input!')


def tricksterDesc():
    print('\n\n--------------------')
    print('\nTHE TRICKSTER')
    print('\nA sneaky opponent, they are! You\'ll hardly be able to get an attack\n'
          'in with their sly dodges. They\'ll evade you before you can even blink!')
    print('\nType: Defense-oriented')
    print('Strongest aspect: Speed')
    print('Difficulty rating: Medium')

    trick = Enemy('Trickster')
    if not trick.checkIsDead():
        print('Status: ALIVE')
    else:  # Trickster is dead
        print('Status: DEAD')

    print('\n--------------------\n')

    # Choice to attack or go back
    print('\nWould you like to go back or start a match with the Trickster?')
    print('1. BACK TO OPTIONS \n2. START MATCH')
    introDone = False

    while not introDone:  # Looped if invalid
        try:
            choice2 = int(input())
            if choice2 > 2 or choice2 < 1:
                print('Invalid input!')
            elif choice2 == 1:
                introDone = True
            else:
                print(f'\n\n[ {player.name} vs. Trickster: START ]\n')
                game('Trickster')
                break
                # Takes us to game function
        except ValueError:
            print('Invalid input!')


def wizardDesc():
    print('\n\n--------------------')
    print('\nTHE WIZARD')
    print('\nThis enemy is certainly challenging! They watch your move, then calculates \n'
          'the best course of action from there. Better pull out your magic for this one!')
    print('\nType: Offense-oriented & defense-oriented')
    print('Strongest aspect: Intelligence')
    print('Difficulty rating: Hard')

    wiz = Enemy('Wizard')
    if not wiz.checkIsDead():
        print('Status: ALIVE')
    else:  # Wizard is dead
        print('Status: DEAD')

    print('\n--------------------\n')

    # Choice to attack or go back
    print('\nWould you like to go back or start a match with the Wizard?')
    print('1. BACK TO OPTIONS \n2. START MATCH')
    introDone = False

    while not introDone:  # Looped if invalid
        try:
            choice2 = int(input())
            if choice2 > 2 or choice2 < 1:
                print('Invalid input!')
            elif choice2 == 1:
                introDone = True
            else:
                print(f'\n\n[ {player.name} vs. Wizard: START ]\n')
                game('Wizard')
                break
                # Takes us to game function
        except ValueError:
            print('Invalid input!')


# Gameplay
def game(enemyName):
    enemy = Enemy(enemyName)

    # Creates an enemy -> player -> enemy loop for the turns
    while player.didTurn and not enemy.didTurn:  # Player just went
        enemy.doTurn(player)

        # Checks to see if player is dead after enemy's move
        if player.checkIsDead():
            print('\n--------------------')
            print(f'[ {player.name} died ] \n{enemy.name} WINS')
            print('--------------------\n')
            print('\nGAME OVER \nThank\'s for playing! \n')
            exit()  # End game when player dies
        else:
            enemy.didTurn = True
            player.didTurn = False

        while enemy.didTurn and not player.didTurn:  # Enemy just went
            player.doTurn(False, enemy)

            # Checks to see if enemy is dead after player's move
            if enemy.checkIsDead():
                print(f'[ {enemy.name} died ] \n{player.name} WINS')
                gameIntro(True)
            else:
                player.didTurn = True
                enemy.didTurn = False


# Stats
def stats():
    print('\n--------------------')
    print(f'{player.name}\'s Stats\n')

    print(f'-> Health: {player.health}')  # Shows health stat
    print(f'-> Shield: {player.shield}')  # Shows shield stat
    print(f'-> Energy: {player.energy}%')  # Shows energy stat
    print(f'\nMONEY AVAILABLE: ${player.money}')  # Show money available

    print('--------------------')
    menuScreen()


# Instructions
def instructions():
    print('Under construction')


# Menu screen
def menuScreen():
    goodInput = False

    while not goodInput:
        try:
            goodInput = True
            choice = int(input(f'\nENTER YOUR CHOICE \n-> '))

            # Redirecting based on choices
            if choice > 3 or choice < 0:  # Typed an number outside of the options
                print('\nPlease enter a valid input!')
                goodInput = False
            elif choice == 1:  # Chose stats
                stats()
            elif choice == 2:
                instructions()
            else:  # choice = 3
                gameIntro(False)
        except ValueError:  # Typed in non-integers
            print('\nPlease enter a valid input!')
            goodInput = False


# Beginning screen
if not startGame:
    print('\n~ WELCOME TO THE BATTLE ARENA ~\n')
    name = input('Enter your name: ')
    player = Player()
    player.setName(name)

    # Menu
    print('\nMENU:')
    print('1. Check Stats')
    print('2. Instructions')
    print('3. START GAME')

    startGame = True
    menuScreen()
