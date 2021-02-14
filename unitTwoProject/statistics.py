class UserStats:
    # Beginning stats
    health = 100
    shield = 0

    def addHealth(self, newHealth):
        UserStats.health += newHealth # Adds specified amount to health

    def getHealth(self):
        return UserStats.health

    def addShield(self, newShield):
        UserStats.shield += newShield # Adds specified amount to shield

    def getShield(self):
        return UserStats.shield