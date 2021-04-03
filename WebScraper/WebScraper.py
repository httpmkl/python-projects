from bs4 import BeautifulSoup
import datetime
from datetime import datetime as dt
from datetime import timezone
import requests


def scrapeGbNews():
    '''Scrapes Global News to return top 3 headlines, category, and time since posted'''
    page = requests.get("https://globalnews.ca/")
    soup = BeautifulSoup(page.content, 'html.parser')

    data = soup.find(class_="c-posts c-posts--tile c-posts--grid c-posts--gridMosaic c-posts--highlightFirst l-section__posts")

    # Scrapes data from website
    headlines = gbHeadlines(data)
    catAndTime = gbCatAndTime(data)

    # Separates catAndTime into categories and timeAgo
    categories = catAndTime[0]
    timeAgo = catAndTime[1]

    return headlines, categories, timeAgo  # Returns data


def gbHeadlines(data):
    '''Scrapes headlines from Global News'''
    headlineData = data.find_all(class_="c-posts__headlineText")
    headlineData.pop(0)  # Gets rid of the repeated first header

    headlines = []

    for num in range(len(headlineData)):
        if len(headlines) <= 3:  # Limits headlines to first 3
            headlines.append(headlineData[num].get_text())  # Adds each headline to the list

    return headlines


def gbCatAndTime(data):
    '''Scrapes categories & time ago from Global News'''
    # Scrapes category & time info
    postInfo = data.find_all(class_="c-posts__info")

    categories = []
    timeAgo = []

    # To track which element is a category & time (since it alternates)
    didCategory = False
    didTime = True

    for num in range(len(postInfo)):
        if not didCategory:  # If time was just appended
            if len(categories) <= 3:  # Limits categories to first 3
                categories.append(postInfo[num].get_text())  # Adds element to category list

                # Did category, did not do time
                didCategory = True
                didTime = False

        elif not didTime:  # If category was just appended
            if len(timeAgo) <= 3:  # Limits time to first 3
                # For grammatical correctness
                word = postInfo[num].get_text().split()
                if 'mins' in word:
                    word[1] = 'minutes'
                if 'min' in word:
                    word[1] = 'minute'

                if word[0].isdigit():  # If time is given
                    word = str(word[0]) + ' ' + str(word[1]) + " ago"
                else:  # If date is given
                    word = str(word[0]) + ' ' + str(word[1])  # Doesn't add "ago"

                timeAgo.append(word)  # Adds element to the timeAgo list

                # Did time, did not do category
                didCategory = False
                didTime = True

    return categories, timeAgo


def scrapeCBC():
    '''Scrapes CBC to return top 4 headlines, category, and time since posted'''
    page = requests.get("https://www.cbc.ca/news/canada")
    soup = BeautifulSoup(page.content, 'html.parser')

    data = soup.find(class_="featuredTopStories sclt-featuredTopStories")

    # Scrapes data from website
    headlines = cbcHeadlines(data)
    categories = cbcCategories(data)
    timeAgo = cbcTimeAgo(data)

    return headlines, categories, timeAgo  # Returns data


def cbcHeadlines(data):
    '''Scrapes headlines from CBC'''
    headlineData = data.find_all(class_="headline")
    headlines = []

    for num in range(len(headlineData)):
        if len(headlines) < 3:  # Limits headlines to first 3
            headlines.append(headlineData[num].get_text())  # Adds each element to the headlines list

    return headlines


def cbcCategories(data):
    '''Scrapes categories from CBC'''
    categoryData = data.find_all(class_="departmentItem")
    categories = []

    for num in range(len(categoryData)):
        if len(categories) < 3:  # Limits categories to first 3
            wordList = categoryData[num].get_text().split()  # Splits the element into its separate words

            if '-' in wordList:  # If a hyphen was in the element
                wordList.append(categoryData[num + 1].get_text())  # Adds the next category element to this one
                word = ' '.join(wordList)
                categories.append(word)
            else:  # If a hyphen was not in the element
                pastWordList = categoryData[num - 1].get_text().split()
                if '-' not in pastWordList:  # If there isn't a hyphen in that past word either
                    categories.append(categoryData[num].get_text())
                # If there was a hyphen in the previous element, it's assumed that the current one has been added to that

    # To take out the space at the end of each category
    index = 0
    for i in categories:
        splitWord = i.split()
        joinWord = ' '.join(splitWord)
        categories[index] = joinWord
        index += 1

    return categories


def cbcTimeAgo(data):
    '''Scrapes time posted info from CBC'''
    timeData = data.find_all("time", {"class": "timeStamp"})
    timeAgo = []

    for num in range(len(timeData)):
        if len(timeAgo) < 3:  # Limits time data to first 3
            timeDiff = getTimeDifference(timeData, num)  # Calculates time since posted

            if int(timeDiff[0]) > 0:  # If there has been 1+ hours since posted
                if int(timeDiff[1]) >= 30:
                    # Rounds up the hour if its above 30 minutes in
                    timeDiff = str(int(timeDiff[0]) + 1)
                else:
                    timeDiff = timeDiff[0]

                # For grammatical correctness
                if int(timeDiff) == 1:
                    timeAgo.append(f"{timeDiff} hour ago")
                else:
                    timeAgo.append(f"{timeDiff} hours ago")

            else:  # If there hasn't been an hour since posted
                timeDiff = timeDiff[1]  # Time is shown in minutes

                # Again for grammatical correctness
                if int(timeDiff) == 1:
                    timeAgo.append(f"{timeDiff} minute ago")
                else:
                    timeAgo.append(f"{timeDiff} minutes ago")

    return timeAgo


def getTimeDifference(timeData, num):
    '''Calculates and returns the time since posted for an article'''
    # Cleans timeData[num] to get a list with one element as the date and one element as the time
    singleEntry = str(timeData[num])
    prunedData = singleEntry.split(' ')
    prunedData = prunedData[2].split('"')
    time = prunedData[1].split('T')
    hms = time[1].split('Z')
    time[1] = hms[0]

    # Gathers information on the current time and stores it in a similar format as above
    now = str(dt.now(tz=timezone.utc)).split("+")
    now = now[0].split(" ")

    # Separates the year/month/day and hour/min/sec elements into their components
    ymdPost = time[0].split("-")
    hmsPost = time[1].split(":")
    ymdNow = now[0].split("-")
    hmsNow = now[1].split(":")

    # Stores post time and current time in datetime objects
    postTime = datetime.datetime(int(ymdPost[0]), int(ymdPost[1]), int(ymdPost[2]), int(hmsPost[0]), int(hmsPost[1]), int(float(hmsPost[2])))
    currentTime = datetime.datetime(int(ymdNow[0]), int(ymdNow[1]), int(ymdNow[2]), int(hmsNow[0]), int(hmsNow[1]), int(float(hmsNow[2])))
    timeDiff = currentTime - postTime  # Subtracts the two to get the difference in time

    # Separates the timeDiff into different elements for hours, minutes, and seconds
    timeDiff = str(timeDiff).split(":")

    return timeDiff


def scrapeVanSun():
    '''Scrapes Vancouver Sun to return latest 5 headlines, category, and time since posted'''
    page = requests.get("https://vancouversun.com/")
    soup = BeautifulSoup(page.content, 'html.parser')

    data = soup.find(class_="list feed-section__content feed-section__content--category")

    # Scrapes data from website
    headlines = vsHeadlines(data)
    categories = vsCategories(data)
    timeAgo = vsTimeAgo(data)

    return headlines, categories, timeAgo  # Returns data


def vsHeadlines(data):
    '''Scrapes headlines from Vancouver Sun'''
    headlineData = data.find_all(class_="article-card__headline-clamp")
    headlines = []

    for num in range(len(headlineData)):
        if len(headlines) < 3:  # Limits headlines to first 3
            headlines.append(headlineData[num].get_text())  # Adds each title to the headlines list

    return headlines


def vsCategories(data):
    '''Scrapes categories from Vancouver Sun'''
    categoryData = data.find_all(class_="article-card__category-link")
    categories = []

    countedOnce = False
    for num in range(len(categoryData)):
        if len(categories) < 3:  # Limits categories to first three
            if not countedOnce: # To avoid repeats in the list
                category = categoryData[num].get_text()
                category = category.strip()
                categories.append(category)  # Adds category to list
                countedOnce = True
            elif countedOnce:
                # Skips every other entry (since it's a repeat)
                countedOnce = False

    return categories


def vsTimeAgo(data):
    '''Scrapes time posted info from Vancouver Sun'''
    timeData = data.find_all(class_="article-card__time")
    timeAgo = []

    for num in range(len(timeData)):
        if len(timeAgo) < 3:  # Limits time entries to first 3
            time = str(timeData[num].get_text()).strip()
            time = time.replace(u'\xa0', u' ')
            timeAgo.append(time)  # Adds each time to the timeAgo list

    return timeAgo


def scrapeNatPost():
    '''Scrapes The National Post to return latest 5 headlines, category, and time since posted'''
    page = requests.get("https://nationalpost.com/")
    soup = BeautifulSoup(page.content, 'html.parser')

    data = soup.find(class_="list feed-section__content feed-section__content--category")

    # Scrapes data from website
    headlines = npHeadlines(data)
    categories = npCategories(data)
    timeAgo = npTimeAgo(data)

    return headlines, categories, timeAgo  # Returns data


def npHeadlines(data):
    '''Scrapes headlines from The National Post'''
    headlineData = data.find_all(class_="article-card__headline-clamp")
    headlines = []

    for num in range(len(headlineData)):
        if len(headlines) < 3:  # Limits headlines to first 3
            headlines.append(headlineData[num].get_text())  # Adds headlines to list

    return headlines


def npCategories(data):
    '''Scrapes categories from The National Post'''
    categoryData = data.find_all(class_="article-card__category-link")
    categories = []

    countedOnce = False
    for num in range(len(categoryData)):
        if len(categories) < 3:  # Limits categories to first 3
            if not countedOnce:  # To avoid repeats in the list
                category = categoryData[num].get_text()
                category = category.strip()
                categories.append(category)  # Adds category to list
                countedOnce = True
            elif countedOnce:
                # Skips every other entry (since it's a repeat)
                countedOnce = False

    return categories


def npTimeAgo(data):
    '''Scrapes time posted info from The National Post'''
    timeInfo = data.find_all(class_="article-card__time")
    timeAgo = []

    for num in range(len(timeInfo)):
        if len(timeAgo) < 3:  # Limits time entries to first 3
            time = timeInfo[num].get_text().strip()
            time = time.replace(u'\xa0', u' ')
            timeAgo.append(time)  # Adds time to the list

    return timeAgo


def scrapeNewegg():
    '''Scrapes Newegg and returns info about today's deals'''
    page = requests.get("https://www.newegg.ca/todays-deals")
    soup = BeautifulSoup(page.content, 'html.parser')

    data = soup.find(class_="item-cells-wrap tile-cells five-cells")

    # Scrapes data from website
    itemNames = scrapeName(data)
    ogPrices = scrapeOgPrice(data)
    newPrices = scrapeNewPrice(data)
    shippingPrices = scrapeShipping(data)
    discounts = scrapeDiscount(data)

    return itemNames, ogPrices, newPrices, shippingPrices, discounts  # Returns data


def scrapeName(data):
    '''Scrapes discounted item names from Newegg'''
    itemData = data.find_all(class_="item-title")
    global itemNames
    itemNames = []

    for num in range(len(itemData)):
        itemNames.append(itemData[num].get_text())  # Adds name to itemNames list

    return itemNames


def scrapeOgPrice(data):
    '''Scrapes original prices of discounted items'''
    ogPriceData = data.find_all(class_="price-was")
    global ogPrices
    ogPrices = []

    for num in range(len(ogPriceData)):
        if ogPriceData[num].get_text() == '':
            # Since they also put new items with no original price on the list
            ogPrices.append('N/A')
        else:
            ogPrices.append(ogPriceData[num].get_text())  # Stores price in ogPrices list

    return ogPrices


def scrapeNewPrice(data):
    '''Scrapes new prices of discounted items'''
    newPriceData = data.find_all(class_="price-current")
    global newPrices
    newPrices = []

    for num in range(len(newPriceData)):
        if newPriceData[num].get_text() == '':
            # Since they also put promo deals with no new price on the list
            newPrices.append('N/A')
        else:
            wordList = newPriceData[num].get_text().split()  # To get rid of the hyphen at the end of the amount
            newPrices.append(wordList[0])  # Stores current price in newPrices list

    return newPrices


def scrapeShipping(data):
    '''Scrapes shipping prices of discounted items'''
    shippingData = data.find_all(class_="price-ship")
    global shippingPrices
    shippingPrices = []

    for num in range(len(shippingData)):
        shippingPrices.append(shippingData[num].get_text())  # Stores shipping price in the list

    return shippingPrices


def scrapeDiscount(data):
    '''Scrapes discount percentage of items'''
    discountData = data.find_all(class_="price-save")
    global discounts
    discounts = []

    for num in range(len(discountData)):
        disc = discountData[num].get_text()

        if disc == '':
            # Since discounts aren't always provided
            disc = 'N/A'
        else:  # If there is a discount provided
            words = disc.split(' ')
            disc = words[1]  # Removes the "Save: " from the string

        discounts.append(disc)  # Stores percentage (or N/A) in discounts list

    return discounts

