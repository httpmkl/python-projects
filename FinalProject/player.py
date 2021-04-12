class Player:

    def __init__(self):
        self.myCards = []
        self.myName = 'Placeholder'
        self.type = 'Player'
        self.teammate = None

class Computer:

    def __init__(self):
        self.myCards = []
        self.type = 'Computer'
        self.myName = self.type