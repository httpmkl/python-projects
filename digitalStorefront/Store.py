'''

    * If you want to test the administrator log-in the beginning of the program, the Admin ID is '123' :)

    Features I implemented:
        - Exception handling & BuyableFurniture class (tier 1)
        - Sub-catalog inside the viewCatalog() function (tier 2)
        - List in StoreInventory to keep track of bought items (tier 2)
            - viewRecentPurchases(); shows the 3 most recently bought items (tier 3)
        - Ability to access the store as an administrator and add inventory items (tier 2)
            - Log-in at the start in order to show the 'add items' option to admins only (tier 3)
        - Ability to return items back to the store (tier 2)
            - Only the 3 most recent purchases can be returned (tier 3)

    Major changes I made to the existing code:
        - Updated buyItem() to display more details about each item (allows for more choice in the selection)
        - Improved the shopping cart and added buyEverythingInShoppingCart() for user convenience

'''


from StoreInventory import StoreInventory
from BankAccount import BankAccount
from Buyable import Buyable, BuyableGame, BuyableFood, BuyableClothing, BuyableFurniture

# Initialize inventories
storeInventory = StoreInventory()
myStuff = list()
myShoppingCart = list()

# Placeholder bank account
myBankAccount = BankAccount(1, 'placeholder')

# FUNCTIONS TO MANAGE MENU SYSTEM IN MAIN SHOPPING PROGRAM

def viewCatalog():
    print("\n---------------")
    print('\n[ What would you like to view? ]')
    showChoiceOfItems()
    continueShopping()

# NOTE: Here is where I implemented the sub-catalog
def showChoiceOfItems():
    loop = True
    while loop:
        try:
            choice = int(input('1. Clothes | 2. Food | 3. Games | 4. Furniture \n'))
            print()  # For spacing/layout
            if choice == 1:
                loop = False
                item: Buyable
                for item in storeInventory.getClothes():
                    print(f'-> {item.name}')
            elif choice == 2:
                loop = False
                item: Buyable
                for item in storeInventory.getFood():
                    print(f'-> {item.name}')
            elif choice == 3:
                loop = False
                item: Buyable
                for item in storeInventory.getGames():
                    print(f'-> {item.name}')
            elif choice == 4:
                loop = False
                item: Buyable
                for item in storeInventory.getFurniture():
                    print(f'-> {item.name}')
            else:
                print('-> Please choose between the options! \n')
        except ValueError:
            print('\n-> Please choose between the options! \n')

# NOTE: I added this function so the user can choose to view the selection before purchasing (if they haven't already)
def offerToSeeInventory():
    print("\n---------------")
    print('\n[ Have you already viewed our selection of items? ]')
    loop = True
    while loop:
        try:
            choice = int(input('\n1. Yes, I know what to purchase \n2. No, I would like to see it \n'))
            if choice == 1:  # Redirects to buyItem()
                loop = False
                buyItem()
            elif choice == 2:  # Redirects to viewCatalog()
                loop = False
                viewCatalog()
            else:
                print('\n-> Please choose between the options!')
        except ValueError:
            print('\n-> Please enter a valid input!')

def buyItem():
    itemName = input('\n[ Enter the name of the item you wish to buy ] \n')

    # NOTE: This was changed to a list so multiples of an item can be shown w/ detail
    itemToPurchase = []

    # Look through the full inventory to see if the item is present
    # Convert both item name and user input to lower case to prevent case issues!
    for item in storeInventory.getFullInventory():
        if item.name.lower() == itemName.lower():
            itemToPurchase.append(item)  # NOTE: Adds each item with that name to the itemToPurchase list

    # If a suitable item was found, give them the option to buy it!
    if len(itemToPurchase) > 0:
        print(f'\n\n... {itemName.upper()} IS IN STOCK ...\n')
        printDetails(itemToPurchase)

    else:  # If user-entered item is not found in the store inventory
        print('\n-> The item you are looking for is sold out or does not exist. Sorry!')

def continueShopping():
    # NOTE: So users can browse each section without having to go to the menu and back each time
    try:
        choice = int(input("\n[ Type '1' to continue browsing the inventory, and a random key to exit ] \n"))
        if choice == 1:
            viewCatalog()
        else:
            print('\n-> Exiting inventory...')
    except ValueError:
        print('\n-> Exiting inventory...')

def printDetails(itemToPurchase):
    # NOTE: So it prints the details of every item with that name
    num = 0
    for item in itemToPurchase:
        if item.category == "Clothing":
            num += 1
            print(f'{num}. {item.name} / {item.size} / ${item.price}')
        elif item.category == "Food":
            num += 1
            print(f'{num}. {item.name} / {item.weight} g / ${item.price}')
        elif item.category == "Game":
            num += 1
            print(f'{num}. {item.name} / {item.genre} / max. {item.numPlayers} players / ${item.price}')
        elif item.category == "Furniture":
            num += 1
            print(f'{num}. {item.name} / {item.colour} / ${item.price}')

    print()
    pickItemToPurchase(itemToPurchase, num)

def pickItemToPurchase(itemToPurchase, num):
    # NOTE: This function gives the user the option for choosing a particular item
    if len(itemToPurchase) > 1:  # If there's more than one of the item, they get to choose
        loop = True
        while loop:  # So they get sent back if there's an invalid input
            try:
                choice = int(input('\n[ Type the number of the item you want ] \n'))
                if choice > num or choice < 1:
                    print('\n-> Please choose between the options!')
                else:
                    item = itemToPurchase[choice - 1]
                    chooseWhetherToBuy(item)
                    loop = False
            except ValueError:
                print('\n-> Please enter a valid input!')
    else:  # If there's only one, they don't get to choose
        item = itemToPurchase[0]
        chooseWhetherToBuy(item)

def chooseWhetherToBuy(item):
    # NOTE: It'll check for whether its a random integer OR random character before cancelling the purchase
    # + Exception handling is added
    userChoice = input('\n...Type 1 to BUY NOW \n...2 to place in your shopping cart \n...Or any other key to cancel the purchase \n')
    try:
        userChoice = int(userChoice)
        if userChoice == 1:
            makePurchaseFromStore(item)
        elif userChoice == 2:
            print('\n-> We will hold onto this item for you. Adding to shopping cart... ')
            moveItemToShoppingCart(item)
        else:  # Random number typed (not 1 or 2)
            print('\n-> Purchase cancelled! Sending you back to the storefront... ')
    except ValueError:  # Random characters typed
        print('\n-> Purchase cancelled! Sending you back to the storefront... ')

def reviewFinancials():
    print("\n---------------")
    print('\n[ Bank Account ]')
    print('\n-> ', end='')  # So the balanceReport() appears after the -> (not in a separate line)
    myBankAccount.balanceReport()

def reviewMyShoppingCart():
    print("\n---------------")
    print('\n[ Shopping Cart: ] \n')
    if len(myShoppingCart) > 0:
        num = 0
        for item in myShoppingCart:
            num += 1
            print(f'{num}. {item.name}')

        # Check to see if the user wants to purchase anything currently in their shopping cart
        # NOTE: I added exception handling and changed how this process works
        continueOrExitCart(num)

    else: # If cart is empty
        print('-> Your shopping cart is empty! Nothing to see here... ')

def continueOrExitCart(num):
    choice = input("\n\n...Type 1 to BUY an item \n...2 to REMOVE an item \n...Or any other key to exit \n")
    try:
        choice = int(choice)
        # Redirects to choice
        if choice == 1:
            chosePurchaseFromCart(num)
        elif choice == 2:
            choseRemoveFromCart(num)
        else:  # Entered a random integer
            print('\n-> Exiting shopping cart...')
    except ValueError:  # Entered a random character
        print('\n-> Exiting shopping cart...')

def choseRemoveFromCart(num):
    loop = True
    while loop:
        try:
            userChoice = int(input("\n[ Enter the number of the item you\'d like to remove ] \n"))
            loop = False
            removeItemFromShoppingCart(num, userChoice)
        except ValueError:
            print('\n-> Please enter a valid input!')

def chosePurchaseFromCart(num):
    loop = True
    while loop:
        try:
            userChoice = input("\n[ Enter the number of the item you\'d like to purchase, or 'ALL' to buy everything in your cart ] \n")
            if userChoice.lower() == 'all':
                loop = False
                buyEverythingInShoppingCart()
            else:
                userChoice = int(userChoice)
                loop = False
                buyItemInShoppingCart(num, userChoice)
        except ValueError:
            print('\n-> Please enter a valid input!')

def buyItemInShoppingCart(num, choice):
    if len(myShoppingCart) > 1:
        try:
            if choice > num or choice < 1:
                print('\n-> Please choose between the options!')
                continueOrExitCart(num)
            else:
                itemInCart = myShoppingCart[choice - 1]
                makePurchaseFromShoppingCart(itemInCart)
        except ValueError:
            print('\n-> Please enter a valid input!')
            continueOrExitCart(num)
    else:  # Only one item in inventory
        itemInCart = myShoppingCart[0]
        makePurchaseFromShoppingCart(itemInCart)

# NOTE: Created as a shortcut for buying all inventory items
def buyEverythingInShoppingCart():
    # To figure out the collective cost
    itemPrice = 0
    for item in myShoppingCart:
        itemPrice += item.price

    if myBankAccount.canAfford(itemPrice):
        print('\n[ Verify your identity to proceed ]')
        passEntry = input('Password: ')
        if passEntry == myBankAccount.getPassword():
            for itemInCart in myShoppingCart:
                myStuff.append(itemInCart)
                storeInventory.boughtItems.append(itemInCart)
            myShoppingCart.clear()
            myBankAccount.makePurchase(itemPrice)
            print('\n-> Items successfully purchased!')
        else:
            print('\n-> Incorrect password! Item cannot be bought')
    else:
        print(f'\n-> You don\'t have enough funds for these items')

def removeItemFromShoppingCart(num, choice):
    if len(myShoppingCart) > 1:
        try:
            if choice > num or choice < 1:
                print('\n-> Please choose between the options!')
                continueOrExitCart(num)
            else:
                itemInCart = myShoppingCart[choice - 1]
                moveItemFromShoppingCartToInventory(itemInCart)
        except ValueError:
            print('\n-> Please enter a valid input!')
            continueOrExitCart(num)
    else:  # Only one item in inventory
        itemInCart = myShoppingCart[0]
        moveItemFromShoppingCartToInventory(itemInCart)

def moveItemToShoppingCart(item):
    myShoppingCart.append(item)
    storeInventory.removeItemFromInventory(item)

def moveItemFromShoppingCartToInventory(item):
    storeInventory.restockItemToInventory(item)
    myShoppingCart.remove(item)
    print(f'\n-> Removal complete! {item.name} is no longer in your shopping cart')

def makePurchaseFromStore(item):
    # If you can afford the item, buy it and remove it from the store

    # NOTE: Moved the passEntry to here so the user can be stopped if the password is incorrect
    if myBankAccount.canAfford(item.price):
        print('\n[ Verify your identity to proceed ]')
        passEntry = input('Password: ')
        if passEntry == myBankAccount.getPassword():
            myBankAccount.makePurchase(item.price)
            print(f'\n-> Purchase complete! You now own {item.name}')
            storeInventory.removeItemFromInventory(item)
            myStuff.append(item)
            storeInventory.boughtItems.append(item)
        else:
            print('\n-> Incorrect password! Item cannot be bought')
    else:
        print(f'\n-> You don\'t have enough funds for {item.name}')

def makePurchaseFromShoppingCart(item):
    # If you can afford the item, buy it and remove it from the store

    # NOTE: Same adjustments from makePurchaseFromStore()
    if myBankAccount.canAfford(item.price):
        print('\n[ Verify your identity to proceed ]')
        passEntry = input('Password: ')
        if passEntry == myBankAccount.getPassword():
            myBankAccount.makePurchase(item.price)
            print(f'\n-> Purchase complete! You now own {item.name}')
            myStuff.append(item)
            storeInventory.boughtItems.append(item)
            myShoppingCart.remove(item)
        else:
            print('\n-> Incorrect password! Item cannot be bought')
    else:
        print(f'\n-> You don\'t have enough funds for {item.name}')

# NOTE: I made this function to show the user's 3 recently bought items
def viewRecentPurchases():
    print("\n---------------")
    print('\n[ Three recently bought items: ]\n')
    if len(storeInventory.boughtItems) > 0:

        # To get the last 3 items (displayed recent -> least recent)
        recent = storeInventory.boughtItems[-3:]
        recent.reverse()

        for item in recent:
            print(f'-> {item.name}')

    else:  # If there aren't any purchased items yet
        print('-> You have not bought any items!')

# NOTE: Another new function added; gives the ability to return 3 recent items
def returnItem():
    # The code below is similar to viewRecentPurchases() but in the format of a numbered list instead of ->
    print("\n---------------")
    print('\n[ Three recently bought items: ]\n')
    if len(storeInventory.boughtItems) > 0:

        # To get the last 3 items (displayed recent -> least recent)
        recent = storeInventory.boughtItems[-3:]
        recent.reverse()
        num = 0

        for item in recent:
            num += 1
            print(f'{num}. {item.name}')

        chooseToReturn(num, recent)

    else:  # If there aren't any purchased items yet
        print('-> You have no purchases to return!')

def chooseToReturn(num, recentItems):
    loop = True
    while loop:
        try:
            choice = input("\n\n[ Enter the number of the item you\'d like to return or type 'EXIT' to go back ] \n")
            if choice.lower() == 'exit':
                print('\n-> Returning to the menu...')
                loop = False
            else:
                choice = int(choice)

                if choice > num or choice < 1:
                    print('\n-> Please choose between the options!')
                else:
                    # Returns selected item to the store inventory & refunds money
                    item = recentItems[choice - 1]
                    myStuff.remove(item)
                    storeInventory.boughtItems.remove(item)
                    storeInventory.restockItemToInventory(item)
                    myBankAccount.addMoney(item.price)
                    print(f'\n-> {item.name} successfully returned!')
                    myBankAccount.balanceReport()
                    loop = False
        except ValueError:
            print('\n-> Please enter a valid input!')

# NOTE: The functions below for adding materials all follow the same logic (w/ slight customization)
def addClothes():
    cName = input('\nName of clothing: ')
    cSize = input('Size: ')

    # Loop for receiving a valid price
    gavePrice = False
    while not gavePrice:
        try:
            cPrice = float(input('Price: '))
            gavePrice = True
        except ValueError:
            print('\n-> Please enter a valid price! \n')

    # Uses input to add item
    storeInventory.clothesForSale.append(BuyableClothing(cPrice, cName, cSize))
    print(f'\n-> {cName} added to the inventory!')

def addFood():
    fdName = input('\nName of food: ')
    fdWeight = input('Weight: ')

    gavePrice = False
    while not gavePrice:
        try:
            fdPrice = float(input('Price: '))
            gavePrice = True
        except ValueError:
            print('\n-> Please enter a valid price! \n')

    storeInventory.foodForSale.append(BuyableFood(fdPrice, fdName, fdWeight))
    print(f'\n-> {fdName} added to the inventory!')

def addGames():
    gName = input('\nName of game: ')
    gGenre = input('Genre: ')

    gaveNum = False
    while not gaveNum:
        try:
            gNum = int(input('# of players: '))
            gaveNum = True
        except ValueError:
            print('\n-> Please enter a valid amount! \n')

    gavePrice = False
    while not gavePrice:
        try:
            gPrice = float(input('Price: '))
            gavePrice = True
        except ValueError:
            print('\n-> Please enter a valid price! \n')

    storeInventory.gamesForSale.append(BuyableGame(gPrice, gName, gNum, gGenre))
    print(f'\n-> {gName} added to the inventory!')

def addFurniture():
    fnName = input('\nName of furniture: ')
    fnColour = input('Colour: ')

    gavePrice = False
    while not gavePrice:
        try:
            fnPrice = float(input('Price: '))
            gavePrice = True
        except ValueError:
            print('\n-> Please enter a valid price! \n')

    storeInventory.furnitureForSale.append(BuyableFurniture(fnPrice, fnName, fnColour))
    print(f'\n-> {fnName} added to the inventory!')

# NOTE: This added function allows for administrators to add inventory items
def addInventoryItems():
    gaveInput = False
    print("\n---------------")

    while not gaveInput:
        try:
            print('\n[ What category does the new item fall under? ]')
            choice = int(input('1. Clothes | 2. Food | 3. Games | 4. Furniture \n'))

            if choice == 1:
                addClothes()
                gaveInput = True
            elif choice == 2:
                addFood()
                gaveInput = True
            elif choice == 3:
                addGames()
                gaveInput = True
            elif choice == 4:
                addFurniture()
                gaveInput = True
            else:
                print('\n-> Please choose between the options!')

        except ValueError:
            print('\n-> Please choose between the options!')

def redirectToChoice():
    # NOTE: This is to ensure non-admins don't get the add inventory items option
    if admin:
        maxChoice = 8
    else:
        maxChoice = 7

    stillShopping = True
    while stillShopping:
        options()  # NOTE: Options shown in a separate function for modularity

        # NOTE: I added a try-except + while loop to avoid value errors
        showedOptions = True
        while showedOptions:
            try:
                userChoice = int(input())
                showedOptions = False
                # Redirects user to option
                if userChoice > maxChoice or userChoice < 1:
                    print('\n-> Please choose a valid option! \n')
                    showedOptions = True
                elif userChoice == maxChoice:
                    print("\n---------------")
                    print('\n\nThanks for shopping! \n-> Exiting program \n')
                    stillShopping = False
                elif userChoice == 1:
                    viewCatalog()
                elif userChoice == 2:
                    offerToSeeInventory()
                elif userChoice == 3:
                    reviewMyShoppingCart()
                elif userChoice == 4:
                    reviewFinancials()
                elif userChoice == 5:
                    viewRecentPurchases()
                elif userChoice == 6:
                    returnItem()
                else:  # userChoice == 7
                    addInventoryItems()
            except ValueError:
                print('\n-> Please enter a valid input! \n')
                showedOptions = True

def options():
    print("\n---------------")
    print("\nMENU OPTIONS: \n")
    print("1. View catalog")
    print("2. Purchase an item")
    print("3. Shopping cart")
    print("4. Bank account")
    print("5. Recent purchases")
    print("6. Return an item")

    if admin:
        print("7. Add an inventory item")
        print("8. Exit the store")
    else:
        print("7. Exit the store")


# PROGRAM BEGINS HERE
print('\n\nWELCOME TO THE STOREFRONT \n')

# NOTE: I added the code below to give the option of administrator access
adminStatus = input("\nType '1' if you are an administrator, and a random key if not: ")

try:
    adminStatus = int(adminStatus)
    if adminStatus == 1:  # They claim to be admin
        id = input('\nAdmin ID: ')
        if id == '123':
            print('-> Welcome, admin! \n')
            admin = True
        else:  # Wrong ID
            print('-> ID not registered! \n')
            admin = False
    else:
        print('')
        admin = False
except ValueError:
    print('')
    admin = False

# Setup bank account
print('\n[ To begin, please set up a bank account. ]')
gaveDeposit = False

# NOTE: I made the float conversion occur here so the user can be stopped immediately if the input isn't a number
while not gaveDeposit:
    try:
        deposit = float(input('Deposit $: '))
        gaveDeposit = True
        print(f'\n-> ${deposit:.2f} added to bank account! \n')
    except ValueError:
        print('\n-> Please enter a valid amount! \n')

myBankAccount = BankAccount(deposit)

# Begin shopping
redirectToChoice()