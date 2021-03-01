'''

    CURRENT LEVEL: 6
    (two tier 2 problems fully solved, one tier 3 problem fully solved)

    Features I implemented:
        - Exception handling & BuyableFurniture class (tier 1)
        - Sub-catalog inside the viewCatalog() function (tier 2)
        - List in StoreInventory to keep track of bought items (tier 2)
            - viewRecentPurchases(); returns 3 recently bought items (tier 3)

    Besides those changes, I also made some general improvements on the layout/design
    of the program and fixed up the logic for some existing functions and methods

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
    print('\n[ What would you like to view? ]')
    showChoiceOfItems()

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

def buyItem():
    itemName = input('Please type in the name of the item you wish to buy! ')

    # Holding variable for the desired item, if found
    itemToPurchase = None

    # Look through the full inventory to see if the item is present
    # Convert both item name and user input to lower case to prevent case issues!
    for item in storeInventory.getFullInventory():
        if item.name.lower() == itemName.lower():
            itemToPurchase = item
            break # end loop early if a suitable item is found

    # If a suitable item was found, give them the option to buy it!
    if itemToPurchase is not None:
        print(f'We have {itemToPurchase.name} in stock!')

        # Separated for modularity
        chooseWhetherToBuy(itemToPurchase)

    else:  # If user-entered item is not found in the store inventory
        print('The item you are looking for is sold out or does not exist. Sorry!')

def chooseWhetherToBuy(itemToPurchase):
    # NOTE: It'll check for whether its a random integer OR random character before cancelling the purchase
    # + Exception handling is added
    userChoice = input('Type 1 to BUY NOW, 2 to place in your shopping cart, or any other key to cancel purchase.')
    try:
        userChoice = int(userChoice)
        if userChoice == 1:
            makePurchaseFromStore(itemToPurchase)
        elif userChoice == 2:
            print('We will hold onto this item for you. Adding to shopping cart ... ')
            moveItemToShoppingCart(itemToPurchase)
        else:  # Random number typed (not 1 or 2)
            print('Purchase cancelled! Sending you back to the storefront ... ')
    except ValueError:  # Random characters typed
        print('Purchase cancelled! Sending you back to the storefront ... ')

def reviewMyInventory():
    print('Here is a list of the items you now own: ')
    for item in myStuff:
        print(item.name)

def reviewFinancials():
    myBankAccount.balanceReport()

def reviewMyShoppingCart():
    if len(myShoppingCart) > 0:
        print('Here are all of the items being held in your shopping cart: ')
        for item in myShoppingCart:
            print(item.name)

        # Check to see if the user wants to purchase anything currently in their shopping cart

        # NOTE: I added exception handling below
        userChoice = input('Would you like to purchase any held items now? 1 for YES or any other key for NO')
        try:
            userChoice = int(userChoice)
            if userChoice == 1:
                buyItemInShoppingCart()
            else:  # Random number typed
                print('Leaving shopping cart as is and returning to the storefront ... ')
        except ValueError:  # Random character type
            print('Leaving shopping cart as is and returning to the storefront ... ')

    else: # If cart is empty
        print('Your shopping cart is empty! Nothing to see here ... ')

def buyItemInShoppingCart():
    userChoice = input('Type in the name of the item you want to buy from the shopping cart: ')

    # Compare user requested name with cart entry names and offer a purchasing offer if there is a match
    itemInCart: Buyable
    for itemInCart in myShoppingCart:
        if itemInCart.name.lower() == userChoice.lower():
            makePurchaseFromShoppingCart(itemInCart)
        else:
            print('Item could not be found in shopping cart ... ')

def removeItemFromShoppingCart(item):
    userChoice = input('Which item would you like to remove from your shopping cart?')

    # Compare user requested name with cart entry names and remove item if found
    itemInCart: Buyable
    for itemInCart in myShoppingCart:
        if itemInCart.name.lower() == userChoice.lower():
            print(f'You have removed {itemInCart.name} from your shopping cart!')
            moveItemFromShoppingCartToInventory(itemInCart)
        else:
            print('Item could not be found in your shopping cart. Nothing was removed.')

def moveItemToShoppingCart(item):
    myShoppingCart.append(item)
    storeInventory.removeItemFromInventory(item)

def moveItemFromShoppingCartToInventory(item):
    storeInventory.restockItemToInventory(item)
    myShoppingCart.remove(item)

def makePurchaseFromStore(item):
    # If you can afford the item, buy it and remove it from the store

    # NOTE: Moved the passEntry to here so the user can be stopped if the password is incorecct
    if myBankAccount.canAfford(item.price):
        passEntry = input('Please enter your password to confirm your identity: ')
        if passEntry == myBankAccount.getPassword():
            myBankAccount.makePurchase(item.price)
            print(f'Purchase complete! You now own {item.name}')
            myStuff.append(item)
            storeInventory.boughtItems.append(item)
        else:
            print('Incorrect password!')
    else:
        print('You can\'t afford that item ... ')

# Made changes here to the logic of the code
def makePurchaseFromShoppingCart(item):
    # If you can afford the item, buy it and remove it from the store

    # NOTE: Same adjustments from makePurchaseFromStore()
    if myBankAccount.canAfford(item.price):
        passEntry = input('Please enter your password to confirm your identity: ')
        if passEntry == myBankAccount.getPassword():
            myBankAccount.makePurchase(item.price)
            print(f'Purchase complete! You now own {item.name}')
            myStuff.append(item)
            storeInventory.boughtItems.append(item)
            myShoppingCart.remove(item)
        else:
            print('Incorrect password!')
    else:
        print('You can\'t afford that item ... ')

# NOTE: I made this function to show the user's 3 recently bought items
def viewRecentPurchases():
    print('\n[ Recent items: ]')
    if len(storeInventory.boughtItems) > 0:

        # To get the last 3 items (displayed recent -> least recent)
        recent = storeInventory.boughtItems[-3:]
        recent.reverse()

        for item in recent:
            print(f'-> {item.name}')

    else:  # If there aren't any purchased items yet
        print('You have not purchased anything yet!')

def redirectToChoice():
    stillShopping = True
    while stillShopping:
        options()  # To shorten this function

        # I added a try-except + while loop to avoid value errors
        showedOptions = True

        while showedOptions:
            try:
                userChoice = int(input())
                showedOptions = False
                # Redirects user to option
                if userChoice == 1:
                    viewCatalog()
                elif userChoice == 2:
                    buyItem()
                elif userChoice == 3:
                    reviewMyShoppingCart()
                elif userChoice == 4:
                    reviewMyInventory()
                elif userChoice == 5:
                    reviewFinancials()
                elif userChoice == 6:
                    viewRecentPurchases()
                elif userChoice == 7:
                    print('Thanks for shopping! Now exiting program ... ')
                    stillShopping = False
                else:
                    print('Incorrect input! Please choose again.')
                    showedOptions = True
            except ValueError:
                print('Please enter a valid input!')
                showedOptions = True

def options():
    print("\n---------------")
    print("\nMENU OPTIONS: \n")
    print("1. View catalog of items to buy")
    print("2. Buy an item")
    print("3. View your cart of held items")
    print("4. Review the items you already own")
    print("5. View the status of your financials")
    print("6. View recent purchases")
    print("7. Exit program")



# PROGRAM BEGINS HERE
print('\nWELCOME TO THE STOREFRONT\n')

# Setup bank account
print('\n[ To begin, please set up a bank account. ]')
gaveDeposit = False

# I made the float conversion occur here so the user can be stopped immediately if the input isn't a number
while not gaveDeposit:
    try:
        deposit = float(input('Deposit $: '))
        gaveDeposit = True
        print(f'\n-> ${deposit:.2f} added to bank account! \n')
    except ValueError:
        print('\nPlease enter a valid amount! \n')

myBankAccount = BankAccount(deposit)

# Begin shopping
redirectToChoice()