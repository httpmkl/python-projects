'''
    Use this class to avoid the circular import error
    Model this after the enemy parent class
    Have stats be accessed here; mainly health & energy (shield is specific to player)

'''
from player import Player
from enemy import Enemy


class Character:

    def __init__(self):
        pass

    # Return health & energy stat depending on name

    def setHealth(self, name, num):
        if name == 'Player':
            player = Player()
            player.setShield(num)
        else:
            enemy = Enemy(name)
            enemy.setHealth(num)
