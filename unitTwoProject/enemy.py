import random
from player import Character


class Enemy:
    didTurn = False

    def __init__(self, name):
        self.name = name

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
    health = 100
    energy = 100
    isDead = False

    def __init__(self):
        super().__init__('Warrior')

    def doTurn(self):
        # Attacks if energy is high enough, dodges if low
        if Warrior.energy >= 15:
            Warrior.energy -= 10
            self.attack()
        else:   # Energy is below 15
            Warrior.energy += 5
            self.dodge()

    def attack(self):
        # Creates 50% chance of either action playing out
        chance = random.randint(1, 10)
        if chance <= 5:
            print('\n-> The Warrior loaded his fist and delivered a powerful blow!')
            print('DAMAGE: 15')
            player = Character()
            player.setHealth(-15)
        else:   # chance >= 6
            print('\n-> With mighty swing, the Warrior gave a strong kick!')
            print('DAMAGE: 15')
            player = Character()
            player.setHealth(-15)

    def dodge(self):
        print('-> The Warrior stood back in fear')
        print('DAMAGE: 0')


# Trickster class
class Trickster(Enemy):
    health = 100
    energy = 100
    isDead = False

    def __init__(self):
        super().__init__('Trickster')

    def doTurn(self):
        print('Trickster time')


# Wizard class
class Wizard(Enemy):
    health = 100
    energy = 100
    isDead = False

    def __init__(self):
        super().__init__('Wizard')

    def doTurn(self):
        print('Wizard time')