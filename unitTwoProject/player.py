class Character:
    # Beginning stats
    health = 100
    shield = 0
    energy = 100
    money = 50

    # Profile
    name = 'Placeholder'

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

    def setName(self, name):
        Character.name = name

    def spendMoney(self, amount):
        Character.money -= amount

    # ---------- GETTERS ----------

    def getHealth(self):
        return Character.health

    def getShield(self):
        return Character.shield

    def getEnergy(self):
        return Character.energy

    def getName(self):
        return Character.name

    def getMoney(self):
        return Character.money