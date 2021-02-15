class Enemy:
    didTurn = False

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.energy = 100

    def doTurn(self):
        # Accesses each character's turn through a single method
        if self.name == 'Warrior':
            war = Warrior()
            war.doTurn()
        elif self.name == 'Trickster':
            trick = Trickster()
            trick.doTurn()
        elif self.name == 'Wizard':
            wiz = Wizard()
            wiz.doTurn()
        else:
            pass

    def checkIsDead(self):
        # Checks if enemy is dead
        if self.name == 'Warrior':
            war = Warrior()
            return war.isDead
        elif self.name == 'Trickster':
            trick = Trickster()
            return trick.isDead
        elif self.name == 'Wizard':
            wiz = Wizard()
            return wiz.isDead
        else:
            pass

'''
     Either offense or defense move

     If warrior; picks offense unless health is low, then picks defense
        If statements based on enemy health
     If wizard; makes a decision based on whether player did offense/defense & their stats
        If statements based on player attack (boolean) & player health
     If trickster; will dodge most attacks, and occasionally attack
        High percent change of dodge, low percent for attack (random int + if statements)
'''

# Warrior class
class Warrior(Enemy):
    isDead = False

    def __init__(self):
        super().__init__('Warrior')

    def doTurn(self):
        print('Warrior time')


# Trickster class
class Trickster(Enemy):
    isDead = False

    def __init__(self):
        super().__init__('Trickster')

    def doTurn(self):
        print('Trickster time')


# Wizard class
class Wizard(Enemy):
    isDead = False

    def __init__(self):
        super().__init__('Wizard')

    def doTurn(self):
        print('Wizard time')