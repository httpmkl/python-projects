import random
from inventory import Inventory


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
            if Warrior.health <= 0:
                Warrior.isDead = True
                return Warrior.isDead
            else:
                Warrior.isDead = False
                return Warrior.isDead
        elif self.name == 'Trickster':
            if Trickster.health <= 0:
                Trickster.isDead = True
                return Trickster.isDead
            else:
                Trickster.isDead = False
        elif self.name == 'Wizard':
            if Wizard.health <= 0:
                Wizard.isDead = True
                return Wizard.isDead
            else:
                Wizard.isDead = False
        else:
            pass

    def setHealth(self, num):
        if self.name == 'Warrior':
            Warrior.health -= num
        elif self.name == 'Trickster':
            Trickster.health -= num
        elif self.name == 'Wizard':
            Wizard.health -= num
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

    def getEnergySabotage(self):
        if self.name == 'Wizard':
            return Wizard.gaveSpell
        else:
            return False

    def getHealthSabotage(self):
        if self.name == 'Wizard':
            return Wizard.gavePoison
        else:
            return False


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
            print('\n\n[ ENEMY TURN... ]')
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
                player.addShield(Warrior.damage * -1)
            else:
                player.setHealth(Warrior.damage * -1)
        else:  # chance >= 6
            print('\n-> With mighty swing, the Warrior gave a strong kick!')
            print(f'DAMAGE: {Warrior.damage}\n')
            if player.shield > 0:
                player.addShield(Warrior.damage * -1)
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
                print('\n\n[ ENEMY TURN... ]')
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
    gavePoison = False
    gaveSpell = False
    firstMove = True
    hasShield = False
    hasShieldTwo = False

    def __init__(self):
        super().__init__('Wizard')

    def doTurn(self, player):
        Wizard.damage = int(5 + (2 * Wizard.energy / 100))
        # To make sure sabotages are regulated throughout the match
        self.controlDamage(player)

        if Wizard.energy >= 15 and not Wizard.energyLow:
            print('\n[ ENEMY TURN... ]')

            if player.didKick or player.didPunch:  # They did an offensive move
                # Later change this criteria and do a didOffense move when special abilities are implemented
                self.defense(player)
                Wizard.energy -= 7
            else:  # Didn't physically attack
                self.offense(player)
                Wizard.energy -= 7

        elif Wizard.energy < 15 and not Wizard.energyLow:  # Energy is below 15
            Wizard.energyLow = True

        # Makes it so that the enemy dodges until energy is back completely
        if Wizard.energyLow:
            if Wizard.energy < 100:
                print('\n\n[ ENEMY TURN... ]')
                Enemy.retreat(self)
                Wizard.energy += 50
                if Wizard.energy > 100:
                    Wizard.energy = 100  # To ensure it's not above max
            else:  # Energy equals 100
                Wizard.energyLow = False
                self.doTurn(player)

    # Offense
    def offense(self, player):
        # Conditional logic for damage
        if Wizard.gavePoison:
            Wizard.damage = 12
        else:
            Wizard.damage = 7

        # Conditional logic for moves
        if player.health < 20:
            # Sets up a harsh but immediate attack
            self.strongAttack(player)
        else:
            # Sets up a prolonged or energy-saving attack
            self.weakAttack(player)

    def strongAttack(self, player):
        # 50% chance for either move
        chance = random.randint(1, 10)
        if chance <= 5:
            print('\n-> The Wizard summoned a grand spear and pierced it through your body!')
            print(f'DAMAGE: {Wizard.damage * 2}\n')
            player.setHealth(Wizard.damage * -2)
        else:  # chance >= 6
            print('\n-> The Wizard mustered a large gust of wind and blasted you to the ground!')
            print(f'DAMAGE: {Wizard.damage * 2}\n')
            player.setHealth(Wizard.damage * -2)

    def weakAttack(self, player):
        chance = random.randint(1, 10)
        if Wizard.firstMove:  # For the first move, the Wizard will always start with a magic attack
            Wizard.firstMove = False
            self.magicAttack(player)
        else:  # For all subsequent moves
            self.normalAttack(player)

    def normalAttack(self, player):
        # 50% chance of either move
        chance = random.randint(1, 10)
        if chance <= 5:
            # Normal
            print('\n-> The Wizard struck you with bow & arrow!')
            print(f'DAMAGE: {Wizard.damage}\n')
            player.setHealth(Wizard.damage * -1)
        else:
            # Normal
            print('\n-> The Wizard knocked you down with his staff!')
            print(f'DAMAGE: {Wizard.damage}\n')
            player.setHealth(Wizard.damage * -1)

    def magicAttack(self, player):
        # 50% chance of either move
        chance = random.randint(1, 10)
        if chance <= 5:
            # Poison
            print('\n-> The Wizard poured a special potion over your head!')
            # Takes an extra 5 damage whenever the wizard attacks
            print('DAMAGE: ?\n')
            Wizard.gavePoison = True
        else:
            # Spell
            print('\n-> The Wizard muttered a peculiar incantation!')
            # Takes an extra -5 energy whenever the player attacks
            print('DAMAGE: ?\n')
            Wizard.gaveSpell = True

    # Defense
    def defense(self, player):
        chance = random.randint(1, 10)

        if player.health < 20:
            # Regardless of the player's move, the wizard attacks if they are vulnerable
            self.strongAttack(player)
        elif Wizard.hasShield:  # The wizard set up a barrier
            self.hasShieldUp(player)
        elif chance <= 3:  # 70% chance
            # Gives player the chance to land some hits
            self.weakAttack(player)
        else:  # 70% chance
            self.dodgeAttack(player)

    def dodgeAttack(self, player):
        chance = random.randint(1, 10)

        if chance <= 8:  # 80% chance
            self.normalDefense(player)
        else:  # 20% chance
            self.magicDefense(player)

    def normalDefense(self, player):
        # Dodges attack using one of 2 moves
        if player.didKick:
            print('\n-> Too slow! The Wizard dodged your attack using the power of flight.')
            print(f'DAMAGE: 0')
            print('[ Your attack gave no damage! ]\n')
            Wizard.health += player.damage  # Restores health
            player.didKick = False
        elif player.didPunch:
            print('\n-> So close! The Wizard blocked your hit with a magical barrier.')
            print(f'DAMAGE: 0')
            print('[ Your attack gave no damage! ]\n')
            Wizard.health += player.damage  # Restores health
            player.didPunch = False

    def magicDefense(self, player):
        # Sets up a defense that'll protect them for two moves
        print('\n-> The Wizard set up a protective shield.')
        print(f'DAMAGE: 0')
        print('[ Your attack gave no damage! ]\n')
        Wizard.health += player.damage  # Restores health
        player.didKick = False
        player.didPunch = False
        Wizard.hasShield = True

    def hasShieldUp(self, player):
        if not Wizard.hasShieldTwo:  # Only used it for one turn so far
            print('\n-> Nice try! The Wizard has put up a protective shield during your previous attack')
            print(f'DAMAGE: 0')
            print('[ Your attack gave no damage! ]\n')
            Wizard.health += player.damage  # Restores health
            player.didKick = False
            player.didPunch = False
            Wizard.hasShieldTwo = True
        else:
            # So the barrier only lasts for two turns
            Wizard.hasShield = False
            Wizard.hasShieldTwo = False
            self.normalDefense(player)

    def controlDamage(self, player):
        if Wizard.gavePoison and player.health < 30:
            Wizard.gavePoison = False
        elif Wizard.gaveSpell and player.energy < 30:
            Wizard.gaveSpell = False