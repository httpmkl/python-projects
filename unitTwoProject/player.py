import random
#from enemy import Enemy

class Character:
    # Stats
    health = 100
    shield = 0
    energy = 100
    money = 50
    didTurn = True

    # Profile
    name = 'Placeholder'

    def __init__(self):
        Character.isDead = False

    # ---------- MATCHES ----------
    def doTurn(self, skipIntro):
        gaveOptions = skipIntro

        while not gaveOptions:
            print('\nPLAYER TURN...')
            print(f'\n{Character.name}, HOW WILL YOU RESPOND?')
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
            except ValueError:
                print('Invalid input!')

        if choice > 5 or choice < 1:
            print(f'Invalid input!')
        elif choice == 1:
            # Access stats
            print('\n---------------')
            print(f'{Character.name}\'s Stats:\n')
            print(f'- Health: {Character.health}')
            print(f'- Shield: {Character.shield}')
            print(f'- Energy: {Character.energy}%')
            print('---------------')
            self.doTurn(True)
        elif choice == 2:
            # Access enemy stats
            print()
        elif choice == 3:
            # Physical attack
            self.attack()
        elif choice == 4:
            # Cower away to regain energy
            self.retreat()
        else:  # choice == 5
            # Access inventory
            print()

    def attack(self):
        chance = random.randint(1, 10)
        if chance <= 5:
            print(f'\n-> {Character.name} threw a ferocious punch!')
            print('DAMAGE: 10')
        else:  # chance >= 6
            print(f'\n-> {Character.name} delivered a fierce kick!')
            print('DAMAGE: 10')

    def retreat(self):
        print(f'\n-> {Character.name} cowered away')
        print('DAMAGE: 0')

    def checkIsDead(self):
        if Character.health > 0:
            Character.isDead = False
            return Character.isDead
        else:
            Character.isDead = True
            return Character.isDead

    # ---------- SETTERS ----------
    def setHealth(self, newHealth):
        Character.health += newHealth
        # To ensure health doesn't go above max
        if Character.health > 100:
            Character.health = 100
        else:
            pass

    def addShield(self, newShield):
        Character.shield += newShield # Adds specified amount to shield

    def addEnergy(self, newEnergy):
        Character.energy += newEnergy

    def spendMoney(self, amount):
        Character.money -= amount

    def setName(self, name):
        Character.name = name