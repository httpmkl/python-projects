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

    def __init__(self, name):
        Character.name = name

    # ---------- MATCHES ----------
    def doTurn(self):
        print('--------------------')
        print('PLAYER, HOW WILL YOU RESPOND?')

        print('1. Check your stats')
        print('2. Check enemy stats')
        print('3. Attack!')
        print('4. Defend!')
        print('4. Use a special ability/tool')

        print('--------------------')

    # ---------- SETTERS ----------
    def addHealth(self, newHealth):
        if Character.health < 100:
            Character.health += newHealth # Adds specified amount to health
            if Character.health > 100: # New health takes it past 100
                print('MAX HEALTH ACHIEVED')
            else:
                pass
        else: # Health at is already max
            print('New health cannot be added; you are at your max!')

    def addShield(self, newShield):
        Character.shield += newShield # Adds specified amount to shield

    def addEnergy(self, newEnergy):
        Character.energy += newEnergy

    def spendMoney(self, amount):
        Character.money -= amount