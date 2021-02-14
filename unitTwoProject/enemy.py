# Parent class for all of the enemies

class Enemy:
    # Basic traits
    name = 'Placeholder'

    def __init__(self, name):
        Enemy.name = name # Sets the enemy name