import random
from player import Character

class Enemy:
    didTurn = False
    name = 'Placeholder'

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
            if war.health <= 0:
                war.isDead = True
                return war.isDead
            else:
                war.isDead = False
                return war.isDead
        elif self.name == 'Trickster':
            trick = Trickster()
            if trick.health <= 0:
                trick.isDead = True
                return trick.isDead
            else:
                trick.isDead = False
        elif self.name == 'Wizard':
            wiz = Wizard()
            if wiz.health <= 0:
                wiz.isDead = True
                return wiz.isDead
            else:
                wiz.isDead = False
        else:
            pass

    def setHealth(self, num):
        if self.name == 'Warrior':
            war = Warrior()
            war.health += num
        elif self.name == 'Trickster':
            trick = Trickster()
            trick.health += num
        elif self.name == 'Wizard':
            wiz = Wizard()
            wiz.health += num
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
    damage = 15
    isDead = False
    energyLow = False

    def __init__(self):
        super().__init__('Warrior')

    def doTurn(self):
        # So the player damage degrades as the warrior loses energy
        Warrior.damage = int(2 + (8 * Warrior.energy / 100))

        # Attacks if energy is high enough, dodges if low
        if Warrior.energy >= 15 and not Warrior.energyLow:
            print('\nENEMY TURN...')
            self.attack()
            Warrior.energy -= 7
        elif Warrior.energy < 15 and not Warrior.energyLow:   # Energy is below 15
            Warrior.energyLow = True

        # Makes it so that the warrior dodges until energy is back completely
        if Warrior.energyLow:
            if Warrior.energy <= 100:
                print('\nENEMY TURN...')
                self.dodge()
                Warrior.energy += 25
            else:
                Warrior.energy = 100 # To ensure it's not above max
                Warrior.energyLow = False
                self.doTurn()


    def attack(self):
        # Creates 50% chance of either action playing out
        chance = random.randint(1, 10)
        if chance <= 5:
            print('\n-> The Warrior loaded his fist and delivered a powerful blow!')
            print(f'DAMAGE: {Warrior.damage}')
            player = Character()
            player.setHealth(Warrior.damage*-1)
        else:   # chance >= 6
            print('\n-> With mighty swing, the Warrior gave a strong kick!')
            print(f'DAMAGE: {Warrior.damage}')
            player = Character()
            player.setHealth(Warrior.damage*-1)

    def dodge(self):
        print('\n-> The Warrior stood back in fear')
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