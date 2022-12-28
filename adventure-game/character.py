def assign_traits(char):
    # Increases their stats based on predominant traits
    for i in range(0, len(char.traits)):
        if char.traits[i] == char.mainAtr: # 1st trait
            char.traits[i] = (5 + char.mainAmn)
        elif char.traits[i] == char.secondaryAtr: # 3rd trait
            char.traits[i] = (5 + char.secondaryAmn)
        elif char.traits[i] == char.weakAtr: # 2nd trait
            char.traits[i] = (5 + char.weakAmn)
        else: # Remaining traits
            char.traits[i] = (5 + char.baseAmn)

    # Reassigns their stat based on their order of attributes
    char.strength = char.traits[0]
    char.endurance = char.traits[1]
    char.flexibility = char.traits[2]
    char.speed = char.traits[3]
    char.intelligence = char.traits[4]
    char.mystery = char.traits[5]


# ---------- PARENT CLASS ----------
class Character:

    def __init__(self, char):
        char.strength = 0
        char.endurance = 0
        char.flexibility = 0
        char.speed = 0
        char.intelligence = 0
        char.mystery = 0
        char.traits = ['strength', 'endurance', 'flexibility', 'speed', 'intelligence', 'mystery']


# ---------- SPECIFIC CHARACTER CLASSES ----------
class Player(Character):
    # Requires user input to determine
    name = 'Placeholder'
    mainAtr = 'Placeholder'
    secondaryAtr = 'Placeholder'
    weakAtr = 'Placeholder'

    mainAmn = 3
    secondaryAmn = 2
    weakAmn = 1
    baseAmn = 0

    def __init__(self, orderTraits):
        super().__init__(Player)
        Player.name = orderTraits[0]
        Player.mainAtr = orderTraits[1]
        Player.secondaryAtr = orderTraits[2]
        Player.weakAtr = orderTraits[3]
        assign_traits(Player)


class Brute(Character):
    mainAtr = 'strength'
    secondaryAtr = 'endurance'
    weakAtr = 'speed'

    # How much their stats increase based on order
    mainAmn = 3
    secondaryAmn = 2
    weakAmn = 1
    baseAmn = 0

    def __init__(self):
        super().__init__(Brute)
        assign_traits(Brute)


class Magician(Character):
    mainAtr = 'flexibility'
    secondaryAtr = 'speed'
    weakAtr = 'mystery'

    # How much their stats increase based on order
    mainAmn = 3
    secondaryAmn = 2
    weakAmn = 1
    baseAmn = 0

    def __init__(self):
        super().__init__(Magician)
        assign_traits(Magician)


class Genius(Character):
    mainAtr = 'intelligence'
    secondaryAtr = 'mystery'
    weakAtr = 'endurance'

    # How much their stats increase based on order
    mainAmn = 3
    secondaryAmn = 2
    weakAmn = 1
    baseAmn = 0

    def __init__(self):
        super().__init__(Genius)
        assign_traits(Genius)


class Joker(Character):
    mainAtr = 'mystery'
    secondaryAtr = 'speed'
    weakAtr = 'endurance'

    # How much their stats increase based on order
    mainAmn = 3
    secondaryAmn = 2
    weakAmn = 1
    baseAmn = 0

    def __init__(self):
        super().__init__(Joker)
        assign_traits(Joker)


class Champion(Character):
    mainAtr = 'strength'
    secondaryAtr = 'flexibility'
    weakAtr = 'intelligence'

    # How much their stats increase based on order
    mainAmn = 3
    secondaryAmn = 2
    weakAmn = 1
    baseAmn = 0

    def __init__(self):
        super().__init__(Champion)
        assign_traits(Champion)


class FinalBoss(Character):
    mainAtr = 'strength'
    secondaryAtr = 'flexibility'
    weakAtr = 'intelligence'

    # How much their stats increase based on order
    mainAmn = 21
    secondaryAmn = 19
    weakAmn = 17
    baseAmn = 15

    def __init__(self):
        super().__init__(FinalBoss)
        assign_traits(FinalBoss)