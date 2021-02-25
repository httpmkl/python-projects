class Inventory:

    # Booleans for special tools
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

    # All of the below functions are for tracking the amount of each tool used

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