import WebScraper
from FileWrite import FileWrite


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
    # Redirects to console output based on original choice
    if userChoice == 1:
        newsHeadlinesConsole()
    elif userChoice == 2:
        pcDiscountsConsole()
    elif userChoice == 3:
        print('\nUNDER CONSTRUCTION')
    elif userChoice == 4:
        print('\nUNDER CONSTRUCTION')
    elif userChoice == 5:
        scrapeAllConsole()


def fileRedirect():
    # Redirects to file output based on original choice
    if userChoice == 1:
        newsHeadlinesFile()
    elif userChoice == 2:
        pcDiscountsFile()
    elif userChoice == 3:
        print('\nUNDER CONSTRUCTION')
    elif userChoice == 4:
        print('\nUNDER CONSTRUCTION')
    elif userChoice == 5:
        scrapeAllFile()

def scheduleRedirect():
    # Redirects to automatic scraping schedule based on original choice
    if userChoice == 1:
        newsHeadlinesSchedule()
    elif userChoice == 2:
        pcDiscountsSchedule()
    elif userChoice == 3:
        print('\nUNDER CONSTRUCTION')
    elif userChoice == 4:
        print('\nUNDER CONSTRUCTION')
    elif userChoice == 5:
        scrapeAllSchedule()

# Choice 1: Current top news headlines
def scrapeNews():
    global globalNews
    global cbcNews
    global vanSun
    global natPost

    globalNews = WebScraper.scrapeGbNews()
    cbcNews = WebScraper.scrapeCBC()
    vanSun = WebScraper.scrapeVanSun()
    natPost = WebScraper.scrapeNatPost()

# Sends news headlines to run in the console
def newsHeadlinesConsole():
    scrapeNews()

    print('\n\nHere are some of the top headlines from today:')
    printGlobalNews()
    printCBCNews()
    printVSNews()
    printNPNews()

def printGlobalNews():
    print('\n\n-> GLOBAL NEWS')
    GBHeadlines = globalNews[0]
    GBCategories = globalNews[1]
    GBTimeAgo = globalNews[2]

    for num in range(3):
        print(f'\nTitle: {GBHeadlines[num]}')
        print(f'Category: {GBCategories[num]}')
        print(f'Time posted: {GBTimeAgo[num]}')

def printCBCNews():
    print('\n\n-> CBC')
    CBCHeadlines = cbcNews[0]
    CBCCategories = cbcNews[1]
    CBCTimeAgo = cbcNews[2]

    for num in range(3):
        print(f'\nTitle: {CBCHeadlines[num]}')
        print(f'Category: {CBCCategories[num]}')
        print(f'Time posted: {CBCTimeAgo[num]}')

def printVSNews():
    print('\n\n-> VANCOUVER SUN')
    VSHeadlines = vanSun[0]
    VSCategories = vanSun[1]
    VSTimeAgo = vanSun[2]

    for num in range(3):
        print(f'\nTitle: {VSHeadlines[num]}')
        print(f'Category: {VSCategories[num]}')
        print(f'Time posted: {VSTimeAgo[num]}')

def printNPNews():
    print('\n\n-> THE NATIONAL POST')
    NPHeadlines = natPost[0]
    NPCategories = natPost[1]
    NPTimeAgo = natPost[2]

    for num in range(3):
        print(f'\nTitle: {NPHeadlines[num]}')
        print(f'Category: {NPCategories[num]}')
        print(f'Time posted: {NPTimeAgo[num]}')

def printTrends(): # TODO
    pass

# Sends news headlines to file
def newsHeadlinesFile():
    scrapeNews()

    global data
    data = []
    data.append('Here are some of the top headlines from today:')

    returnGlobalNews()
    returnCBCNews()
    returnVSNews()
    returnNPNews()

    FileWrite.writeDataOverFile(FileWrite, 'NewsScrape.txt', data)

def returnGlobalNews():
    data.append('\n-> GLOBAL NEWS')
    GBHeadlines = globalNews[0]
    GBCategories = globalNews[1]
    GBTimeAgo = globalNews[2]

    for num in range(3):
        data.append(f'\nTitle: {GBHeadlines[num]}')
        data.append(f'Category: {GBCategories[num]}')
        data.append(f'Time posted: {GBTimeAgo[num]}')

def returnCBCNews():
    data.append('\n\n-> CBC')
    CBCHeadlines = cbcNews[0]
    CBCCategories = cbcNews[1]
    CBCTimeAgo = cbcNews[2]

    for num in range(3):
        data.append(f'\nTitle: {CBCHeadlines[num]}')
        data.append(f'Category: {CBCCategories[num]}')
        data.append(f'Time posted: {CBCTimeAgo[num]}')

def returnVSNews():
    data.append('\n\n-> VANCOUVER SUN')
    VSHeadlines = vanSun[0]
    VSCategories = vanSun[1]
    VSTimeAgo = vanSun[2]

    for num in range(3):
        data.append(f'\nTitle: {VSHeadlines[num]}')
        data.append(f'Category: {VSCategories[num]}')
        data.append(f'Time posted: {VSTimeAgo[num]}')

def returnNPNews():
    data.append('\n\n-> THE NATIONAL POST')
    NPHeadlines = natPost[0]
    NPCategories = natPost[1]
    NPTimeAgo = natPost[2]

    for num in range(3):
        data.append(f'\nTitle: {NPHeadlines[num]}')
        data.append(f'Category: {NPCategories[num]}')
        data.append(f'Time posted: {NPTimeAgo[num]}')

def returnTrends():  # TODO
    pass

# Schedules a timer for when the scraped info is sent to a file
def newsHeadlinesSchedule():  # TODO
    scrapeNews()


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