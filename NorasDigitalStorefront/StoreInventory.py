from Buyable import Buyable, BuyableClothing, BuyableFood, BuyableGame

class StoreInventory:

    def __init__(self):
        self.clothesForSale = []
        self.foodForSale = []
        self.gamesForSale = []
        self.initializeInventoryLists()

    def getFullInventory(self):
        return self.clothesForSale + self.foodForSale + self.gamesForSale

    def removeItemFromInventory(self, item):
        if type(item) is BuyableClothing:
            self.clothesForSale.remove(item)
        elif type(item) is BuyableFood:
            self.foodForSale.remove(item)
        elif type(item) is BuyableGame:
            self.gamesForSale.remove(item)

    def restockItemToInventory(self, item):
        if type(item) is BuyableClothing:
            self.clothesForSale.append(item)
        elif type(item) is BuyableFood:
            self.foodForSale.append(item)
        elif type(item) is BuyableGame:
            self.gamesForSale.append(item)

    def addMultiple(self, item, num):
        if type(item) is BuyableClothing:
            for x in range(num):
                self.clothesForSale.append(item)
        elif type(item) is BuyableFood:
            for x in range(num):
                self.foodForSale.append(item)
        elif type(item) is BuyableGame:
            for x in range(num):
                self.gamesForSale.append(item)

    def initializeInventoryLists(self):
        #Populate initial clothes list
        #Hoodies
        smallHoodie = BuyableClothing(59.99, 'Hoodie', 'small')
        self.clothesForSale.append(smallHoodie)  #You can add this way, but it is more efficient to do as below ...
        self.clothesForSale.append(BuyableClothing(59.99, 'Hoodie', 'medium'))
        self.clothesForSale.append(BuyableClothing(59.99, 'Hoodie', 'large'))

        #Shoes
        self.clothesForSale.append(BuyableClothing(99.99, 'Dress Shoes', '8'))
        self.clothesForSale.append(BuyableClothing(9.99, 'Sandals', '5'))

        #Gloves
        gloves = BuyableClothing(13.49, 'Gloves', 'Medium')
        self.addMultiple(gloves, 3)


        #Populate initial food list
        #Perishables
        self.foodForSale.append(BuyableFood(12.99, 'Pizza', 400))
        self.foodForSale.append(BuyableFood(24.00, 'Lasagna', 1000))
        self.foodForSale.append(BuyableFood(3.99, 'Spinach', 250))

        #Non-perishables
        self.foodForSale.append(BuyableFood(1.49, 'Beans', 300))
        self.foodForSale.append(BuyableFood(0.99, 'Noodles', 125))
        rice = BuyableFood(7.99, 'Rice', 2000)
        self.addMultiple(rice, 5)


        #Populate initial games list
        #Board Games
        self.gamesForSale.append(BuyableGame(19.99, 'Monopoly', 4, 'Board Game'))
        self.gamesForSale.append(BuyableGame(24.99, 'Scrabble', 2, 'Board Game'))

        #Computer Games
        self.gamesForSale.append(BuyableGame(79.99, 'Breath of the Wild', 2, 'Video Game'))
        self.gamesForSale.append(BuyableGame(59.99, 'Forza', 2, 'Video Game'))