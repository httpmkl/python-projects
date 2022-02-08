def assign_traits(enemy):
    # Increases their stats based on predominant traits
    for i in range(0, len(enemy.traits)):
        if enemy.traits[i] == enemy.mainAtr: # 1st trait
            enemy.traits[i] = (5 + enemy.mainAmn)
        elif enemy.traits[i] == enemy.secondaryAtr: # 3rd trait
            enemy.traits[i] = (5 + enemy.secondaryAmn)
        elif enemy.traits[i] == enemy.weakAtr: # 2nd trait
            enemy.traits[i] = (5 + enemy.weakAmn)
        else: # Remaining traits
            enemy.traits[i] = (5 + enemy.baseAmn)

    # Reassigns their stat based on their order of attributes
    enemy.strength = enemy.traits[0]
    enemy.endurance = enemy.traits[1]
    enemy.flexibility = enemy.traits[2]
    enemy.speed = enemy.traits[3]
    enemy.intelligence = enemy.traits[4]
    enemy.mystery = enemy.traits[5]

# ---------- PARENT CLASS ----------
class Enemies:

    def __init__(self, enemy):
        enemy.strength = 0
        enemy.endurance = 0
        enemy.flexibility = 0
        enemy.speed = 0
        enemy.intelligence = 0
        enemy.mystery = 0
        enemy.traits = ['strength', 'endurance', 'flexibility', 'speed', 'intelligence', 'mystery']


# ---------- RESPECTIVE ENEMY CLASSES ----------
class Brute(Enemies):
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


class Magician(Enemies):
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


class Genius(Enemies):
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


class Joker(Enemies):
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


class Champion(Enemies):
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