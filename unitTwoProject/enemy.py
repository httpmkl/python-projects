import random
from player import Player


class Enemy:
    didTurn = False
    name = 'Placeholder'

    def __init__(self, name):
        self.name = name

    def returnName(self):
        return self.name

    def doTurn(self, player):
        # Accesses each character's turn through a single method
        if self.name == 'Warrior':
            war = Warrior()
            war.doTurn(player)
        elif self.name == 'Trickster':
            trick = Trickster()
            trick.doTurn(player)
        elif self.name == 'Wizard':
            wiz = Wizard()
            wiz.doTurn(player)
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
            Warrior.health -= num
        elif self.name == 'Trickster':
            Trickster.health -= num
        elif self.name == 'Wizard':
            Warrior.health -= num
        else:
            pass

    def retreat(self):  # Generic method for all enemies
        print(f'\n-> The {self.returnName()} stood back in fear')
        print('DAMAGE: 0\n')

    # ---------- GETTERS ----------
    def getHealth(self):
        if self.name == 'Warrior':
            return Warrior.health
        elif self.name == 'Trickster':
            return Trickster.health
        elif self.name == 'Wizard':
            return Wizard.health
        else:
            pass

    def getEnergy(self):
        if self.name == 'Warrior':
            return Warrior.energy
        elif self.name == 'Trickster':
            return Trickster.energy
        elif self.name == 'Wizard':
            return Wizard.energy
        else:
            pass


# Warrior class
class Warrior(Enemy):
    health = 100
    energy = 100
    damage = 10
    isDead = False
    energyLow = False

    def __init__(self):
        super().__init__('Warrior')

    def doTurn(self, player):
        # So the player damage degrades as the warrior loses energy
        Warrior.damage = int(3 + (7 * Warrior.energy / 100))

        # Attacks if energy is high enough, dodges if low
        if Warrior.energy >= 15 and not Warrior.energyLow:
            print('\n[ ENEMY TURN... ]')
            self.attack(player)
            Warrior.energy -= 7
        elif Warrior.energy < 15 and not Warrior.energyLow:  # Energy is below 15
            Warrior.energyLow = True

        # Makes it so that the enemy retreats until energy is back completely
        if Warrior.energyLow:
            if Warrior.energy < 100:
                print('\n[ ENEMY TURN... ]')
                Enemy.retreat(self)
                Warrior.energy += 25
                if Warrior.energy > 100:
                    Warrior.energy = 100  # To ensure it's not above max
            else:  # Energy equals 100
                Warrior.energyLow = False
                self.doTurn(player)

    def attack(self, player):
        # Creates 50% chance of either action playing out
        chance = random.randint(1, 10)
        if chance <= 5:
            print('\n-> The Warrior loaded his fist and delivered a powerful blow!')
            print(f'DAMAGE: {Warrior.damage}\n')
            # So damage gets taken on shield before health
            if player.shield > 0:
                player.setShield(Warrior.damage * -1)
            else:
                player.setHealth(Warrior.damage * -1)
        else:  # chance >= 6
            print('\n-> With mighty swing, the Warrior gave a strong kick!')
            print(f'DAMAGE: {Warrior.damage}\n')
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

    def doTurn(self, player):
        Trickster.damage = int(2 + (5 * Trickster.energy / 100))

        # To create a higher chance of a certain response
        chance = random.randint(1, 10)

        # Re-used code from Warrior section
        if Trickster.energy >= 15 and not Trickster.energyLow:
            print('\n[ ENEMY TURN... ]')

            if chance > 7:  # 30% chance of attack
                self.attack(player)
                Trickster.energy -= 10
            else:  # 70% chance of dodge
                self.dodge(player)
                Trickster.energy -= 10

        elif Trickster.energy < 15 and not Trickster.energyLow:  # Energy is below 15
            Trickster.energyLow = True

        # Makes it so that the enemy retreats until energy is back completely
        if Trickster.energyLow:
            if Trickster.energy < 100:
                print('\n[ ENEMY TURN... ]')
                Enemy.retreat(self)
                Trickster.energy += 34
                player.didKick = False
                player.didPunch = False
                # To ensure energy doesn't go above above max
                if Trickster.energy > 100:
                    Trickster.energy = 100
            else:  # Energy equals 100
                Trickster.energyLow = False
                self.doTurn(player)

    def attack(self, player):
        print('\n-> The Trickster speedily approached you and sent a harsh jab!')
        print(f'DAMAGE: {Trickster.damage}\n')
        player.setHealth(Trickster.damage * -1)

    def dodge(self, player):
        if player.didKick:
            print('\n-> Nice try! The Trickster saw through your attack and jumped over your kick.')
            print('DAMAGE: 0')
            print('[ Your attack gave no damage! ]\n')
            Trickster.health += player.damage  # Restores health
            player.didKick = False
        elif player.didPunch:
            print('\n-> Close call! The Trickster dodged your punch.')
            print('DAMAGE: 0')
            print('[ Your attack gave no damage! ]\n')
            Trickster.health += player.damage  # Restores health
            player.didPunch = False
        else:  # If the player didn't make a physical attack
            self.attack(player)


# Wizard class
class Wizard(Enemy):
    health = 100
    energy = 100
    damage = 7
    isDead = False
    energyLow = False

    '''
        - Checks player stats to figure out action
        - If they did offense, wizard does defense
        - If they did defense/retreat, wizard does offense
        - Uses spells & potions to do moves
            - Less energy spent, more lethal & gradual damage done
    
    '''

    def __init__(self):
        super().__init__('Wizard')

    def doTurn(self, player):
        if Wizard.energy >= 15 and not Wizard.energyLow:
            print('\n[ ENEMY TURN... ]')

            if player.didKick or player.didPunch: # They did an offensive move
                # Later change this criteria and do a didOffense move when special abilities are implemented
                self.defense(player5)
            else: # Didn't physically attack
                self.offense()

        elif Wizard.energy < 15 and not Wizard.energyLow:  # Energy is below 15
            Wizard.energyLow = True

        # Makes it so that the enemy dodges until energy is back completely
        if Wizard.energyLow:
            if Wizard.energy < 100:
                print('\n[ ENEMY TURN... ]')
                Enemy.retreat(self)
                Wizard.energy += 50
                if Wizard.energy > 100:
                    Wizard.energy = 100  # To ensure it's not above max
            else:  # Energy equals 100
                Wizard.energyLow = False
                self.doTurn(player)

    def offense(self):
        # Offense
        print('attack')

    def defense(self, player):
        # Defense
        print('retreat')
        player.didKick = False
        player.didPunch = False