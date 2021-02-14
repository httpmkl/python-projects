# Warrior - enemy child class
from enemy import Enemy

class Warrior(Enemy):

    def __init__(self):
        super().__init__('Warrior')