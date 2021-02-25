import random


class Enemy:
    name = 'Placeholder'
    turnText = '...ENEMY TURN...'

    def __init__(self, name):
        Enemy.name = name

    def returnName(self):
        return Enemy.name

    def doTurn(self, player):
        # Accesses each character's turn through this single method
        if Enemy.name == 'Warrior':
            war = Warrior()
            war.doTurn(player)
        elif Enemy.name == 'Trickster':
            trick = Trickster()
            trick.doTurn(player)
        elif Enemy.name == 'Wizard':
            wiz = Wizard()
            wiz.doTurn(player)
        else:
            pass

    def checkIsDead(self):
        # Checks if enemy is dead
        if Enemy.name == 'Warrior':
            if Warrior.health <= 0:
                Warrior.isDead = True
                return Warrior.isDead
            else:
                Warrior.isDead = False
                return Warrior.isDead
        elif Enemy.name == 'Trickster':
            if Trickster.health <= 0:
                Trickster.isDead = True
                return Trickster.isDead
            else:
                Trickster.isDead = False
        elif Enemy.name == 'Wizard':
            if Wizard.health <= 0:
                Wizard.isDead = True
                return Wizard.isDead
            else:
                Wizard.isDead = False
        else:
            pass

    # So player is able to decrease enemy health
    def setHealth(self, num):
        if Enemy.name == 'Warrior':
            Warrior.health -= num
        elif Enemy.name == 'Trickster':
            Trickster.health -= num
        elif Enemy.name == 'Wizard':
            Wizard.health -= num
        else:
            pass

    def retreat(self):  # Generic method for all enemies
        print(f'\n-> The {self.returnName()} stood back in fear')
        print('DAMAGE: 0\n')

    # ---------- GETTERS ----------
    def getHealth(self):
        if Enemy.name == 'Warrior':
            return Warrior.health
        elif Enemy.name == 'Trickster':
            return Trickster.health
        elif Enemy.name == 'Wizard':
            return Wizard.health
        else:
            pass

    def getEnergy(self):
        if Enemy.name == 'Warrior':
            return Warrior.energy
        elif Enemy.name == 'Trickster':
            return Trickster.energy
        elif Enemy.name == 'Wizard':
            return Wizard.energy
        else:
            pass

    def getEnergySabotage(self):
        if Enemy.name == 'Wizard':
            return Wizard.gaveSpell
        else:
            return False

    def getHealthSabotage(self):
        if Enemy.name == 'Wizard':
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
        # So the damage degrades as the warrior loses energy
        Warrior.damage = int(3 + (7 * Warrior.energy / 100))

        # Attacks if energy is high enough, dodges if low
        if Warrior.energy >= 15 and not Warrior.energyLow:
            print(f'\n{Enemy.turnText}')
            self.controlAttack(player)
            Warrior.energy -= 7
        elif Warrior.energy < 15 and not Warrior.energyLow:  # Energy is below 15
            Warrior.energyLow = True

        self.checkEnergyLow(player)

    def checkEnergyLow(self, player):
        # Makes it so that the enemy retreats until energy is back completely
        if Warrior.energyLow:
            if Warrior.energy < 100:
                print(f'\n{Enemy.turnText}')
                Enemy.retreat(self)
                Warrior.energy += 25
                if Warrior.energy > 100:
                    Warrior.energy = 100  # To ensure it's not above max
            else:  # Energy equals 100
                Warrior.energyLow = False
                self.doTurn(player)

    def controlAttack(self, player):
        if player.skTrackingTurns:  # If Spiked Armour is enabled
            self.failAttack(player)
        else:
            self.attack(player)

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

    def failAttack(self, player):
        num = Warrior.damage - 10
        # Takes away health for attacking
        chance = random.randint(1, 10)
        if chance <= 5:
            print('\n-> The Warrior loaded his fist and delivered a powerful blow!')
            print(f'DAMAGE: {num}')
            print('[ The Warrior took 10 damage for attacking you! ]\n')
            if num < 0:  # If damage - 10 is negative, enemy takes damage
                player.skTrackTurns(self)
                Enemy.setHealth(self, num * -1)
            else:  # If damage - 10 is positive, player takes damage
                if player.shield > 0:
                    player.setShield(num)
                else:
                    player.setHealth(num)
        else:  # chance >= 6
            print('\n-> With mighty swing, the Warrior gave a strong kick!')
            print(f'DAMAGE: {num}')
            print('[ The Warrior took 10 damage for attacking you! ]\n')
            if num < 0:  # If damage - 10 is negative, enemy takes damage
                player.skTrackTurns(self)
                Enemy.setHealth(self, num * -1)
            else:  # If damage - 10 is positive, player takes damage
                if player.shield > 0:
                    player.setShield(num)
                else:
                    player.setHealth(num)


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
            print(f'\n{Enemy.turnText}')

            if chance > 7:  # 30% chance of attack
                self.attack(player)
                Trickster.energy -= 10
            else:  # 70% chance of dodge
                self.dodge(player)
                Trickster.energy -= 10

        elif Trickster.energy < 15 and not Trickster.energyLow:  # Energy is below 15
            Trickster.energyLow = True

        self.checkEnergyLow(player)

    def checkEnergyLow(self, player):
        # Makes it so that the enemy retreats until energy is back completely
        if Trickster.energyLow:
            if Trickster.energy < 100:
                print(f'\n{Enemy.turnText}')
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
        if player.shield > 0:
            player.setShield(Trickster.damage * -1)
        else:
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
    chanceNum = 0
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
            print(f'\n{Enemy.turnText}')
            self.pickAttack(player)  # How the wizard attacks/defense
        elif Wizard.energy < 15 and not Wizard.energyLow:  # Energy is below 15
            Wizard.energyLow = True

        self.checkEnergyLow(player)

    def checkEnergyLow(self, player):
        # Makes it so that the enemy dodges until energy is back completely
        if Wizard.energyLow:
            if Wizard.energy < 100:
                print(f'\n{Enemy.turnText}')
                Enemy.retreat(self)
                Wizard.energy += 50
                if Wizard.energy > 100:
                    Wizard.energy = 100  # To ensure it's not above max
            else:  # Energy equals 100
                Wizard.energyLow = False
                self.doTurn(player)

    def pickAttack(self, player):
        # To deteriorate the accuracy with Cursed Sabotage
        player.csTrackTurns(self)
        if player.csTrackingTurns:
            Wizard.chanceNum = 7  # 30% chance of calculating an appropriate attack/defense
        else:  # Cursed Sabotage is NOT enable
            Wizard.chanceNum = 0  # 100% chance of calculating an appropriate attack/defense

        chance = random.randint(1, 10)
        if chance > Wizard.chanceNum:
            if player.didKick or player.didPunch:  # Player did an offensive move
                self.defense(player)
            else:  # Didn't physically attack
                self.offense(player)
        else:  # This will only be accessed if Cursed Sabotage is enabled
            self.disoriented(player)

    # Offense
    def offense(self, player):
        # Conditional logic for damage
        if Wizard.gavePoison:
            Wizard.damage = 12
        else:
            Wizard.damage = 7

        # Conditional logic for moves
        if player.health < 20:
            # Sets up a harsh but immediate attack if player is vulnerable
            self.strongAttack(player)
            Wizard.energy -= 15
        else:
            # Sets up a prolonged or energy-saving attack
            self.weakAttack(player)
            Wizard.energy -= 7

    def strongAttack(self, player):
        # 50% chance for either move
        chance = random.randint(1, 10)
        if chance <= 5:
            print('\n-> The Wizard summoned a grand spear and pierced it through your body!')
            print(f'DAMAGE: {Wizard.damage * 2}\n')
            if player.shield > 0:
                player.setShield(Wizard.damage * -2)
            else:
                player.setHealth(Wizard.damage * -2)
        else:  # chance >= 6
            print('\n-> The Wizard mustered a large gust of wind and blasted you to the ground!')
            print(f'DAMAGE: {Wizard.damage * 2}\n')
            if player.shield > 0:
                player.setShield(Wizard.damage * -2)
            else:
                player.setHealth(Wizard.damage * -2)

    def weakAttack(self, player):
        chance = random.randint(1, 10)
        if Wizard.firstMove:  # For the first move, the Wizard will always start with a magic attack
            Wizard.firstMove = False
            self.magicAttack(player)
            Wizard.usedMagic = True
        else:  # For all subsequent moves
            self.normalAttack(player)

    def normalAttack(self, player):
        # 50% chance of either move
        chance = random.randint(1, 10)
        if chance <= 5:
            print('\n-> The Wizard struck you with bow & arrow!')
            print(f'DAMAGE: {Wizard.damage}\n')
            if player.shield > 0:
                player.setShield(Wizard.damage * -1)
            else:
                player.setHealth(Wizard.damage * -1)
        else:
            print('\n-> The Wizard knocked you down with his staff!')
            print(f'DAMAGE: {Wizard.damage}\n')
            if player.shield > 0:
                player.setShield(Wizard.damage * -1)
            else:
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
            # Takes an extra 5 energy from player when they attack
            print('DAMAGE: ?\n')
            Wizard.gaveSpell = True

    # Defense
    def defense(self, player):
        chance = random.randint(1, 10)

        if player.health < 20:
            # Regardless of the player's move, the wizard attacks if they are vulnerable
            self.strongAttack(player)
            Wizard.energy -= 15
        elif Wizard.hasShield:  # The wizard set up a barrier
            self.hasShieldUp(player)
        else:
            self.dodgeAttack(player)
            Wizard.energy -= 7

    def dodgeAttack(self, player):
        chance = random.randint(1, 10)

        if chance <= 8:  # 80% chance
            self.normalDefense(player)
        else:  # 20% chance
            self.magicDefense(player)

    def normalDefense(self, player):
        # Dodges attack using one of 2 moves
        chance = random.randint(1, 2)
        if chance == 1:
            print('\n-> Too slow! The Wizard dodged your attack using the power of flight.')
            print(f'DAMAGE: 0')
            print('[ Your attack gave no damage! ]\n')
            Wizard.health += player.damage  # Restores health
            player.didKick = False
        else:  # chance = 2; 50% likelihood
            # Sort of an attack, gives the player a chance to land hits
            if player.didKick:
                print('\n-> The Wizard held up his blade and slashed your foot!')
                print(f'DAMAGE: {Wizard.damage}')
                print('[ Your attack damage was cut in half! ]\n')
                Wizard.health += int(player.damage/2)  # Restores half health
                if player.shield > 0:
                    player.setShield(Wizard.damage * -1)
                else:
                    player.setHealth(Wizard.damage * -1)
            elif player.didPunch:
                print('\n-> The Wizard blocked your punch with his blade!')
                print(f'DAMAGE: {Wizard.damage}')
                print('[ Your attack damage was cut in half! ]\n')
                Wizard.health += int(player.damage / 2)
                if player.shield > 0:
                    player.setShield(Wizard.damage * -1)
                else:
                    player.setHealth(Wizard.damage * -1)

    def magicDefense(self, player):
        # Sets up a defense that'll protect them for two moves
        print('\n-> The Wizard set up a protective shield.')
        print(f'DAMAGE: 0')
        print('[ Your attack gave no damage! ]\n')
        Wizard.health += player.damage  # Restores health
        player.didKick = False
        player.didPunch = False
        Wizard.hasShield = True

    # If the Wizard put up a shield (magic defense) the round before
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

    # Disoriented attack (nothing happens)
    def disoriented(self, player):
        print('\n-> The Wizard walked in circles. They seem a bit confused.')
        print(f'DAMAGE: 0\n')

    def controlDamage(self, player):
        # So the potion/spell in the first round stops working when the player reaches 30 health
        if Wizard.gavePoison and player.health < 30:
            Wizard.gavePoison = False
        elif Wizard.gaveSpell and player.energy < 30:
            Wizard.gaveSpell = False