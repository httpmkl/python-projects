class Player:
    strength = 0
    endurance = 0
    flexibility = 0
    speed = 0
    intelligence = 0
    mystery = 0
    traits = ['strength', 'endurance', 'flexibility', 'speed', 'intelligence', 'mystery']
    name = 'Placeholder'

    mainAtr = 'Placeholder'
    secondaryAtr = 'Placeholder'
    weakAtr = 'Placeholder'

    def __init__(self, orderTraits):
        Player.mainAtr = orderTraits[0]
        Player.secondaryAtr = orderTraits[1]
        Player.weakAtr = orderTraits[2]
        self.assign_traits()

    def assign_traits(self):
        # Increases their stats based on predominant traits
        for i in range(0, len(Player.traits)):
            if Player.traits[i] == Player.mainAtr:  # 1st trait
                Player.traits[i] = 9
            elif Player.traits[i] == Player.secondaryAtr:  # 3rd trait
                Player.traits[i] = 8
            elif Player.traits[i] == Player.weakAtr:  # 2nd trait
                Player.traits[i] = 7
            else:  # Remaining traits
                Player.traits[i] = 5

        # Reassigns their stat based on their order of attributes
        Player.strength = Player.traits[0]
        Player.endurance = Player.traits[1]
        Player.flexibility = Player.traits[2]
        Player.speed = Player.traits[3]
        Player.intelligence = Player.traits[4]
        Player.mystery = Player.traits[5]
