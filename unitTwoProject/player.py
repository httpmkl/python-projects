class Character:
    # Stats
    health = 100
    shield = 0
    energy = 100
    money = 50
    isDead = False
    didTurn = True

    # Profile
    name = 'Placeholder'

    def __init__(self):
        isDead = False

    # ---------- MATCHES ----------
    def doTurn(self):
        print('\n--------------------')
        print(f'{Character.name}, HOW WILL YOU RESPOND?')
        # Options
        print('1. Check your stats')
        print('2. Check enemy stats')
        print('3. Attack!')
        print('4. Defend!')
        print('5. Use a special ability/tool')
        print('--------------------\n')
        gaveOptions = True

        # Loop for picking choices until move is made
        while gaveOptions:
            try:
                choice = int(input())
                if choice == 1:
                    print(f'{Character.health}')
                else:
                    pass
            except ValueError:
                print('Invalid input!')

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