'''

    TODO:
    - Continue organizing the content from CBC to the end
    - Add "Loading..." text before scrapes

'''

import WebScraper
from FileWrite import FileWrite
import time, threading
import statistics
from datetime import datetime


def menuOptions():
    # Menu options
    print('\n[ Which source would you like scraped? ]')
    print('1. Top headlines from Global News')
    print('2. Top headlines from CBC')
    print('3. Top headlines from Vancouver Sun')
    print('4. Top headlines from The National Post')
    print('5. All of the above')
    print('6. BONUS: Tech discounts on Newegg')

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
            if 0 < userChoice < 7:  # User chose 1-6
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
            if accessChoice == 1:  # Chose to view in console
                consoleRedirect()
                gaveInput = True
            elif accessChoice == 2:  # Chose to view in file
                fileRedirect()
                gaveInput = True
            elif accessChoice == 3:  # Chose to automatically scrape content
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
        GNConsole()
    elif userChoice == 2:
        CBCConsole()
    elif userChoice == 3:
        VSConsole()
    elif userChoice == 4:
        NPConsole()
    elif userChoice == 5:
        newsHeadlinesConsole()
    elif userChoice == 6:
        neweggConsole()

def fileRedirect():
    # Redirects to file output based on original choice
    if userChoice == 1:
        GNFile(True)
    elif userChoice == 2:
        CBCFile(True)
    elif userChoice == 3:
        VSFile(True)
    elif userChoice == 4:
        NPFile(True)
    elif userChoice == 5:
        newsHeadlinesFile(True)
    elif userChoice == 6:
        neweggFile(True)

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

    # Sets up automatic scraping based on their original choice for source
    if userChoice == 1:
        continuousGNScrape()
    elif userChoice == 2:
        continuousCBCScrape()
    elif userChoice == 3:
        continuousVSScrape()
    elif userChoice == 4:
        continuousNPScrape()
    elif userChoice == 5:
        continuousNewsScrape()
    elif userChoice == 6:
        continuousTechScrape()

    redirectToMenu()  # Redirects to menu afterwards

def setTimer(unit):
    # Converts desired time interval to seconds and returns value
    gaveInput = False
    while not gaveInput:
        try:
            secs = int(input('\nEnter time amount: '))
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
                    # Reminds user that their content is being scraped
                    print('[ rest assured, your content is still being scraped periodically! ]\n')
                quit()
            else:  # Gave a value out of bounds
                print('\n-> Please enter a valid input!')
        except ValueError:  # Entered non-integer characters
            print('\n-> Please enter a valid input!')

def scrapeNews():
    '''Scrapes the news sites and stores them in global variables'''
    global globalNews
    global cbcNews
    global vanSun
    global natPost

    globalNews = WebScraper.scrapeGbNews()
    cbcNews = WebScraper.scrapeCBC()
    vanSun = WebScraper.scrapeVanSun()
    natPost = WebScraper.scrapeNatPost()


# Option 1: Global News
def GNConsole():
    '''Presents content from Global News in the console'''
    scrapeNews()
    now = getCurrentTime()

    print(f'\n\nTOP HEADLINES FOR {now[0]}:')
    print(f'[ Last scraped: {now[1]} ]')

    printGlobalNews()
    redirectToMenu()

def printGlobalNews():
    print('\n\n----------')
    print('\n-> GLOBAL NEWS')
    print('\n----------\n')

    # Separates info into headlines, categories, and time
    GBHeadlines = globalNews[0]
    GBCategories = globalNews[1]
    GBTimeAgo = globalNews[2]

    for num in range(len(GBHeadlines)):
        # Prints information one article at a time
        print(f'\nTitle: {GBHeadlines[num]}')
        print(f'Category: {GBCategories[num]}')

        word = GBTimeAgo[num].split(' ')
        if word[0].isdigit():  # If a time is given
            print(f'Time posted: {GBTimeAgo[num]}')
        else:  # If a date is given
            print(f'Date posted: {GBTimeAgo[num]}')

def GNFile(choseFile):
    '''Presents content from Global News in the file GlobalNewsScrape.txt'''
    scrapeNews()
    now = getCurrentTime()

    global newsData
    newsData = []
    newsData.append(f'TOP HEADLINES FOR {now[0]}:')
    newsData.append(f'[ Last scraped: {now[1]} ]')

    returnGlobalNews()

    FileWrite.writeDataOverFile(FileWrite, 'GlobalNewsScrape.txt', newsData)

    if choseFile == True:
        # To avoid printing this msg for scheduled scrapes
        print('\n-> Success! Content is send to GlobalNewsScrape.txt')
        redirectToMenu()

def returnGlobalNews():
    newsData.append('\n\n----------')
    newsData.append('\n-> GLOBAL NEWS')
    newsData.append('\n----------\n')

    # Separates info into headlines, categories, and time
    GBHeadlines = globalNews[0]
    GBCategories = globalNews[1]
    GBTimeAgo = globalNews[2]

    for num in range(len(GBHeadlines)):
        # Same as printGlobalNews() except adds content to newsData list
        newsData.append(f'\nTitle: {GBHeadlines[num]}')
        newsData.append(f'Category: {GBCategories[num]}')
        word = GBTimeAgo[num].split(' ')
        if word[0].isdigit():  # If time is given
            newsData.append(f'Time posted: {GBTimeAgo[num]}')
        else:  # If date is given
            newsData.append(f'Date posted: {GBTimeAgo[num]}')

def continuousGNScrape():
    '''Scrapes Global News periodically based on an interval set by the user'''
    GNFile(False)
    threading.Timer(time, continuousGNScrape).start()


# Option 2: CBC
# TODO: Continue organizing the functions and adding desc from here
def CBCConsole():
    scrapeNews()
    now = getCurrentTime()

    print(f'\n\nTOP HEADLINES FOR {now[0]}:')
    print(f'[ Last scraped: {now[1]} ]')

    printCBCNews()
    redirectToMenu()

def printCBCNews():
    print('\n\n----------')
    print('\n-> CBC')
    print('\n----------\n')

    # Separates info into its different parts
    CBCHeadlines = cbcNews[0]
    CBCCategories = cbcNews[1]
    CBCTimeAgo = cbcNews[2]

    for num in range(len(CBCHeadlines)):
        # Prints info one article at a time
        print(f'\nTitle: {CBCHeadlines[num]}')
        print(f'Category: {CBCCategories[num]}')
        print(f'Time posted: {CBCTimeAgo[num]}')

def VSConsole():  # Prints Vancouver Sun scrape
    scrapeNews()
    now = getCurrentTime()

    print(f'\n\nTOP HEADLINES FOR {now[0]}:')
    print(f'[ Last scraped: {now[1]} ]')

    printVSNews()
    redirectToMenu()

def printVSNews():
    print('\n\n----------')
    print('\n-> VANCOUVER SUN')
    print('\n----------\n')

    # Separates info
    VSHeadlines = vanSun[0]
    VSCategories = vanSun[1]
    VSTimeAgo = vanSun[2]

    for num in range(len(VSHeadlines)):
        # Prints info
        print(f'\nTitle: {VSHeadlines[num]}')
        print(f'Category: {VSCategories[num]}')
        print(f'Time posted: {VSTimeAgo[num]}')

def NPConsole():  # Prints The National Post scrape
    scrapeNews()
    now = getCurrentTime()

    print(f'\n\nTOP HEADLINES FOR {now[0]}:')
    print(f'[ Last scraped: {now[1]} ]')

    printNPNews()
    redirectToMenu()

def printNPNews():
    print('\n\n----------')
    print('\n-> THE NATIONAL POST')
    print('\n----------\n')

    # Separates info
    NPHeadlines = natPost[0]
    NPCategories = natPost[1]
    NPTimeAgo = natPost[2]

    for num in range(len(NPHeadlines)):
        # Prints info
        print(f'\nTitle: {NPHeadlines[num]}')
        print(f'Category: {NPCategories[num]}')
        print(f'Time posted: {NPTimeAgo[num]}')

def newsHeadlinesConsole():  # Scrapes all 4 news sites
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

def printTrends():  # Reports a common theme between the news sites
    scrapeNews()

    # Gathers category info for different news sites
    GBCategories = globalNews[1]
    CBCCategories = cbcNews[1]
    VSCategories = vanSun[1]
    NPCategories = natPost[1]

    allCategories = []

    for i in range(len(GBCategories)):
        # Stores all of the categories into a single list
        allCategories.append(GBCategories[i])
        allCategories.append(CBCCategories[i])
        allCategories.append(VSCategories[i])
        allCategories.append(NPCategories[i])

    commonCatg = statistics.mode(allCategories)  # Gets the most reoccurring category
    print('\n\n----------')
    print('\nTRENDS & ANALYSIS')
    print(f'-> Common theme for today: {commonCatg.upper()}')

def CBCFile(choseFile):
    scrapeNews()
    now = getCurrentTime()

    global newsData
    newsData = []
    newsData.append(f'TOP HEADLINES FOR {now[0]}:')
    newsData.append(f'[ Last scraped: {now[1]} ]')

    returnCBCNews()

    FileWrite.writeDataOverFile(FileWrite, 'CBCScrape.txt', newsData)

    if choseFile == True:
        # To avoid printing this msg for scheduled scrapes
        print('\n-> Success! Content is send to CBCScrape.txt')
        redirectToMenu()

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

def VSFile(choseFile):
    scrapeNews()
    now = getCurrentTime()

    global newsData
    newsData = []
    newsData.append(f'TOP HEADLINES FOR {now[0]}:')
    newsData.append(f'[ Last scraped: {now[1]} ]')

    returnVSNews()

    FileWrite.writeDataOverFile(FileWrite, 'VNScrape.txt', newsData)

    if choseFile == True:
        # To avoid printing this msg for scheduled scrapes
        print('\n-> Success! Content is send to VNScrape.txt')
        redirectToMenu()

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

def NPFile(choseFile):
    scrapeNews()
    now = getCurrentTime()

    global newsData
    newsData = []
    newsData.append(f'TOP HEADLINES FOR {now[0]}:')
    newsData.append(f'[ Last scraped: {now[1]} ]')

    returnVSNews()

    FileWrite.writeDataOverFile(FileWrite, 'NPScrape.txt', newsData)

    if choseFile == True:
        # To avoid printing this msg for scheduled scrapes
        print('\n-> Success! Content is send to NPScrape.txt')
        redirectToMenu()

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


# Scrapes news sites periodically

def continuousCBCScrape():
    CBCFile(False)
    threading.Timer(time, continuousCBCScrape).start()

def continuousVSScrape():
    VSFile(False)
    threading.Timer(time, continuousVSScrape).start()

def continuousNPScrape():
    NPFile(False)
    threading.Timer(time, continuousNPScrape).start()

def continuousNewsScrape():
    newsHeadlinesFile(False)
    threading.Timer(time, continuousNewsScrape).start()

# Bonus option: Newegg scrape
def scrapeTechDeals():
    global itemName
    global ogPrice
    global newPrice
    global shipping
    global discount
    newegg = WebScraper.scrapeNewegg()

    # Separates info from scrape into it's different parts
    itemName = newegg[0]
    ogPrice = newegg[1]
    newPrice = newegg[2]
    shipping = newegg[3]
    discount = newegg[4]

def neweggConsole():
    scrapeTechDeals()
    now = getCurrentTime()

    print(f'\n\nTOP TECH DEALS FOR {now[0]}:')
    print(f'[ Last scraped: {now[1]} ]')

    print('')  # Empty space

    for i in range(len(itemName)):
        printDeal(i)

    redirectToMenu()

def printDeal(i):
    # To organize how the shipping is presented
    if shipping[i] == 'Free Shipping':
        ship = '(w/ Free Shipping)'
    else:
        ship = '+ ' + str(shipping[i])

    if discount[i] == 'N/A' and ogPrice[i] != 'N/A' and newPrice[
        i] != 'N/A':  # Discount isn't specified (but it's not a new item)
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
    elif newPrice[i] == 'N/A':
        print('\n-> PROMO DEAL')
        print(f'Name: {itemName[i]}')
        print(f'Original price: {ogPrice[i]} {ship}')
        print('[ Check site for a limited time offer on this item! ]\n')
    else:
        print('\n-> DISCOUNTED ITEM')
        print(f'Name: {itemName[i]}')
        print(f'Original price: {ogPrice[i]} {ship}')
        print(f'Discount: {disc}')
        print(f'New price: {newPrice[i]} {ship} \n')

def neweggFile(choseFile):
    scrapeTechDeals()
    now = getCurrentTime()

    global pcData
    pcData = []

    pcData.append(f'TOP PC DEALS FOR {now[0]}:')
    pcData.append(f'[ Last scraped: {now[1]} ]')

    pcData.append('')  # Empty space

    for i in range(len(itemName)):
        # To organize how the shipping is presented
        if shipping[i] == 'Free Shipping':
            ship = '(w/ Free Shipping)'
        else:
            ship = '+ ' + str(shipping[i])

        if discount[i] == 'N/A' and ogPrice[i] != 'N/A' and newPrice[
            i] != 'N/A':  # Discount isn't specified (but it's not a new item)
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
        elif newPrice[i] == 'N/A':
            pcData.append('\n-> PROMO DEAL')
            pcData.append(f'Name: {itemName[i]}')
            pcData.append(f'Original price: {ogPrice[i]} {ship}')
            pcData.append('[ Check site for a limited time offer on this item! ]\n')
        else:
            pcData.append('\n-> DISCOUNTED ITEM')
            pcData.append(f'Name: {itemName[i]}')
            pcData.append(f'Original price: {ogPrice[i]} {ship}')
            pcData.append(f'Discount: {disc}')
            pcData.append(f'New price: {newPrice[i]} {ship} \n')

    FileWrite.writeDataOverFile(FileWrite, 'TechScrape.txt', pcData)

    if choseFile == True:
        # To avoid printing this msg for scheduled scrapes
        print('\n-> Success! Content is send to TechScrape.txt')
        redirectToMenu()

# Scrapes Newegg periodically
def continuousTechScrape():
    neweggFile(False)
    threading.Timer(time, continuousTechScrape).start()

menu(True)