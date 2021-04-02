'''

    TODO:
    - Scrape two more websites
    - Set up the menu system for aforementioned websites
    - Create the "scrapeAll" functionality
    - Clean up the code before handing it
        - Ensure everywhere is properly commented
        - Make everything modular and give function descriptions
        - Add "Loading..." text before information gets scraped

    Finish by Friday at the latest !!

'''

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
                setSchedule()
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
        pcDiscountsFile(True)
    elif userChoice == 3:
        print('\nUNDER CONSTRUCTION')
    elif userChoice == 4:
        print('\nUNDER CONSTRUCTION')
    elif userChoice == 5:
        scrapeAllFile()

# Schedules a timer for when the scraped info is sent to a file
def setSchedule():
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

    if userChoice == 1:
        continuousNewsScrape()
    elif userChoice == 2:
        continuousPcScrape()

    redirectToMenu()

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

    global newsData
    newsData = []
    newsData.append(f'TOP HEADLINES FOR {now[0]}:')
    newsData.append(f'[ Last scraped: {now[1]} ]')

    returnGlobalNews()
    returnCBCNews()
    returnVSNews()
    returnNPNews()
    returnTrends()

    FileWrite.writeDataOverFile(FileWrite, 'NewsScrape.txt', newsData)

    if choseFile == True:
        # To avoid printing this msg for scheduled scrapes
        print('\n-> Success! Content is send to NewsScrape.txt')
        redirectToMenu()

def returnGlobalNews():
    newsData.append('\n\n----------')
    newsData.append('\n-> GLOBAL NEWS')
    newsData.append('\n----------\n')

    GBHeadlines = globalNews[0]
    GBCategories = globalNews[1]
    GBTimeAgo = globalNews[2]

    for num in range(3):
        newsData.append(f'\nTitle: {GBHeadlines[num]}')
        newsData.append(f'Category: {GBCategories[num]}')
        newsData.append(f'Time posted: {GBTimeAgo[num]}')

def returnCBCNews():
    newsData.append('\n\n----------')
    newsData.append('\n-> CBC')
    newsData.append('\n----------\n')

    CBCHeadlines = cbcNews[0]
    CBCCategories = cbcNews[1]
    CBCTimeAgo = cbcNews[2]

    for num in range(3):
        newsData.append(f'\nTitle: {CBCHeadlines[num]}')
        newsData.append(f'Category: {CBCCategories[num]}')
        newsData.append(f'Time posted: {CBCTimeAgo[num]}')

def returnVSNews():
    newsData.append('\n\n----------')
    newsData.append('\n-> VANCOUVER SUN')
    newsData.append('\n----------\n')

    VSHeadlines = vanSun[0]
    VSCategories = vanSun[1]
    VSTimeAgo = vanSun[2]

    for num in range(3):
        newsData.append(f'\nTitle: {VSHeadlines[num]}')
        newsData.append(f'Category: {VSCategories[num]}')
        newsData.append(f'Time posted: {VSTimeAgo[num]}')

def returnNPNews():
    newsData.append('\n\n----------')
    newsData.append('\n-> THE NATIONAL POST')
    newsData.append('\n----------\n')

    NPHeadlines = natPost[0]
    NPCategories = natPost[1]
    NPTimeAgo = natPost[2]

    for num in range(3):
        newsData.append(f'\nTitle: {NPHeadlines[num]}')
        newsData.append(f'Category: {NPCategories[num]}')
        newsData.append(f'Time posted: {NPTimeAgo[num]}')

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
    newsData.append('\n\n----------')
    newsData.append('\nTRENDS & ANALYSIS')
    newsData.append(f'-> Common theme for today: {commonCatg.upper()}')

# Scrapes news headlines periodically
def continuousNewsScrape():
    newsHeadlinesFile(False)
    threading.Timer(time, continuousNewsScrape).start()


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
    now = getCurrentTime()

    print(f'\n\nTOP PC DEALS FOR {now[0]}:')
    print(f'[ Last scraped: {now[1]} ]')

    print('')  # Empty space

    for i in range(len(itemName)):
        # To organize how the shipping
        if shipping[i] == 'Free Shipping':
            ship = '(w/ Free Shipping)'
        else:
            ship = '+ ' + str(shipping[i])

        if discount[i] == 'N/A' and ogPrice[i] != 'N/A':  # Discount isn't specified (but it's not a new item)
            price = ogPrice[i].split('$')
            newP = newPrice[i].split('$')
            diff = float(price[-1]) - float(newP[-1])
            disc = '$' + str(format(diff, '.2f')) + ' off'
        else:  # Discount percentage is given
            disc = str(discount[i]) + ' off'

        if ogPrice[i] == 'N/A':
            print('\n-> NEW ITEM')
            print(f'Name: {itemName[i]}')
            print(f'Price: {newPrice[i]} {ship} \n')
        else:
            print('\n-> DISCOUNTED ITEM')
            print(f'Name: {itemName[i]}')
            print(f'Original price: {ogPrice[i]} {ship}')
            print(f'Discount: {disc}')
            print(f'New price: {newPrice[i]} {ship} \n')

def pcDiscountsFile(choseFile):
    scrapePcParts()
    now = getCurrentTime()

    global pcData
    pcData = []

    pcData.append(f'1TOP PC DEALS FOR {now[0]}:')
    pcData.append(f'[ Last scraped: {now[1]} ]')

    pcData.append('')  # Empty space

    for i in range(len(itemName)):
        # To organize how the shipping
        if shipping[i] == 'Free Shipping':
            ship = '(w/ Free Shipping)'
        else:
            ship = '+ ' + str(shipping[i])

        if discount[i] == 'N/A' and ogPrice[i] != 'N/A':  # Discount isn't specified (but it's not a new item)
            price = ogPrice[i].split('$')
            newP = newPrice[i].split('$')
            diff = float(price[-1]) - float(newP[-1])
            disc = '$' + str(format(diff, '.2f')) + ' off'
        else:  # Discount percentage is given
            disc = str(discount[i]) + ' off'

        if ogPrice[i] == 'N/A':
            pcData.append('\n-> NEW ITEM')
            pcData.append(f'Name: {itemName[i]}')
            pcData.append(f'Price: {newPrice[i]} {ship} \n')
        else:
            pcData.append('\n-> DISCOUNTED ITEM')
            pcData.append(f'Name: {itemName[i]}')
            pcData.append(f'Original price: {ogPrice[i]} {ship}')
            pcData.append(f'Discount: {disc}')
            pcData.append(f'New price: {newPrice[i]} {ship} \n')

    FileWrite.writeDataOverFile(FileWrite, 'PcScrape.txt', pcData)

    if choseFile == True:
        # To avoid printing this msg for scheduled scrapes
        print('\n-> Success! Content is send to PcScrape.txt')
        redirectToMenu()

# Scrapes Newegg periodically
def continuousPcScrape():
    pcDiscountsFile(False)
    threading.Timer(time, continuousPcScrape).start()

# Choice 5: All of the above
def scrapeAllConsole():
    pass

def scrapeAllFile():
    pass

def scrapeAllSchedule():
    pass

menu(True)