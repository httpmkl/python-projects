from Buyable import Buyable, BuyableClothing, BuyableFood, BuyableGame, BuyableFurniture

class StoreInventory:

    def __init__(self):
        self.clothesForSale = []
        self.foodForSale = []
        self.gamesForSale = []
        self.furnitureForSale = []
        self.initializeInventoryLists()
        self.boughtItems = []

    def getFullInventory(self):
        return self.clothesForSale + self.foodForSale + self.gamesForSale + self.furnitureForSale

    # NOTE: These methods below are to display more specific results
    def getClothes(self):
        return self.clothesForSale

    def getFood(self):
        return self.foodForSale

    def getGames(self):
        return self.gamesForSale

    def getFurniture(self):
        return self.furnitureForSale

    def removeItemFromInventory(self, item):
        if type(item) is BuyableClothing:
            self.clothesForSale.remove(item)
        elif type(item) is BuyableFood:
            self.foodForSale.remove(item)
        elif type(item) is BuyableGame:
            self.gamesForSale.remove(item)
        elif type(item) is BuyableFurniture:
            self.furnitureForSale.remove(item)

    def restockItemToInventory(self, item):
        if type(item) is BuyableClothing:
            self.clothesForSale.append(item)
        elif type(item) is BuyableFood:
            self.foodForSale.append(item)
        elif type(item) is BuyableGame:
            self.gamesForSale.append(item)
        elif type(item) is BuyableFurniture:
            self.furnitureForSale.append(item)

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
        elif type(item) is BuyableFurniture:
            for x in range(num):
                self.furnitureForSale.append(item)

    def initializeInventoryLists(self):
        # Populate initial clothes list
        # Hoodies
        self.clothesForSale.append(BuyableClothing(59.99, 'Hoodie', 'Small'))
        self.clothesForSale.append(BuyableClothing(59.99, 'Hoodie', 'Medium'))
        self.clothesForSale.append(BuyableClothing(59.99, 'Hoodie', 'Large'))

        # Shoes
        self.clothesForSale.append(BuyableClothing(99.99, 'Dress Shoes', '8'))
        self.clothesForSale.append(BuyableClothing(9.99, 'Sandals', '5'))

        # Gloves
        gloves = BuyableClothing(13.49, 'Gloves', 'Medium')
        self.addMultiple(gloves, 3)


        # Populate initial food list
        # Perishables
        self.foodForSale.append(BuyableFood(12.99, 'Pizza', 400))
        self.foodForSale.append(BuyableFood(24.99, 'Lasagna', 1000))
        self.foodForSale.append(BuyableFood(3.99, 'Spinach', 250))

        # Non-perishables
        self.foodForSale.append(BuyableFood(1.49, 'Beans', 300))
        self.foodForSale.append(BuyableFood(0.99, 'Noodles', 125))
        rice = BuyableFood(7.99, 'Rice', 2000)
        self.addMultiple(rice, 5)


        # Populate initial games list
        # Board Games
        self.gamesForSale.append(BuyableGame(19.99, 'Monopoly', 4, 'Board Game'))
        self.gamesForSale.append(BuyableGame(24.99, 'Scrabble', 2, 'Board Game'))

        # Computer Games
        self.gamesForSale.append(BuyableGame(79.99, 'Breath of the Wild', 2, 'Video Game'))
        self.gamesForSale.append(BuyableGame(59.99, 'Forza', 2, 'Video Game'))


        # NOTE: Here is where I added the furniture items

        # Populate initial furniture list
        # Living room
        self.furnitureForSale.append(BuyableFurniture(149.99, 'Couch', 'Orange'))
        self.furnitureForSale.append(BuyableFurniture(149.99, 'Couch', 'White'))
        self.furnitureForSale.append(BuyableFurniture(59.99, 'Bookshelf', 'Brown'))

        # Bedroom
        self.furnitureForSale.append(BuyableFurniture(199.99, 'Mattress', 'White'))
        self.furnitureForSale.append(BuyableFurniture(229.99, 'Dresser', 'Silver'))
        self.furnitureForSale.append(BuyableFurniture(39.99, 'Vase', 'Beige'))