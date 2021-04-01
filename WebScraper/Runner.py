import WebScraper
from FileWrite import FileWrite
import time, threading
import statistics
from datetime import datetime


def menuOptions():
    # Menu options
    print('\n[ Which type of information would you like scraped? ]')
    print('1. Current top news headlines')
    print('2. Today\'s discounts & deals for PC parts')
    print('3. INSERT CATEGORY')
    print('4. INSERT CATEGORY')
    print('5. All of the above')

def getCurrentTime():
    now = datetime.now()  # Gets current date and time
    dateAndTime = str(now).split(' ')  # Splits into separate elements for date & time

    dateNow = dateAndTime[0]  # Assigns first element to date

    timeNow = dateAndTime[1]  # Assigns second element to time
    # Cleans up timeNow to display only hour:min
    timeNow = timeNow.split('.')
    timeNow = timeNow[0]
    timeNow = timeNow.split(':')
    timeNow = str(timeNow[0]) + ':' + str(timeNow[1])

    return dateNow, timeNow  # Returns date & time

def menu(isStart):
    menuOptions()  # Shows menu options
    global userChoice  # So I can access it in later functions

    # Loop for entering input until a valid choice is made
    gaveInput = False
    while not gaveInput:
        try:
            userChoice = int(input())
            if 0 < userChoice < 6:  # Chose 1-5
                accessContent(isStart)  # Asks the user how they want to see the content
                gaveInput = True
            else:  # Gave a value out of bounds
                print('\n-> Please enter a valid input!')
        except ValueError:  # Entered non-integer characters
            print('\n-> Please enter a valid input!')


def accessContent(isStart):
    global accessChoice
    global bgScraping

    if isStart == True:
        # bgScraping is given a value of false in the beginning and when it becomes true, it doesn't change
        bgScraping = False

    print('\n[ How would you like to access the content? ]')
    print('1. Show me in the console  \n2. Send it to a file  \n3. Set up an automatic scraping timer')

    # Another loop for entering input until a valid choice is made
    gaveInput = False
    while not gaveInput:
        try:
            accessChoice = int(input())
            if accessChoice == 1:
                consoleRedirect()
                gaveInput = True
            elif accessChoice == 2:
                fileRedirect()
                gaveInput = True
            elif accessChoice == 3:
                bgScraping = True
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
        newsHeadlinesFile(True)
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

# Shows at the end of every scrape
def redirectToMenu():
    print('\n\n[ Would you like to see more content scraped? ]')
    print('1. YES, take me back to the menu')
    if bgScraping == True:
        print('2. NO, exit the main program and continue scraping in the background')
    else:
        print('2. NO, I\'d like to exit the program')

    # Loop for entering input until a valid choice is made
    gaveInput = False
    while not gaveInput:
        try:
            choice = int(input())
            if choice == 1:
                menu(False)
                gaveInput = True
            elif choice == 2:
                print('\n-> Have a nice day!')
                if bgScraping == True:
                    print('[ rest assured, your content is still being scraped periodically! ]\n')
                quit()
            else:  # Gave a value out of bounds
                print('\n-> Please enter a valid input!')
        except ValueError:  # Entered non-integer characters
            print('\n-> Please enter a valid input!')


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
    now = getCurrentTime()

    print(f'\n\nTOP HEADLINES FOR {now[0]}:')
    print(f'[ Last scraped: {now[1]} ]')
    printGlobalNews()
    printCBCNews()
    printVSNews()
    printNPNews()
    printTrends()

    redirectToMenu()

def printGlobalNews():
    print('\n\n----------')
    print('\n-> GLOBAL NEWS')
    print('\n----------\n')

    GBHeadlines = globalNews[0]
    GBCategories = globalNews[1]
    GBTimeAgo = globalNews[2]

    for num in range(len(GBHeadlines)):
        print(f'\nTitle: {GBHeadlines[num]}')
        print(f'Category: {GBCategories[num]}')
        print(f'Time posted: {GBTimeAgo[num]}')

def printCBCNews():
    print('\n\n----------')
    print('\n-> CBC')
    print('\n----------\n')

    CBCHeadlines = cbcNews[0]
    CBCCategories = cbcNews[1]
    CBCTimeAgo = cbcNews[2]

    for num in range(len(CBCHeadlines)):
        print(f'\nTitle: {CBCHeadlines[num]}')
        print(f'Category: {CBCCategories[num]}')
        print(f'Time posted: {CBCTimeAgo[num]}')

def printVSNews():
    print('\n\n----------')
    print('\n-> VANCOUVER SUN')
    print('\n----------\n')

    VSHeadlines = vanSun[0]
    VSCategories = vanSun[1]
    VSTimeAgo = vanSun[2]

    for num in range(len(VSHeadlines)):
        print(f'\nTitle: {VSHeadlines[num]}')
        print(f'Category: {VSCategories[num]}')
        print(f'Time posted: {VSTimeAgo[num]}')

def printNPNews():
    print('\n\n----------')
    print('\n-> THE NATIONAL POST')
    print('\n----------\n')

    NPHeadlines = natPost[0]
    NPCategories = natPost[1]
    NPTimeAgo = natPost[2]

    for num in range(len(NPHeadlines)):
        print(f'\nTitle: {NPHeadlines[num]}')
        print(f'Category: {NPCategories[num]}')
        print(f'Time posted: {NPTimeAgo[num]}')

def printTrends():
    scrapeNews()
    GBCategories = globalNews[1]
    CBCCategories = cbcNews[1]
    VSCategories = vanSun[1]
    NPCategories = natPost[1]
    allCategories = []

    for i in range(len(GBCategories)):
        allCategories.append(GBCategories[i])
        allCategories.append(CBCCategories[i])
        allCategories.append(VSCategories[i])
        allCategories.append(NPCategories[i])

    commonCatg = statistics.mode(allCategories)
    print('\n\n----------')
    print('\nTRENDS & ANALYSIS')
    print(f'-> Common theme for today: {commonCatg.upper()}')

# Sends news headlines to file
def newsHeadlinesFile(choseFile):
    scrapeNews()
    now = getCurrentTime()

    global data
    data = []
    data.append(f'TOP HEADLINES FOR {now[0]}:')
    data.append(f'[ Last scraped: {now[1]} ]')

    returnGlobalNews()
    returnCBCNews()
    returnVSNews()
    returnNPNews()
    returnTrends()

    FileWrite.writeDataOverFile(FileWrite, 'NewsScrape.txt', data)

    if choseFile == True:
        # To avoid printing this msg for scheduled scrapes
        print('\n-> Success! Content is send to NewsScrape.txt')
        redirectToMenu()

def returnGlobalNews():
    data.append('\n\n----------')
    data.append('\n-> GLOBAL NEWS')
    data.append('\n----------\n')

    GBHeadlines = globalNews[0]
    GBCategories = globalNews[1]
    GBTimeAgo = globalNews[2]

    for num in range(3):
        data.append(f'\nTitle: {GBHeadlines[num]}')
        data.append(f'Category: {GBCategories[num]}')
        data.append(f'Time posted: {GBTimeAgo[num]}')

def returnCBCNews():
    data.append('\n\n----------')
    data.append('\n-> CBC')
    data.append('\n----------\n')

    CBCHeadlines = cbcNews[0]
    CBCCategories = cbcNews[1]
    CBCTimeAgo = cbcNews[2]

    for num in range(3):
        data.append(f'\nTitle: {CBCHeadlines[num]}')
        data.append(f'Category: {CBCCategories[num]}')
        data.append(f'Time posted: {CBCTimeAgo[num]}')

def returnVSNews():
    data.append('\n\n----------')
    data.append('\n-> VANCOUVER SUN')
    data.append('\n----------\n')

    VSHeadlines = vanSun[0]
    VSCategories = vanSun[1]
    VSTimeAgo = vanSun[2]

    for num in range(3):
        data.append(f'\nTitle: {VSHeadlines[num]}')
        data.append(f'Category: {VSCategories[num]}')
        data.append(f'Time posted: {VSTimeAgo[num]}')

def returnNPNews():
    data.append('\n\n----------')
    data.append('\n-> THE NATIONAL POST')
    data.append('\n----------\n')

    NPHeadlines = natPost[0]
    NPCategories = natPost[1]
    NPTimeAgo = natPost[2]

    for num in range(3):
        data.append(f'\nTitle: {NPHeadlines[num]}')
        data.append(f'Category: {NPCategories[num]}')
        data.append(f'Time posted: {NPTimeAgo[num]}')

def returnTrends():
    scrapeNews()
    GBCategories = globalNews[1]
    CBCCategories = cbcNews[1]
    VSCategories = vanSun[1]
    NPCategories = natPost[1]
    allCategories = []

    for i in range(len(GBCategories)):
        allCategories.append(GBCategories[i])
        allCategories.append(CBCCategories[i])
        allCategories.append(VSCategories[i])
        allCategories.append(NPCategories[i])

    commonCatg = statistics.mode(allCategories)
    data.append('\n\n----------')
    data.append('\nTRENDS & ANALYSIS')
    data.append(f'-> Common theme for today: {commonCatg.upper()}')

# Schedules a timer for when the scraped info is sent to a file
def newsHeadlinesSchedule():
    global time
    print('\n[ How often would you like the content to be scraped? ]')
    print('1. ___ hours  \n2. ___ minutes  \n3. ___ seconds')

    # Loop for entering input until a valid choice is made
    gaveInput = False
    while not gaveInput:
        try:
            choice = int(input())
            if choice == 1:
                time = setTimer('hours')
                gaveInput = True
            elif choice == 2:
                time = setTimer('minutes')
                gaveInput = True
            elif choice == 3:
                time = setTimer('seconds')
                gaveInput = True
            else:  # Gave a value out of bounds
                print('\n-> Please enter a valid input!')
        except ValueError:  # Entered non-integer characters
            print('\n-> Please enter a valid input!')

    continuousScrape()
    redirectToMenu()

def continuousScrape():
    newsHeadlinesFile(False)
    threading.Timer(time, continuousScrape).start()

def setTimer(unit):
    gaveInput = False
    while not gaveInput:
        try:
            secs = int(input('\nEnter amount: '))
            if unit == 'hours':
                secs *= 3600  # Converts hours to seconds
                gaveInput = True
            elif unit == 'minutes':
                secs *= 60  # Converts minutes to seconds
                gaveInput = True
            elif unit == 'seconds':
                # If unit is seconds, time isn't altered
                gaveInput = True
        except ValueError:  # Entered non-integer characters
            print('\n-> Please enter a valid input!')

    return secs


# Choice 2: Today's discounts & deals for PC parts
def scrapePcParts():
    global itemName
    global ogPrice
    global newPrice
    global shipping
    global discount
    newegg = WebScraper.scrapeNewegg()

    itemName = newegg[0]
    ogPrice = newegg[1]
    newPrice = newegg[2]
    shipping = newegg[3]
    discount = newegg[4]

def pcDiscountsConsole():
    scrapePcParts()
    print('')  # Empty space

    for i in range(len(itemName)):
        if shipping[i] == 'Free Shipping':
            ship = '(w/ Free Shipping)'
        else:
            ship = '+ ' + str(shipping[i])

        if discount[i] == 'N/A':
            price = ogPrice[i].split('$')
            newP = newPrice[i].split('$')
            diff = float(price[1]) - float(newP[1])  # TODO: Fix out of range error
            disc = '$' + str(format(diff, '.2f')) + ' off'
        else:
            disc = str(discount[i]) + ' off'

        if ogPrice[i] == 'N/A':
            print('\n-> NEW ITEM')
            print(f'Name: {itemName[i]}')
            print(f'Price: {newPrice[i]} {ship}')
        else:
            print('\n-> DISCOUNTED ITEM')
            print(f'Name: {itemName[i]}')
            print(f'Original price: {ogPrice[i]} {ship}')
            print(f'Discount: {disc}')
            print(f'New price: {newPrice[i]} {ship}')


def pcDiscountsFile():
    scrapePcParts()

def pcDiscountsSchedule():
    scrapePcParts()


# Choice 5: All of the above
def scrapeAllConsole():
    pass

def scrapeAllFile():
    pass

def scrapeAllSchedule():
    pass

menu(True)