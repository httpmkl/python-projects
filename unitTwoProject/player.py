import random


class Player:
    # Stats
    health = 100
    shield = 0
    energy = 100
    money = 50
    damage = 7
    didTurn = True

    # To be accessed by enemies
    didKick = False
    didPunch = False

    # Profile
    name = 'Placeholder'

    def __init__(self):
        Player.isDead = False


    # ---------- MATCHES ----------
    def doTurn(self, skipIntro, enemy):
        gaveOptions = skipIntro
        Player.damage = int(5 + (2 * Player.energy / 100))

        while not gaveOptions:
            self.showOptions()
            gaveOptions = True

        # Loop for picking choices until move is made
        while gaveOptions:
            try:
                choice = int(input(''))
                gaveOptions = False
                # Redirects player to choice
                if choice > 5 or choice < 1:
                    print(f'Invalid input!')
                    gaveOptions = True
                elif choice == 1:   # Chose user stats
                    self.userStats()
                    gaveOptions = True
                elif choice == 2:  # Chose enemy stats
                    self.enemyStats(enemy)
                    gaveOptions = True
                elif choice == 3:  # Chose attack
                    self.controlAttack(enemy)
                elif choice == 4:
                    self.controlRetreat()
                else:  # choice == 5
                    self.inventory()
            except ValueError:
                print('Invalid input!')

    def showOptions(self):
        print('\n[ PLAYER TURN... ]')
        print(f'\n{Player.name}, HOW WILL YOU RESPOND?')
        # Options
        print('1. Check your stats')
        print('2. Check enemy stats')
        print('3. Attack!')
        print('4. Retreat!')
        print('5. Use a special ability/tool')

    def userStats(self):
        print('\n--------------------')
        print(f'{Player.name}\'s Stats:\n')
        print(f'- Health: {Player.health}')
        print(f'- Shield: {Player.shield}')
        print(f'- Energy: {Player.energy}%')
        print('--------------------')

    def enemyStats(self, enemy):
        print('\n--------------------')
        print(f'{enemy.name}\'s Stats:\n')
        print(f'- Health: {enemy.getHealth()}')
        print(f'- Energy: {enemy.getEnergy()}%')
        print('--------------------')

    def controlAttack(self, enemy):
        # Physical attack
        if Player.energy > 0:
            self.attack(enemy)
            Player.energy -= 10
        else:  # Player has no energy
            print('\n[ You can\'t attack if you have no energy! ]\n')
            self.doTurn(True, enemy)

    def controlRetreat(self):
        # Cower away to regain energy
        self.retreat()
        if Player.energy < 100:
            Player.energy += 20
            if Player.energy > 100:
                Player.energy = 100

    def inventory(self):
        print()

    def attack(self, enemy):
        chance = random.randint(1, 10)
        if chance <= 5:
            print(f'\n-> {Player.name} threw a ferocious punch!')
            print(f'DAMAGE: {Player.damage}\n')
            enemy.setHealth(Player.damage)
            self.didPunch = True
        else:  # chance >= 6
            print(f'\n-> {Player.name} delivered a fierce kick!')
            print(f'DAMAGE: {Player.damage}\n')
            enemy.setHealth(Player.damage)
            self.didKick = True

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