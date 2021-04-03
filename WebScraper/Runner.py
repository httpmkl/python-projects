'''

    Project by Nora Calif :)

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
    '''Returns the current date and time'''
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
    global userChoice  # To be accessed in later functions

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


def accessContent(isStart):  # Determines how user wants to view the scraped content
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


def setSchedule():
    # Schedules a timer for when the scraped info is sent to a file
    global time
    print('\n[ How often would you like the content to be scraped? ]')
    print('1. ___ hours  \n2. ___ minutes  \n3. ___ seconds')

    # Loop for entering input until a valid choice is made
    gaveInput = False
    while not gaveInput:
        try:
            choice = int(input())
            if choice == 1:  # Chose hours
                time = setTimer('hours')
                gaveInput = True
            elif choice == 2:  # Chose minutes
                time = setTimer('minutes')
                gaveInput = True
            elif choice == 3:  # Chose seconds
                time = setTimer('seconds')
                gaveInput = True
            else:  # Gave a value out of bounds
                print('\n-> Please enter a valid input!')
        except ValueError:  # Entered non-integer characters
            print('\n-> Please enter a valid input!')

    redirectToContinuousScrape()  # Initiates automatic scraping
    redirectToMenu()  # Redirects to menu afterwards


def redirectToContinuousScrape():
    '''Sets up automatic scraping based on their original choice of content'''
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


def setTimer(unit):
    '''Converts desired time interval to seconds and returns value'''
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


def redirectToMenu(): # Shows at the end of every scrape
    print('\n\n[ Would you like to see more content scraped? ]')
    print('1. YES, take me back to the menu')
    if bgScraping == True:  # If there is something being scaped in the background
        print('2. NO, exit the main program and continue scraping in the background')
    else:  # If nothing is being scraped
        print('2. NO, I\'d like to exit the program')

    # Loop for entering input until a valid choice is made
    gaveInput = False
    while not gaveInput:
        try:
            choice = int(input())
            if choice == 1:  # Chose menu
                menu(False)
                gaveInput = True
            elif choice == 2:  # Chose to exit
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
def GNConsole():  # Chose to view in console
    '''Presents content from Global News in the console'''
    print('\nLoading content...')

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


def GNFile(choseFile):  # Chose to view in file
    '''Presents content from Global News in the file GlobalNewsScrape.txt'''
    if choseFile == True:
        print('\nLoading content...')

    scrapeNews()
    now = getCurrentTime()

    global newsData
    newsData = []

    newsData.append(f'TOP HEADLINES FOR {now[0]}:')
    newsData.append(f'[ Last scraped: {now[1]} ]')

    returnGlobalNews()

    # Writes information to GlobalNewsScrape.txt
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


def continuousGNScrape():  # Chose automatic scraping
    '''Scrapes Global News periodically based on an interval set by the user'''
    GNFile(False)
    threading.Timer(time, continuousGNScrape).start()


# Option 2: CBC
def CBCConsole():  # Chose to view in console
    '''Presents content from CBC in the console'''
    print('\nLoading content...')

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


def CBCFile(choseFile):  # Chose to view in file
    '''Presents content from CBC in the file CBCScrape.txt'''
    if choseFile == True:
        print('\nLoading content...')

    scrapeNews()
    now = getCurrentTime()

    global newsData
    newsData = []

    newsData.append(f'TOP HEADLINES FOR {now[0]}:')
    newsData.append(f'[ Last scraped: {now[1]} ]')

    returnCBCNews()

    # Writes content to file CBCScrape.txt
    FileWrite.writeDataOverFile(FileWrite, 'CBCScrape.txt', newsData)

    if choseFile == True:
        # To avoid printing this msg for scheduled scrapes
        print('\n-> Success! Content is send to CBCScrape.txt')
        redirectToMenu()


def returnCBCNews():
    newsData.append('\n\n----------')
    newsData.append('\n-> CBC')
    newsData.append('\n----------\n')

    # Separates scraped data into its components
    CBCHeadlines = cbcNews[0]
    CBCCategories = cbcNews[1]
    CBCTimeAgo = cbcNews[2]

    for num in range(len(CBCHeadlines)):
        # Prints data accordingly
        newsData.append(f'\nTitle: {CBCHeadlines[num]}')
        newsData.append(f'Category: {CBCCategories[num]}')
        newsData.append(f'Time posted: {CBCTimeAgo[num]}')


def continuousCBCScrape():  # Chose automatic scraping
    '''Scrapes CBC periodically based on an interval set by the user'''
    CBCFile(False)
    threading.Timer(time, continuousCBCScrape).start()


# Option 3: Vancouver Sun
def VSConsole():  # Chose to view in console
    '''Presents content from Vancouver Sun in the console'''
    print('\nLoading content...')

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

    # Separates info into its parts
    VSHeadlines = vanSun[0]
    VSCategories = vanSun[1]
    VSTimeAgo = vanSun[2]

    for num in range(len(VSHeadlines)):
        # Prints info one article at a time
        print(f'\nTitle: {VSHeadlines[num]}')
        print(f'Category: {VSCategories[num]}')
        print(f'Time posted: {VSTimeAgo[num]}')


def VSFile(choseFile):  # Chose to view in file
    '''Presents content from Vancouver Sun in the file VSScrape.txt'''
    if choseFile == True:
        print('\nLoading content...')

    scrapeNews()
    now = getCurrentTime()

    global newsData
    newsData = []

    newsData.append(f'TOP HEADLINES FOR {now[0]}:')
    newsData.append(f'[ Last scraped: {now[1]} ]')

    returnVSNews()

    # Writes content to file VSScrape.txt
    FileWrite.writeDataOverFile(FileWrite, 'VSScrape.txt', newsData)

    if choseFile == True:
        # To avoid printing this msg for scheduled scrapes
        print('\n-> Success! Content is send to VSScrape.txt')
        redirectToMenu()


def returnVSNews():
    newsData.append('\n\n----------')
    newsData.append('\n-> VANCOUVER SUN')
    newsData.append('\n----------\n')

    # Separates scraped data
    VSHeadlines = vanSun[0]
    VSCategories = vanSun[1]
    VSTimeAgo = vanSun[2]

    for num in range(len(VSHeadlines)):
        # Prints data one article at a time
        newsData.append(f'\nTitle: {VSHeadlines[num]}')
        newsData.append(f'Category: {VSCategories[num]}')
        newsData.append(f'Time posted: {VSTimeAgo[num]}')


def continuousVSScrape():  # Chose automatic scraping
    '''Scrapes Vancouver Sun periodically based on an interval set by the user'''
    VSFile(False)
    threading.Timer(time, continuousVSScrape).start()


# Option 4: The National Post
def NPConsole():  # Chose to view in console
    '''Presents content from The National Post in the console'''
    print('\nLoading content...')

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


def NPFile(choseFile):  # Chose to view in file
    '''Presents content from The National Post in the file NPScrape.txt'''
    if choseFile == True:
        print('\nLoading content...')

    scrapeNews()
    now = getCurrentTime()

    global newsData
    newsData = []

    newsData.append(f'TOP HEADLINES FOR {now[0]}:')
    newsData.append(f'[ Last scraped: {now[1]} ]')

    returnVSNews()

    # Writes content to file NPScrape.txt
    FileWrite.writeDataOverFile(FileWrite, 'NPScrape.txt', newsData)

    if choseFile == True:
        # To avoid printing this msg for scheduled scrapes
        print('\n-> Success! Content is send to NPScrape.txt')
        redirectToMenu()


def returnNPNews():
    newsData.append('\n\n----------')
    newsData.append('\n-> THE NATIONAL POST')
    newsData.append('\n----------\n')

    # Separates info
    NPHeadlines = natPost[0]
    NPCategories = natPost[1]
    NPTimeAgo = natPost[2]

    for num in range(len(NPHeadlines)):
        # Prints info one article at a time
        newsData.append(f'\nTitle: {NPHeadlines[num]}')
        newsData.append(f'Category: {NPCategories[num]}')
        newsData.append(f'Time posted: {NPTimeAgo[num]}')


def continuousNPScrape():  # Chose automatic scraping
    '''Scrapes The National Post periodically based on an interval set by the user'''
    NPFile(False)
    threading.Timer(time, continuousNPScrape).start()


# Option 5: Scrape all
def newsHeadlinesConsole():  # Chose to view in console
    '''Presents content from all 4 of the news sites in the console'''
    print('\nLoading content...')

    scrapeNews()
    now = getCurrentTime()

    print(f'\n\nTOP HEADLINES FOR {now[0]}:')
    print(f'[ Last scraped: {now[1]} ]')

    # Scrapes all 4 sites + reports trends
    printGlobalNews()
    printCBCNews()
    printVSNews()
    printNPNews()
    printTrends()

    redirectToMenu()


def printTrends():
    '''Prints the most reoccurring category between the 4 news sites'''
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


def newsHeadlinesFile(choseFile):  # Chose to view in file
    '''Presents content from all 4 news sites in the file NewsScrape.txt'''
    if choseFile == True:
        print('\nLoading content...')

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

    # Writes content to file NewsScrape.txt
    FileWrite.writeDataOverFile(FileWrite, 'NewsScrape.txt', newsData)

    if choseFile == True:
        # To avoid printing this msg for scheduled scrapes
        print('\n-> Success! Content is send to NewsScrape.txt')
        redirectToMenu()


def returnTrends():
    '''Returns the most reoccurring category between the 4 news sites'''
    scrapeNews()

    # Gathers category info for different news sites
    GBCategories = globalNews[1]
    CBCCategories = cbcNews[1]
    VSCategories = vanSun[1]
    NPCategories = natPost[1]

    allCategories = []

    for i in range(len(GBCategories)):
        # Stores categories in a single list
        allCategories.append(GBCategories[i])
        allCategories.append(CBCCategories[i])
        allCategories.append(VSCategories[i])
        allCategories.append(NPCategories[i])

    commonCatg = statistics.mode(allCategories)  # Gets the most reoccurring category
    newsData.append('\n\n----------')
    newsData.append('\nTRENDS & ANALYSIS')
    newsData.append(f'-> Common theme for today: {commonCatg.upper()}')


def continuousNewsScrape():  # Chose automatic scraping
    '''Scrapes all 4 news sites periodically based on an interval set by the user'''
    newsHeadlinesFile(False)
    threading.Timer(time, continuousNewsScrape).start()


# Bonus option 6: Newegg scrape
def scrapeTechDeals():
    '''Scrapes Newegg's deals page and stores them in global variables'''
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


def organizeTechData(i):
    '''Sorts data to organize how the shipping and discount is presented'''
    # To organize how the shipping is presented
    if shipping[i] == 'Free Shipping':
        ship = '(w/ Free Shipping)'
    else:
        ship = '+ ' + str(shipping[i])

    # To organize how the discount is presented
    if discount[i] == 'N/A' and ogPrice[i] != 'N/A' and newPrice[i] != 'N/A':
        # Discount isn't specified (but it's not a new item)
        price = ogPrice[i].split('$')
        newP = newPrice[i].split('$')
        diff = float(price[1]) - float(newP[1])  # Calculates the difference between the two prices
        disc = '$' + str(format(diff, '.2f')) + ' off'  # Stores difference in 'disc' variable
    else:
        # Discount percentage is given
        disc = str(discount[i]) + ' off'  # Stores discount in 'disc' variable

    return ship, disc


def neweggConsole():  # Chose to view in console
    '''Presents content from Newegg in the console'''
    print('\nLoading content...')

    scrapeTechDeals()
    now = getCurrentTime()

    print(f'\n\nTOP TECH DEALS FOR {now[0]}:')
    print(f'[ Last scraped: {now[1]} ]')

    print('')  # Empty space

    for i in range(len(itemName)):
        data = organizeTechData(i)
        printDeal(i, data[0], data[1])

    redirectToMenu()  # Redirects to menu at the end


def printDeal(i, ship, disc):
    '''Decides whether an item has a discount, promo, or is new, then prints info accordingly'''
    if ogPrice[i] == 'N/A':  # No original price = new item
        print('\n-> NEW ITEM')
        print(f'Name: {itemName[i]}')
        print(f'Price: {newPrice[i]} {ship} \n')
    elif newPrice[i] == 'N/A':  # No new price = promo deal
        print('\n-> PROMO DEAL')
        print(f'Name: {itemName[i]}')
        print(f'Original price: {ogPrice[i]} {ship}')
        print('[ Check site for a limited time offer on this item! ]\n')
    else:  # Original price & new price = discount item
        print('\n-> DISCOUNT ITEM')
        print(f'Name: {itemName[i]}')
        print(f'Original price: {ogPrice[i]} {ship}')
        print(f'Discount: {disc}')
        print(f'New price: {newPrice[i]} {ship} \n')


def neweggFile(choseFile):  # Chose to view in file
    '''Presents content from Newegg in the file TechScrape.txt'''
    if choseFile == True:
        print('\nLoading content...')

    scrapeTechDeals()
    now = getCurrentTime()

    global pcData
    pcData = []

    pcData.append(f'TOP PC DEALS FOR {now[0]}:')
    pcData.append(f'[ Last scraped: {now[1]} ]')

    pcData.append('')  # Empty space

    for i in range(len(itemName)):
        data = organizeTechData(i)
        returnDeal(i, data[0], data[1])

    # Writes content to file TechScrape.txt
    FileWrite.writeDataOverFile(FileWrite, 'TechScrape.txt', pcData)

    if choseFile == True:
        # To avoid printing this msg for scheduled scrapes
        print('\n-> Success! Content is send to TechScrape.txt')
        redirectToMenu()  # Redirects to menu at the end


def returnDeal(i, ship, disc):
    '''Decides whether an item has a discount, promo, or is new, then adds info to pcData accordingly'''
    if ogPrice[i] == 'N/A':  # No original price = new item
        pcData.append('\n-> NEW ITEM')
        pcData.append(f'Name: {itemName[i]}')
        pcData.append(f'Price: {newPrice[i]} {ship} \n')
    elif newPrice[i] == 'N/A':  # No new price = promo deal
        pcData.append('\n-> PROMO DEAL')
        pcData.append(f'Name: {itemName[i]}')
        pcData.append(f'Original price: {ogPrice[i]} {ship}')
        pcData.append('[ Check site for a limited time offer on this item! ]\n')
    else:  # Original price & new price = discount item
        pcData.append('\n-> DISCOUNT ITEM')
        pcData.append(f'Name: {itemName[i]}')
        pcData.append(f'Original price: {ogPrice[i]} {ship}')
        pcData.append(f'Discount: {disc}')
        pcData.append(f'New price: {newPrice[i]} {ship} \n')


def continuousTechScrape():  # Chose automatic scraping
    '''Scrapes Newegg periodically based on an interval set by the user'''
    neweggFile(False)
    threading.Timer(time, continuousTechScrape).start()


# Runs at the start of the program
menu(True)