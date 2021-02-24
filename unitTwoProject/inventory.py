class Inventory:
    '''
        Types of items:

        1. Specialized weapons: Items that can only be accessed when playing against certain enemies
        [Work for 5 enemy turns and can be purchased 1 time]
            Spiked armour: Makes the Warrior take 10 damage when they throw a physical attack
                - You won't receive damage from the hits; only the Warrior will
            Ninja mist: Hides your movement from the Trickster
                - They'll perceive your movement as a retreat so they'll attack (w/ less damage than you)
            Cursed sabotage: Makes it so that the Wizard loses half of his intelligence
                - Accuracy depleted

        2. General tools: Items that can be accessed during any battle
            Protein drink: Increases energy to 100%
                - One-time occurrence; 2 available
            Enchanted sword: Increases damage to x2 (+ has a unique attack description!)
                - Applicable for 3 turns; 2 available
            Force field: Increases shield by 50
                - One-time occurrence; 2 available
            Medical kit: Increases health by 20
                - One-time occurrence; 2 available

    '''
    hasSkArmour = False
    hasNjMist = False
    hasCsSabotage = False
    hasProDrink = False
    hasProDrinkTwo = False
    hasEnSword = False
    hasEnSwordTwo = False
    hasFrField = False
    hasFrFieldTwo = False
    hasMedKit = False
    hasMedKitTwo = False
    hasHint = False
    hasHintTwo = False
    hasHintThree = False

    def __init__(self):
        pass

    def skArmourNum(self):
        if not Inventory.hasSkArmour:
            return 0
        else:
            return 1

    def njMistNum(self):
        if not Inventory.hasNjMist:
            return 0
        else:
            return 1

    def csSabotageNum(self):
        if not Inventory.hasCsSabotage:
            return 0
        else:
            return 1

    def proDrinkNum(self):
        if not Inventory.hasProDrink:
            return 0
        elif not Inventory.hasProDrinkTwo:
            return 1
        else:
            return 2

    def enSwordNum(self):
        if not Inventory.hasEnSword:
            return 0
        elif not Inventory.hasEnSwordTwo:
            return 1
        else:
            return 2

    def frFieldNum(self):
        if not Inventory.hasFrField:
            return 0
        elif not Inventory.hasFrFieldTwo:
            return 1
        else:
            return 2

    def medKitNum(self):
        if not Inventory.hasMedKit:
            return 0
        elif not Inventory.hasMedKitTwo:
            return 1
        else:
            return 2

    def hintNum(self):
        if not Inventory.hasHint:
            return 0
        elif not Inventory.hasHintTwo:
            return 1
        elif not Inventory.hasHintThree:
            return 2
        else:
            return 3