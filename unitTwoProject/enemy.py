import random
from player import Player
from character import Character

class Enemy(Character):
    didTurn = False
    name = 'Placeholder'

    def __init__(self, name):
        self.name = name

    def returnName(self):
        return self.name

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

    def backAway(self): # Generic method for all enemies
        print(f'\n-> The {self.returnName()} stood back in fear')
        print('DAMAGE: 0')

'''
     Either offense or defense move

     If warrior; picks offense unless health is low, then picks defense
        If statements based on enemy health
      If trickster; will dodge most attacks, and occasionally attack
        High percent change of dodge, low percent for attack (random int + if statements)
    If wizard; makes a decision based on whether player did offense/defense & their stats
        If statements based on player attack (boolean) & player health

'''

# Warrior class
class Warrior(Enemy):
    health = 100
    energy = 100
    damage = 10
    isDead = False
    energyLow = False

    def __init__(self):
        super().__init__('Warrior')

    def doTurn(self):
        # So the player damage degrades as the warrior loses energy
        Warrior.damage = int(3 + (7 * Warrior.energy / 100))

        # Attacks if energy is high enough, dodges if low
        if Warrior.energy >= 15 and not Warrior.energyLow:
            print('\nENEMY TURN...')
            self.attack()
            Warrior.energy -= 7
        elif Warrior.energy < 15 and not Warrior.energyLow:   # Energy is below 15
            Warrior.energyLow = True

        # Makes it so that the enemy dodges until energy is back completely
        if Warrior.energyLow:
            if Warrior.energy <= 100:
                print('\nENEMY TURN...')
                Enemy.backAway(self)
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
            player = Player()
            # So damage gets taken on shield before health
            if player.shield > 0:
                player.setShield(Warrior.damage*-1)
            else:
                player.setHealth(Warrior.damage * -1)
        else: # chance >= 6
            print('\n-> With mighty swing, the Warrior gave a strong kick!')
            print(f'DAMAGE: {Warrior.damage}')
            player = Player()
            if player.shield > 0:
                player.setShield(Warrior.damage * -1)
            else:
                player.setHealth(Warrior.damage * -1)


# Trickster class
class Trickster(Enemy):
    health = 100
    energy = 100
    damage = 7
    isDead = False
    energyLow = False

    def __init__(self):
        super().__init__('Trickster')

    def doTurn(self):
        Trickster.damage = int(2 + (5 * Trickster.energy / 100))

        # To create a higher chance of a certain response
        chance = random.randint(1, 10)

        # Re-used code from Warrior section
        if Trickster.energy >= 15 and not Trickster.energyLow:
            print('\nENEMY TURN...')

            if chance > 7: # 30% chance of attack
                self.attack()
                Trickster.energy -= 10
            else: # 70% chance of dodge
                self.dodge()
                Trickster.energy -= 10

        elif Trickster.energy < 15 and not Trickster.energyLow:  # Energy is below 15
            Trickster.energyLow = True

        # Makes it so that the enemy dodges until energy is back completely
        if Trickster.energyLow:
            if Trickster.energy <= 100:
                print('\nENEMY TURN...')
                Enemy.backAway(self)
                Trickster.energy += 34
            else:
                Trickster.energy = 100  # To ensure it's not above max
                Trickster.energyLow = False
                self.doTurn()

    def attack(self):
        print('\n-> The Trickster speedily approached you and sent a harsh jab!')
        print(f'DAMAGE: {Trickster.damage}')
        player = Player()
        player.setHealth(Trickster.damage * -1)

    def dodge(self):
        player = Player()
        if Player.didKick:
            print('\n-> Nice try! The Trickster saw through your attack and jumped over your kick.')
            print('DAMAGE: 0')
            print('[ Your attack gave no damage! ]')
            Player.didKick = False
        elif Player.didPunch:
            print('\n-> Close call! The Trickster dodged your punch.')
            print('DAMAGE: 0')
            print('[ Your attack gave no damage! ]')
            Player.didPunch = False
        else: # If the player didn't make a physical attack
            self.attack()

# Wizard class
class Wizard(Enemy):
    health = 100
    energy = 100
    isDead = False

    def __init__(self):
        super().__init__('Wizard')

    def doTurn(self):
        print('Wizard time')