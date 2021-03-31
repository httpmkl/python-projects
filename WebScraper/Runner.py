import WebScraper

def menuOptions():
    # Menu options
    print('\n[ Which type of information would you like scraped? ]')
    print('1. Current top news headlines')
    print('2. Today\'s discounts & deals for PC parts')
    print('3. INSERT CATEGORY')
    print('4. INSERT CATEGORY')
    print('5. All of the above')

def menu():
    menuOptions()  # Shows menu options
    global userChoice  # So I can access it in later functions

    # Loop for entering input until a valid choice is made
    gaveInput = False
    while not gaveInput:
        try:
            userChoice = int(input())
            if 0 < userChoice < 6:  # Chose 1-5
                accessContent()  # Asks the user how they want to see the content
                gaveInput = True
            else:  # Gave a value out of bounds
                print('\n-> Please enter a valid input!')
        except ValueError:  # Entered non-integer characters
            print('\n-> Please enter a valid input!')

def accessContent():
    print('\n[ How would you like to access the content? ]')
    print('1. Show me in the console  \n2. Send it to a file  \n3. Set up an automatic scraping timer')

    # Another loop for entering input until a valid choice is made
    gaveInput = False
    while not gaveInput:
        try:
            choice = int(input())
            if choice == 1:
                consoleRedirect()
                gaveInput = True
            elif choice == 2:
                fileRedirect()
                gaveInput = True
            elif choice == 3:
                scheduleRedirect()
                gaveInput = True
            else:  # Gave a value out of bounds
                print('\n-> Please enter a valid input!')
        except ValueError:  # Entered non-integer characters
            print('\n-> Please enter a valid input!')

def consoleRedirect():
    pass

def fileRedirect():
    pass

def scheduleRedirect():
    pass


# Choice 1: Current top news headlines
def newsHeadlinesConsole():
    pass

def newsHeadlinesFile():
    pass

def newsHeadlinesSchedule():
    pass


# Choice 2: Today's discounts & deals for PC parts
def pcDiscountsConsole():
    pass

def pcDiscountsFile():
    pass

def pcDiscountsSchedule():
    pass


# Choice 5: All of the above
def scrapeAllConsole():
    pass

def scrapeAllFile():
    pass

def scrapeAllSchedule():
    pass

menu()