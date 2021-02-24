import random
from inventory import Inventory


class Player:
    # Stats
    health = 100
    shield = 0
    energy = 100
    money = 75
    damage = 7
    skTurn = 0
    njTurn = 0
    csTurn = 0
    enTurn = 0
    didTurn = True
    skTrackingTurns = False
    njTrackingTurns = False
    csTrackingTurns = False
    enTrackingTurns = False


    # To be accessed by enemies
    didKick = False
    didPunch = False

    # For giving hints
    gaveWarHint = False
    gaveTrickHint = False
    gaveWizHint = False

    # Profile
    name = 'Placeholder'

    def __init__(self):
        Player.isDead = False

    # ---------- MATCHES ----------
    def doTurn(self, skipIntro, enemy):
        gaveIntro = skipIntro
        Player.damage = int(5 + (2 * Player.energy / 100))

        while not gaveIntro:
            print('\n[ PLAYER TURN... ]')
            gaveIntro = True

        # Loop for picking choices until move is made
        while gaveIntro:
            try:
                self.showOptions()
                choice = int(input(''))
                gaveIntro = False
                # Redirects player to choice
                if choice > 5 or choice < 1:
                    print(f'Invalid input!')
                    gaveIntro = True
                elif choice == 1:  # Chose user stats
                    self.userStats()
                    gaveIntro = True
                elif choice == 2:  # Chose enemy stats
                    self.enemyStats(enemy)
                    gaveIntro = True
                elif choice == 3:  # Chose attack
                    self.controlAttack(enemy)
                elif choice == 4:
                    self.controlRetreat()
                else:  # choice == 5
                    self.inventory(enemy)
            except ValueError:
                print('Invalid input!')

    def showOptions(self):
        # Options
        print(f'\n{Player.name}, HOW WILL YOU RESPOND?')
        print('1. Check your stats')
        print('2. Check enemy stats')
        print('3. Attack!')
        print('4. Retreat!')
        print('5. Check inventory')

    def userStats(self):
        print('\n--------------------')
        print(f'{Player.name}\'s Stats:\n')
        print(f'- Health: {self.getHealth()}')
        print(f'- Shield: {Player.shield}')
        print(f'- Energy: {self.getEnergy()}%')
        print(f'\nMoney Available: ${Player.money}')
        print('--------------------')

    def enemyStats(self, enemy):
        print('\n--------------------')
        print(f'{enemy.name}\'s Stats:\n')
        print(f'- Health: {enemy.getHealth()}')
        print(f'- Energy: {enemy.getEnergy()}%')
        print('--------------------')

    def controlAttack(self, enemy):
        # Physical attack
        if Player.energy > 0:
            # Checks if player has enchanted sword
            if Player.enTrackingTurns:
                self.enSwordAttack(enemy)
            else:
                self.attack(enemy)
            # Checks if the wizard sabotaged the player
            if not enemy.getEnergySabotage():
                if not Player.enTrackingTurns:
                    Player.energy -= 10
            else:  # Takes an extra 5 energy if they did
                if not Player.enTrackingTurns:
                    Player.energy -= 15

        else:  # Player has no energy
            print('\n[ You can\'t attack if you have no energy! ]\n')
            self.doTurn(True, enemy)

    def attack(self, enemy):
        self.njTrackTurns(enemy)
        chance = random.randint(1, 10)
        if chance <= 5:
            print(f'\n-> {Player.name} threw a ferocious punch!')
            print(f'DAMAGE: {Player.damage}\n')
            enemy.setHealth(Player.damage)
            self.njTrackTurns(enemy)
            if not Player.njTrackingTurns:
                self.didPunch = True
        else:  # chance >= 6
            print(f'\n-> {Player.name} delivered a fierce kick!')
            print(f'DAMAGE: {Player.damage}\n')
            enemy.setHealth(Player.damage)
            self.njTrackTurns(enemy)
            if not Player.njTrackingTurns:
                self.didKick = True

    def enSwordAttack(self, enemy):
        print(f'\n-> {Player.name} plunged an enchanted sword into the enemy!')
        print(f'DAMAGE: {Player.damage * 2}\n')
        enemy.setHealth(Player.damage * 2)
        self.enTrackTurns(enemy)
        self.njTrackTurns(enemy)
        if not Player.njTrackingTurns:
            self.didPunch = True

    def controlRetreat(self):
        # Cower away to regain energy
        self.retreat()
        if Player.energy < 100:
            Player.energy += 20

    def retreat(self):
        print(f'\n-> {Player.name} backed away')
        print('DAMAGE: 0\n')
        self.didKick = False
        self.didPunch = False

    def checkIsDead(self):
        if Player.health > 0:
            Player.isDead = False
            return Player.isDead
        else:
            Player.isDead = True
            return Player.isDead

    def resetStats(self):
        # Og stats
        Player.health = 100
        Player.energy = 100
        Player.shield = 0
        Player.damage = 7
        self.didKick = False
        self.didPunch = False

    # ---------- INVENTORY ----------

    def inventory(self, enemy):
        self.didKick = False
        self.didPunch = False
        inven = Inventory()

        print('\n--------------------\n')
        print(f'{Player.name}\'s Inventory:')
        print('\nSpecialized Tools:')
        print(f'1. SPIKED ARMOUR -> {inven.skArmourNum()}/1 used')
        print(f'2. NINJA MIST -> {inven.njMistNum()}/1 used')
        print(f'3. CURSED SABOTAGE -> {inven.csSabotageNum()}/1 used')
        print('\nGeneral Tools:')
        print(f'4. PROTEIN DRINK -> {inven.proDrinkNum()}/2 used')
        print(f'5. ENCHANTED SWORD -> {inven.enSwordNum()}/2 used')
        print(f'6. FORCE FIELD -> {inven.frFieldNum()}/2 used')
        print(f'7. MEDICAL KIT -> {inven.medKitNum()}/2 used')
        print(f'8. ENEMY HINT -> {inven.hintNum()}/3 used')
        print('\n--------------------')

        self.inventoryOptions(enemy)

    def inventoryOptions(self, enemy):
        try:
            choice = input("\n-> Enter in a number to learn about the tool "
                           "or type 'BACK' to be sent to the options: ")
            # Conditional logic to redirect player to their choice
            if choice == 'BACK':
                self.doTurn(True, enemy)
            else:  # Presumably chose a number
                choice = int(choice)
                if choice > 8 or choice < 1:
                    print('Invalid input!')
                    self.inventoryOptions(enemy)
                elif choice == 1:
                    self.skArmourDesc(enemy)
                elif choice == 2:
                    self.njMistDesc(enemy)
                elif choice == 3:
                    self.csSabotageDesc(enemy)
                elif choice == 4:
                    self.proDrinkDesc(enemy)
                elif choice == 5:
                    self.enSwordDesc(enemy)
                elif choice == 6:
                    self.frFieldDesc(enemy)
                elif choice == 7:
                    self.medKitDesc(enemy)
                else:  # choice = 8
                    self.hintDesc(enemy)
        except ValueError:
            print('Invalid input!')
            self.inventoryOptions(enemy)

    # Spiked Armour
    def skArmourDesc(self, enemy):
        print('\n\n----------')
        print('\nSPIKED ARMOUR')
        print('\n-> Gives the enemy 10 damage for attacking Player')
        print('\nType: SPECIALIZED - Warrior')
        print(f'Unlocked: {self.skArmourStatus(enemy)}')
        print('Cost: $10')
        print('Length: 5 turns')
        print('\n----------\n')
        gaveDesc = True

        while gaveDesc:
            if self.skArmourStatus(enemy) == 'YES':
                try:
                    print('Would you like to purchase Spiked Armour?')
                    choice = int(input('1. YES | 2. NO \n'))
                    # To redirect back to menu or continue with the game
                    if choice > 2 or choice < 1:
                        print('Invalid input!')
                    elif choice == 1:
                        gaveDesc = False
                        self.useSkArmour(enemy)
                    else:  # choice = 2
                        gaveDesc = False
                        self.inventory(enemy)
                except ValueError:
                    print('Invalid input!')
            else:
                gaveDesc = False
                self.inventoryOptions(enemy)

    def skArmourStatus(self, enemy):
        if enemy.name == 'Warrior':
            return 'YES'
        else:
            return 'NO'

    def skTrackTurns(self, enemy):
        # Tracks 5 player turns
        if Player.skTrackingTurns:
            if Player.skTurn >= 4:
                Player.skTurn = 0
                Player.skTrackingTurns = False
            elif enemy.doTurn:
                Player.skTurn += 1
            elif Player.doTurn:
                Player.skTurn += 1

    def useSkArmour(self, enemy):
        if not Inventory.hasSkArmour:
            self.spendMoney(10)
            Player.skTrackingTurns = True
            print('')
            Inventory.hasSkArmour = True
        else:
            print('\n[ Cannot purchase item; max amount already bought! ]\n')
            self.inventory(enemy)

    # Ninja Mist
    def njMistDesc(self, enemy):
        print('\n\n----------')
        print('\nNINJA MIST')
        print('\n-> Hides your movement from the enemy')
        print('\nType: SPECIALIZED - Trickster')
        print(f'Unlocked: {self.njMistStatus(enemy)}')
        print('Cost: $10')
        print('Length: 5 turns')
        print('\n----------\n')
        gaveDesc = True

        while gaveDesc:
            if self.njMistStatus(enemy) == 'YES':
                try:
                    print('Would you like to purchase Ninja Mist?')
                    choice = int(input('1. YES | 2. NO \n'))
                    # To redirect back to options or continue with the game
                    if choice > 2 or choice < 1:
                        print('Invalid input!')
                    elif choice == 1:
                        gaveDesc = False
                        self.useNjMist(enemy)
                    else:  # choice = 2
                        gaveDesc = False
                        self.inventory(enemy)
                except ValueError:
                    print('Invalid input!')
            else:
                gaveDesc = False
                self.inventoryOptions(enemy)

    def njMistStatus(self, enemy):
        if enemy.name == 'Trickster':
            return 'YES'
        else:
            return 'NO'

    def njTrackTurns(self, enemy):
        # Tracks 5 player turns
        if Player.njTrackingTurns:
            if Player.njTurn >= 5:
                # >= 5 instead of 4 cause the first turn doesnt count
                Player.njTurn = 0
                Player.njTrackingTurns = False
            elif enemy.doTurn:
                Player.njTurn += 1
            elif Player.doTurn:
                Player.njTurn += 1

    def useNjMist(self, enemy):
        if not Inventory.hasNjMist:
            self.spendMoney(10)
            Player.njTrackingTurns = True
            print('')
            Inventory.hasNjMist = True
        else:
            print('\n[ Cannot purchase item; max amount already bought! ]\n')
            self.inventory(enemy)

    # Cursed Sabotage
    def csSabotageDesc(self, enemy):
        print('\n\n----------')
        print('\nCURSED SABOTAGE')
        print('\n-> Gives the enemy 10 damage for using magical attacks or defense')
        print('\nType: SPECIALIZED - Wizard')
        print(f'Unlocked: {self.csSabotageStatus(enemy)}')
        print('Cost: $10')
        print('Length: 5 turns')
        print('\n----------\n')
        gaveDesc = True

        while gaveDesc:
            if self.csSabotageStatus(enemy) == 'YES':
                try:
                    print('Would you like to purchase Cursed Sabotage?')
                    choice = int(input('1. YES | 2. NO \n'))
                    # To redirect back to options or continue with the game
                    if choice > 2 or choice < 1:
                        print('Invalid input!')
                    elif choice == 1:
                        gaveDesc = False
                        self.useCsSabotage(enemy)
                    else:  # choice = 2
                        gaveDesc = False
                        self.inventory(enemy)
                except ValueError:
                    print('Invalid input!')
            else:
                gaveDesc = False
                self.inventoryOptions(enemy)

    def csSabotageStatus(self, enemy):
        if enemy.name == 'Wizard':
            return 'YES'
        else:
            return 'NO'

    def csTrackTurns(self, enemy):
        # Tracks 5 player turns
        if Player.csTrackingTurns:
            if Player.csTurn >= 4:
                Player.csTurn = 0
                Player.csTrackingTurns = False
            elif enemy.doTurn:
                Player.csTurn += 1
            elif Player.doTurn:
                Player.csTurn += 1

    def useCsSabotage(self, enemy):
        if not Inventory.hasCsSabotage:
            self.spendMoney(10)
            Player.csTrackingTurns = True
            print('')
            Inventory.hasCsSabotage = True
        else:
            print('\n[ Cannot purchase item; max amount already bought! ]\n')
            self.inventory(enemy)

    # Protein Drink
    def proDrinkDesc(self, enemy):
        print('\n\n----------')
        print('\nPROTEIN DRINK')
        print('\n-> Replenishes energy to 100%')
        print('\nType: General')
        print(f'Unlocked: YES')
        print('Cost: $5')
        print('\n----------\n')
        gaveDesc = True

        while gaveDesc:
            try:
                print('Would you like to purchase Protein Drink?')
                choice = int(input('1. YES | 2. NO \n'))
                # To redirect back to options or continue with the game
                if choice > 2 or choice < 1:
                    print('Invalid input!')
                elif choice == 1:
                    gaveDesc = False
                    self.useProDrink(enemy)
                else:  # choice = 2
                    gaveDesc = False
                    self.inventory(enemy)
            except ValueError:
                print('Invalid input!')

    def useProDrink(self, enemy):
        # Sets energy to 100 for player
        if not Inventory.hasProDrink:
            self.spendMoney(5)
            Player.energy = 100
            print('')  # Empty space for layout
            Inventory.hasProDrink = True
        elif not Inventory.hasProDrinkTwo:
            self.spendMoney(5)
            Player.energy = 100
            print('')
            Inventory.hasProDrinkTwo = True
        else:
            print('\n[ Cannot purchase item; max amount already bought! ]\n')
            self.inventory(enemy)

    # Enchanted Sword
    def enSwordDesc(self, enemy):
        print('\n\n----------')
        print('\nENCHANTED SWORD')
        print('\n-> Increases damage on enemy to x2 its amount')
        print('\nType: General')
        print(f'Unlocked: YES')
        print('Cost: $5')
        print('Length: 3 turns')
        print('\n----------\n')
        gaveDesc = True

        while gaveDesc:
            try:
                print('Would you like to purchase Enchanted Sword?')
                choice = int(input('1. YES | 2. NO \n'))
                # To redirect back to options or continue with the game
                if choice > 2 or choice < 1:
                    print('Invalid input!')
                elif choice == 1:
                    gaveDesc = False
                    self.useEnSword(enemy)
                else:  # choice = 2
                    gaveDesc = False
                    self.inventory(enemy)
            except ValueError:
                print('Invalid input!')

    def enTrackTurns(self, enemy):
        # Tracks 3 player turns
        if Player.enTrackingTurns:
            if Player.enTurn >= 2:
                Player.enTurn = 0
                Player.enTrackingTurns = False
            elif enemy.doTurn:
                Player.enTurn += 1
            elif Player.doTurn:
                Player.enTurn += 1

    def useEnSword(self, enemy):
        # Gives enchanted sword to player
        if not Inventory.hasEnSword:
            self.spendMoney(5)
            Player.enTrackingTurns = True
            print('')
            Inventory.hasEnSword = True
        elif not Inventory.hasEnSwordTwo:
            self.spendMoney(5)
            Player.enTrackingTurns = True
            print('')
            Inventory.hasEnSwordTwo = True
        else:
            print('\n[ Cannot purchase item; max amount already bought! ]\n')
            self.inventory(enemy)

    # Force Field
    def frFieldDesc(self, enemy):
        print('\n\n----------')
        print('\nFORCE FIELD')
        print('\n-> Adds 50 to shield')
        print('\nType: General')
        print(f'Unlocked: YES')
        print('Cost: $5')
        print('\n----------\n')
        gaveDesc = True

        while gaveDesc:
            try:
                print('Would you like to purchase Force Field?')
                choice = int(input('1. YES | 2. NO \n'))
                # To redirect back to options or continue with the game
                if choice > 2 or choice < 1:
                    print('Invalid input!')
                elif choice == 1:
                    gaveDesc = False
                    self.useFrField(enemy)
                else:  # choice = 2
                    gaveDesc = False
                    self.inventory(enemy)
            except ValueError:
                print('Invalid input!')

    def useFrField(self, enemy):
        # Adds 50 shield to player
        if not Inventory.hasFrField:
            self.spendMoney(5)
            self.setShield(50)
            print('')
            Inventory.hasFrField = True
        elif not Inventory.hasFrFieldTwo:
            self.spendMoney(5)
            self.setShield(50)
            print('')
            Inventory.hasFrFieldTwo = True
        else:
            print('\n[ Cannot purchase item; max amount already bought! ]\n')
            self.inventory(enemy)

    # Medical Kit
    def medKitDesc(self, enemy):
        print('\n\n----------')
        print('\nMEDICAL KIT')
        print('\n-> Increases player health by 20')
        print('\nType: General')
        print(f'Unlocked: YES')
        print('Cost: $5')
        print('\n----------\n')
        gaveDesc = True

        while gaveDesc:
            try:
                print('Would you like to purchase Medical Kit?')
                choice = int(input('1. YES | 2. NO \n'))
                # To redirect back to options or continue with the game
                if choice > 2 or choice < 1:
                    print('Invalid input!')
                elif choice == 1:
                    gaveDesc = False
                    self.useMedKit(enemy)
                else:  # choice = 2
                    gaveDesc = False
                    self.inventory(enemy)
            except ValueError:
                print('Invalid input!')

    def useMedKit(self, enemy):
        # Adds 20 health to player
        if not Inventory.hasMedKit:
            self.spendMoney(5)
            self.setHealth(20)
            print('')
            Inventory.hasMedKit = True
        elif not Inventory.hasMedKitTwo:
            self.spendMoney(5)
            self.setHealth(20)
            print('')
            Inventory.hasMedKitTwo = True
        else:
            print('\n[ Cannot purchase item; max amount already bought! ]\n')
            self.inventory(enemy)

    def hintDesc(self, enemy):
        print('\n\n----------')
        print('\nENEMY HINT')
        print('\n-> Provides a clue about the playing style of the enemy')
        print('\nType: General')
        print(f'Unlocked: YES')
        print('Cost: $3')
        print('\n----------\n')
        gaveDesc = True

        while gaveDesc:
            try:
                print('Would you like to purchase Enemy Hint?')
                choice = int(input('1. YES | 2. NO \n'))
                # To redirect back to options or continue with the game
                if choice > 2 or choice < 1:
                    print('Invalid input!')
                elif choice == 1:
                    gaveDesc = False
                    self.giveHint(enemy)
                else:  # choice = 2
                    gaveDesc = False
                    self.inventory(enemy)
            except ValueError:
                print('Invalid input!')

    def giveHint(self, enemy):
        # Check enemy name to figure out which hint to give
        if enemy.returnName() == 'Warrior':
            # Warrior hint
            self.checkWarHint(enemy)
        elif enemy.returnName() == 'Trickster':
            # Trickster hint
            self.checkTrickHint(enemy)
        elif enemy.returnName() == 'Wizard':
            # Wizard hint
            self.checkWizHint(enemy)
        else:
            pass

    def checkWarHint(self, enemy):
        if not Player.gaveWarHint:  # To make sure only one hint is given for this enemy
            if not Inventory.hasHint:
                self.warHint()
                Inventory.hasHint = True
            elif not Inventory.hasHintTwo:
                self.warHint()
                Inventory.hasHintTwo = True
            elif not Inventory.hasHintThree:
                self.warHint()
                Inventory.hasHintThree = True
            else:  # To make sure 3+ hints haven't been given (this state can't really be reached in the program)
                print('\n[ Cannot purchase item; hint has already been given for this enemy! ]\n')
                self.inventoryOptions(enemy)  # Redirects back to inventory)
        else:
            print('\n[ Cannot purchase item; hint has already been given for this enemy! ]\n')
            self.inventoryOptions(enemy)

    def warHint(self):
        self.spendMoney(3)
        print('\nEnemy hint:')
        print("-> [ The Warrior will always attack until they're low on energy; then, they retreat,"
              "\nand they might find themselves vulnerable to receiving physical attacks... ]\n")
        Player.gaveWarHint = True

    def checkTrickHint(self, enemy):
        # Same logic as checkWarHint
        if not Player.gaveTrickHint:
            if not Inventory.hasHint:
                self.trickHint()
                Inventory.hasHint = True
            elif not Inventory.hasHintTwo:
                self.trickHint()
                Inventory.hasHintTwo = True
            elif not Inventory.hasHintThree:
                self.trickHint()
                Inventory.hasHintThree = True
            else:
                print('\n[ Cannot purchase item; hint has already been given for this enemy! ]\n')
                self.inventoryOptions(enemy)
        else:
            print('\n[ Cannot purchase item; hint has already been given for this enemy! ]\n')
            self.inventoryOptions(enemy)

    def trickHint(self):
        self.spendMoney(3)
        print('\nEnemy hint:')
        print("-> [ There's a high, but not total, chance of the trickster dodging you, so perhaps"
              "\nit would be wise to save your powerful attacks for when they can't detect it... ]\n")
        Player.gaveTrickHint = True

    def checkWizHint(self, enemy):
        # Same logic as checkWarHint
        if not Player.gaveWizHint:
            if not Inventory.hasHint:
                self.wizHint()
                Inventory.hasHint = True
            elif not Inventory.hasHintTwo:
                self.wizHint()
                Inventory.hasHintTwo = True
            elif not Inventory.hasHintThree:
                self.wizHint()
                Inventory.hasHintThree = True
            else:
                print('\n[ Cannot purchase item; hint has already been given for this enemy! ]\n')
                self.inventory(enemy)
        else:
            print('\n[ Cannot purchase item; hint has already been given for this enemy! ]\n')
            self.inventory(enemy)

    def wizHint(self):
        self.spendMoney(3)
        print('\nEnemy hint:')
        print("-> [ The Wizard is extremely intelligent and calculative in formulating attacks,"
              "\nso by getting them disoriented, you might be able to inflict some damage ]\n")
        Player.gaveWizHint = True

    # ---------- SETTERS ----------

    def setHealth(self, num):
        Player.health += num

    def setName(self, name):
        Player.name = name

    def setShield(self, num):
        Player.shield += num

        # Conditional logic to maintain shield between 1-100
        if Player.shield > 100:
            # To ensure shield doesn't go above max
            Player.shield = 100
        elif Player.shield <= 0:
            # If shield goes in the negatives, it gets taken away from health
            Player.health -= (Player.shield * -1)
            Player.shield = 0

    def spendMoney(self, num):
        if Player.money > 0:
            Player.money -= num
            if Player.money < 0:
                Player.money += num
                print('\n[ Cannot purchase item; not enough money! ]\n')
        else:
            print('\n[ Cannot purchase item; not enough money! ]\n')

    # ---------- GETTERS ----------

    def getEnergy(self):
        # Conditional logic to ensure energy stays between 1-100
        if Player.energy > 100:
            Player.energy = 100
            return Player.energy
        elif Player.energy < 0:
            Player.energy = 0
            return Player.energy
        else:  # Energy is within 1-100
            return Player.energy

    def getHealth(self):
        # Conditional logic to maintain health between 1-100
        if Player.health > 100:
            # To ensure health doesn't go above max
            Player.health = 100
            return Player.health
        elif Player.health < 0:
            Player.health = 0
            return Player.health
        else:
            return Player.health
