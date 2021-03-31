from bs4 import BeautifulSoup
import datetime
from datetime import datetime as dt
from datetime import timezone
import requests

def scrapeGbNews():
    "Scrapes Global News to return top 3 headlines, category, and time since posted"
    page = requests.get("https://globalnews.ca/")
    soup = BeautifulSoup(page.content, 'html.parser')

    data = soup.find(class_="c-posts c-posts--tile c-posts--grid c-posts--gridMosaic c-posts--highlightFirst l-section__posts")

    # Scrapes headline info
    headlineData = data.find_all(class_="c-posts__headlineText")
    headlineData.pop(0)  # Gets rid of the repeated first header

    headlines = []

    for num in range(len(headlineData)):
        headlines.append(headlineData[num].get_text())  # Adds each headline to the list

    # Scrapes category & time info
    postInfo = data.find_all(class_="c-posts__info")

    categories = []

    timeAgo = []

    # To track which element is a category & time (since it alternates)
    didCategory = False
    didTime = True

    for num in range(len(postInfo)):
        if not didCategory:
            categories.append(postInfo[num].get_text())  # Adds first element to category list
            didCategory = True
            didTime = False
        elif not didTime:
            timeAgo.append(postInfo[num].get_text() + " ago")  # Adds next element to the time list
            didCategory = False
            didTime = True

    return headlines, categories, timeAgo


def scrapeCBC():
    "Scrapes CBC to return top 4 headlines, category, and time since posted"
    page = requests.get("https://www.cbc.ca/news/canada")
    soup = BeautifulSoup(page.content, 'html.parser')

    data = soup.find(class_="featuredTopStories sclt-featuredTopStories")

    # Scrapes headline info
    headlineData = data.find_all(class_="headline")
    headlines = []

    for num in range(len(headlineData)):
        headlines.append(headlineData[num].get_text())  # Adds each element to the headlines list

    # Scrapes category info
    categoryData = data.find_all(class_="departmentItem")
    categories = []

    for num in range(len(categoryData)):
        wordList = categoryData[num].get_text().split()  # Splits the element into its separate words

        if '-' in wordList:  # If a hyphen was in the element
            wordList.append(categoryData[num + 1].get_text())  # Adds the next category element to this one
            word = ' '.join(wordList)  # Joins words back into a single element
            categories.append(word)
        else:  # If a hyphen was not in the element
            pastWordList = categoryData[num - 1].get_text().split()  # Gets info of the past element
            if '-' not in pastWordList:  # If there isn't a hyphen in that one either
                categories.append(categoryData[num].get_text())
            # If there was a hyphen in the previous element, it's assumed that the current one has been added to that

    # To take out the space at the end of each category
    index = 0
    for i in categories:
        splitWord = i.split()
        joinWord = ' '.join(splitWord)
        categories[index] = joinWord
        index += 1

    # Scrapes time info
    timeData = data.find_all("time", {"class": "timeStamp"})
    timeAgo = []

    for num in range(len(timeData)):
        singleEntry = str(timeData[num])
        prunedData = singleEntry.split(' ')
        prunedData = prunedData[2].split('"')
        time = prunedData[1].split('T')
        hms = time[1].split('Z')
        hms = hms[0]
        time.pop()
        time.append(hms)
        now = str(dt.now(tz=timezone.utc)).split("+")
        now = now[0].split(" ")

        ymd = time[0].split("-")
        hms = time[1].split(":")

        ymdNow = now[0].split("-")
        hmsNow = now[1].split(":")

        a = datetime.datetime(int(ymd[0]), int(ymd[1]), int(ymd[2]), int(hms[0]), int(hms[1]), int(float(hms[2])))
        b = datetime.datetime(int(ymdNow[0]), int(ymdNow[1]), int(ymdNow[2]), int(hmsNow[0]), int(hmsNow[1]), int(float(hmsNow[2])))
        timeDiff = b - a

        timeDiff = str(timeDiff).split(":")
        if int(timeDiff[0]) > 0:
            if int(timeDiff[1]) >= 30:
                timeDiff = str(int(timeDiff[0]) + 1)
            else:
                timeDiff = timeDiff[0]
            if int(timeDiff) == 1:
                timeAgo.append(f"{timeDiff} hour ago")
            else:
                timeAgo.append(f"{timeDiff} hours ago")
        else:
            timeDiff = timeDiff[1]
            if int(timeDiff) == 1:
                timeAgo.append(f"{timeDiff} minute ago")
            else:
                timeAgo.append(f"{timeDiff} minutes ago")

    return headlines, categories, timeAgo

def scrapeVanSun():
    "Scrapes Vancouver Sun to return latest 5 headlines, category, and time since posted"
    page = requests.get("https://vancouversun.com/")
    soup = BeautifulSoup(page.content, 'html.parser')

    data = soup.find(class_="list feed-section__content feed-section__content--category")

    # Scrapes headline info
    headlineData = data.find_all(class_="article-card__headline-clamp")
    headlines = []

    for num in range(len(headlineData)):
        headlines.append(headlineData[num].get_text())  # Adds each title to the headlines list

    # Scrapes category info
    categoryData = data.find_all(class_="article-card__category-link")
    categories = []

    countedOnce = False
    for num in range(len(categoryData)):
        # Because I noticed repeats in the list
        if not countedOnce:
            category = categoryData[num].get_text()
            category = category.strip()  # Takes away whitespace
            categories.append(category)  # Adds category to list
            countedOnce = True
        elif countedOnce:
            countedOnce = False
            # Skips every other entry (since it's a repeat)

    # Scrapes time info
    timeData = data.find_all(class_="article-card__time")
    timeAgo = []

    for num in range(len(timeData)):
        time = str(timeData[num].get_text()).strip()
        time = time.replace(u'\xa0', u' ')
        timeAgo.append(time)  # Adds each time to the timeAgo list

    return headlines, categories, timeAgo


def scrapeNatPost():
    """Scrapes The National Post to return latest 5 headlines, category, and time since posted"""
    page = requests.get("https://nationalpost.com/")
    soup = BeautifulSoup(page.content, 'html.parser')

    data = soup.find(class_="list feed-section__content feed-section__content--category")

    # Scrapes headline info
    headlineData = data.find_all(class_="article-card__headline-clamp")
    headlines = []

    for num in range(len(headlineData)):
        headlines.append(headlineData[num].get_text())  # Adds headlines to list

    # Scrapes category info
    categoryData = data.find_all(class_="article-card__category-link")
    categories = []

    countedOnce = False
    for num in range(len(categoryData)):
        # Because I noticed repeats in the list
        if not countedOnce:
            category = categoryData[num].get_text()
            category = category.strip()  # Takes away whitespace
            categories.append(category)  # Adds category to list
            countedOnce = True
        elif countedOnce:
            countedOnce = False
            # Skips every other entry (since it's a repeat)

    # Scrapes time info
    timeInfo = data.find_all(class_="article-card__time")
    timeAgo = []

    for num in range(len(timeInfo)):
        time = timeInfo[num].get_text().strip()  # Takes away whitespace
        time = time.replace(u'\xa0', u' ')
        timeAgo.append(time)  # Adds time to the list

    return headlines, categories, timeAgo


def scrapeNewegg():
    page = requests.get("https://www.newegg.ca/todays-deals")
    soup = BeautifulSoup(page.content, 'html.parser')

    data = soup.find(class_="item-cells-wrap tile-cells five-cells")

    # Scrape discounted item info
    itemData = data.find_all(class_="item-title")
    global itemNames
    itemNames = []

    for num in range(len(itemData)):
        itemNames.append(itemData[num].get_text())

    # Scrapes original price
    ogPriceData = data.find_all(class_="price-was-data")
    global ogPrices
    ogPrices = []

    for num in range(len(ogPriceData)):
        ogPrices.append(ogPriceData[num].get_text())  # Stores price in ogPrices list

    # Scrapes new price
    newPriceData = data.find_all(class_="price-current")
    global newPrices
    newPrices = []

    for num in range(len(newPriceData)):
        wordList = newPriceData[num].get_text().split()  # To get rid of the hyphen at the end of the amount
        newPrices.append(wordList[0])  # Stores current price in newPrices list

    # Scrapes discount info
    discountData = data.find_all(class_="price-was-data")
    global discounts
    discounts = []

    for num in range(len(discountData)):
        discounts.append(discountData[num].get_text())  # Stores percentage in discounts list

