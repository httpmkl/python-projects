import random
from character import Character

class Player(Character):
    # Stats
    health = 100
    shield = 50
    energy = 100
    money = 50
    didTurn = True

    # To be accessed by enemies
    didKick = False
    didPunch = False

    # Profile
    name = 'Placeholder'

    def __init__(self):
        Player.isDead = False


    # ---------- MATCHES ----------
    def doTurn(self, skipIntro):
        gaveOptions = skipIntro

        while not gaveOptions:
            print('\nPLAYER TURN...')
            print(f'\n{Player.name}, HOW WILL YOU RESPOND?')
            # Options
            print('1. Check your stats')
            print('2. Check enemy stats')
            print('3. Attack!')
            print('4. Retreat!')
            print('5. Use a special ability/tool')
            gaveOptions = True

        # Loop for picking choices until move is made
        while gaveOptions:
            try:
                choice = int(input(''))
                gaveOptions = False
                # Redirects player to cho9ce
                if choice > 5 or choice < 1:
                    print(f'Invalid input!')
                    gaveOptions = True
                elif choice == 1:
                    # Access stats
                    print('\n--------------------')
                    print(f'{Player.name}\'s Stats:\n')
                    print(f'- Health: {Player.health}')
                    print(f'- Shield: {Player.shield}')
                    print(f'- Energy: {Player.energy}%')
                    print('--------------------')
                    gaveOptions = True
                elif choice == 2:
                    # Access enemy stats
                    print()
                    gaveOptions = True
                elif choice == 3:
                    # Physical attack
                    if Player.energy > 0:
                        self.attack()
                        Player.energy -= 10
                    else:  # Player has no energy
                        print('\n[ You can\'t attack if you have no energy! ]\n')
                        gaveOptions = True
                elif choice == 4:
                    # Cower away to regain energy
                    self.retreat()
                    Player.energy += 25
                else:  # choice == 5
                    # Access inventory
                    print()
            except ValueError:
                print('Invalid input!')



    def attack(self):
        chance = random.randint(1, 10)
        if chance <= 5:
            print(f'\n-> {Player.name} threw a ferocious punch!')
            print('DAMAGE: 10')
            Player.didPunch = True
        else:  # chance >= 6
            print(f'\n-> {Player.name} delivered a fierce kick!')
            print('DAMAGE: 10')
            Player.didKick = True

    def retreat(self):
        print(f'\n-> {Player.name} backed away')
        print('DAMAGE: 0')

    def checkIsDead(self):
        if Player.health > 0:
            Player.isDead = False
            return Player.isDead
        else:
            Player.isDead = True
            return Player.isDead


    # ---------- SETTERS ----------
    def setHealth(self, num):
        Player.health += num

        # Conditional logic to maintain health between 1-100
        if Player.health > 100:
            # To ensure health doesn't go above max
            Player.health = 100

    def setName(self, name):
        Player.name = name

    def setShield(self, num):
        Player.shield += num

        # Conditional logic to maintain shield between 1-100
        if Player.shield > 100:
            # To ensure shield doesn't go above max
            Player.shield = 100
        elif Player.shield <= 0:
            # If shield goes in the negatives, it gets taken away from health
            Player.health -= (Player.shield * -1)
            Player.shield = 0