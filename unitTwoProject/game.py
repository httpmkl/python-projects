'''
    Battle Arena RPG game
    -> Made by Nora Calif

'''

startGame = False
import time
from player import Player
from enemy import Enemy


def introText():
    print('\n\n--------------------\n')
    print('NEW GAME STARTED')
    print('\n--------------------')

    # Dialogue
    print(f'\n\nWelcome to the Battle Arena, {player.name}!')
    time.sleep(1)
    print('Here, you face off against enemies to see who can come out victorious')
    time.sleep(1)
    print('Do you think you can survive until the end?')
    time.sleep(1)

# Starting screen for battle
def gameIntro(trueOrFalse):
    hasItStarted = trueOrFalse

    # So the intro text only shows before the game first starts
    while not hasItStarted:
        introText()
        hasItStarted = True

    # Loop for showing enemy options
    while hasItStarted:
        print('\n\nENEMIES: the Warrior, the Trickster, the Wizard')
        choice = input('[ Type in the opponent\'s name for a brief description ] \n-> ')

        if choice == 'Warrior' or choice == 'warrior':  # Chose warrior
            warriorDesc()
            break
        elif choice == 'Trickster' or choice == 'trickster':  # Chose trickster
            tricksterDesc()
            break
        elif choice == 'Wizard' or choice == 'wizard':  # Chose wizard
            wizardDesc()
            break
        else:  # They didn't type a proper name
            print('\nInvalid input!')

# Warrior
def warriorDesc():
    print('\n\n--------------------')
    print('\nTHE WARRIOR')
    print('\nThis one is a formidable opponent! Powerful attacks, though reluctant \n'
          'to dodge; you\'ll hardly be able to make it out alive with the Warrior!')
    print('\nType: Offense-oriented')
    print('Strongest aspect: Strength')
    print('Difficulty rating: Easy')

    # The status will update based on whether it has been defeated
    war = Enemy('Warrior')
    if not war.checkIsDead():
        print('Status: ALIVE')
    else:  # Warrior is dead
        print('Status: DEAD')

    print('\n--------------------\n')

    # Only lets a match start if it hasn't been defeated already
    if not war.checkIsDead():
        startWarriorGame()
    else:
        print('\n[ You have already defeated this enemy!]')
        gameIntro(True)


def startWarriorGame():
    # Gives the choice to attack or go back
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
                gameIntro(True)
            else:
                warriorGameIntro()
                print('\n\n--------------------')
                print(f'\n| {player.name} vs. Warrior: START |')
                print('\n--------------------\n')
                gameTip()
                time.sleep(2)
                introDone = True
                game('Warrior')  # Takes us to game function
        except ValueError:
            print('Invalid input!')

def warriorGameIntro():
    # Short text before starting game with Warrior
    print('\n\nWith a nervous gulp, you pointed at the Warrior...')
    time.sleep(1)
    print('While the crowd gasped at your decision, your opponent let out a mighty roar...')
    time.sleep(2)

# Trickster; follows the same logic as above
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

    if not trick.checkIsDead():
        startTricksterGame()
    else:
        print('[ You have already defeated this enemy!]')
        gameIntro(True)

def startTricksterGame():
    # Gives choice to attack or go back
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
                gameIntro(True)
            else:  # choice2 = 2
                tricksterGameIntro()
                print('\n\n--------------------')
                print(f'\n| {player.name} vs. Trickster: START |')
                print('\n--------------------\n')
                gameTip()
                time.sleep(2)
                introDone = True
                game('Trickster')
        except ValueError:
            print('Invalid input!')

def tricksterGameIntro():
    print('\n\nYou hesitantly looked towards the Trickster...')
    time.sleep(1)
    print('But before the crowd can even react, the opponent vanished from your sight...')
    time.sleep(2)

# Wizard; same logic as above
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

    if not wiz.checkIsDead():
        startWizardGame()
    else:
        print('[ You have already defeated this enemy!]')
        gameIntro(True)

def startWizardGame():
    # Gives the choice to attack or go back
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
                gameIntro(True)
            else:
                wizardGameIntro()
                print('\n\n--------------------')
                print(f'\n| {player.name} vs. Wizard: START |')
                print('\n--------------------\n')
                gameTip()
                time.sleep(2)
                introDone = True
                game('Wizard')
                break
                # Takes us to game function
        except ValueError:
            print('Invalid input!')

def wizardGameIntro():
    print('\n\nAs a bead of sweat trails down your face, you muttered the Wizard\'s name...')
    time.sleep(1)
    print('But the crowd couldn\'t help but show worried glances at the sound of the opponent...')
    time.sleep(2)

# Just a piece of advice for the player on their first match
def gameTip():
    if not game.gaveHint:
        print('\nTIP: Be careful with what you purchase! Try to save most of your special \n'
              'tools for when you\'re playing against harder enemies; you\'ll need it! \n')
        game.gaveHint = True

# Gameplay
def game(enemyName):
    enemy = Enemy(enemyName)
    player.resetStats()  # To make sure the player starts with max stats
    player.didTurn = True
    enemy.didTurn = False

    # Creates an enemy -> player -> enemy loop for the turns
    while player.didTurn and not enemy.didTurn:  # Player just went
        enemyTurn(enemy)

        while enemy.didTurn and not player.didTurn:  # Enemy just went
            playerTurn(enemy)

def enemyTurn(enemy):
    enemy.doTurn(player)
    # Checks to see if player is dead after enemy's move
    if player.checkIsDead():
        print('\n--------------------')
        print(f'[ {player.name} died ] \n{enemy.name} WINS')
        print('--------------------\n')
        endScreen()  # End game when player dies
    else:
        enemy.didTurn = True
        player.didTurn = False

def playerTurn(enemy):
    player.doTurn(False, enemy)
    # Checks to see if enemy is dead after player's move
    if enemy.checkIsDead():
        print('\n\n--------------------')
        print(f'[ {enemy.name} died ] \n{player.name} WINS')
        print('--------------------\n')
        checkIfGameOver()
        matchFinished()
        gameIntro(True)
    else:
        player.didTurn = True
        enemy.didTurn = False

# Shows when the player wins a match
def matchFinished():
    print('\nThe crowd erupted with praise and compliments...')
    time.sleep(1)
    print(f'Congratulations on your victory, {player.name}!')
    time.sleep(1)
    print('\n\nSETTING UP NEXT BATTLE...')
    time.sleep(2)

# Player stats
def stats():
    print('\n\n--------------------')
    print(f'{player.name}\'s Stats\n')

    print(f'-> Health: {player.health}')  # Shows health stat
    print(f'-> Shield: {player.shield}')  # Shows shield stat
    print(f'-> Energy: {player.energy}%')  # Shows energy stat
    print(f'\nMoney Available: ${player.money}')  # Show money available
    print('--------------------\n')
    menuScreen()

# Ending screen
def checkIfGameOver():
    war = Enemy('Warrior')
    trick = Enemy('Trickster')
    wiz = Enemy('Wizard')

    # If all of the enemies are dead
    if war.checkIsDead() and trick.checkIsDead() and wiz.checkIsDead():
        endScreen()

def endScreen():
    if player.checkIsDead():  # Player is dead
        enemyWinOutro()
    else:  # Enemies are dead
        playerWinOutro()

def enemyWinOutro():
    time.sleep(2)
    print('\nThe stadium fell silent at the sight of your limp body falling over...')
    time.sleep(2)
    print('You were the competitor they had the most hope for...')
    time.sleep(2)
    print('But as the paramedics removed your body from the field...')
    time.sleep(2)
    print('The crowd couldn\'t help but clap at your relentless efforts')
    time.sleep(2)
    print('\n\nThank\'s for playing!\n')
    exit()

def playerWinOutro():
    time.sleep(2)
    print('\nThe stadium erupted in cheers...')
    time.sleep(2)
    print('With a sigh of relief, you threw your fist into the air...')
    time.sleep(2)
    print('At last, you have defeated all of the opponents...')
    time.sleep(2)
    print('And finally, victory was all yours!')
    time.sleep(2)
    print('\n\nThank\'s for playing!\n')
    exit()

# Menu screen
def menuScreen():
    goodInput = False

    while not goodInput:
        try:
            goodInput = True
            choice = int(input('\nEnter your choice:\n-> '))

            # Redirecting based on choices
            if choice > 2 or choice < 1:  # Typed an number outside of the options
                print('\nPlease enter a valid input!')
                goodInput = False
            elif choice == 1:  # Chose stats
                stats()
            else:  # choice = 2
                gameIntro(False)
        except ValueError:  # Typed in non-integers
            print('\nPlease enter a valid input!')
            goodInput = False

# Beginning screen
def storyIntroPt1():
    print('\n\nThe sounds of the crowd cheering flooded your ears...')
    time.sleep(2)
    print('The harsh stream of sunlight shined down upon your frame...')
    time.sleep(2)
    print('As you stepped into the field, you noticed the sensation of sand coating your feet...')
    time.sleep(2)
    print('And through a careful inspection, a certain sign caught your attention...')
    time.sleep(2)
    print('\nThe sign read,')
    time.sleep(1)
    print('~ WELCOME TO THE BATTLE ARENA ~\n')
    time.sleep(2)

def storyIntroPt2():
    nme = player.name
    print(f'\n\nThe crowd chanted with glee, "{nme}! {nme}! {nme}!"')
    time.sleep(1)
    print('Everyone in the bleachers were excited to see what\'s to come...')
    time.sleep(2)

# Occurs first in the program
if not startGame:
    storyIntroPt1()

    name = input('\n[ Player, what is your name? ]\n-> ')
    player = Player()
    player.setName(name)

    storyIntroPt2()

    # Menu
    print('\n\nMENU:')
    print('1. Check Stats')
    print('2. START GAME')

    startGame = True
    game.gaveHint = False
    menuScreen()