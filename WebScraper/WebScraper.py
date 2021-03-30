from bs4 import BeautifulSoup
import requests

def scrapeCNN():
    "Scrapes CNN to return top 3 headlines, category, and time since posted"
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
            timeAgo.append(postInfo[num].get_text())  # Adds next element to the time list
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
            wordList.append(categoryData[num + 1].get_text())  # Adds the category to this one
            word = ' '.join(wordList)  # Joins words back into a single element
            categories.append(word)
        else:  # If a hyphen was not in the element
            pastWordList = categoryData[num - 1].get_text().split()  # Gets info of the past element
            if '-' not in pastWordList:  # If there isn't a hyphen in that one either
                categories.append(categoryData[num].get_text())

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
        # TODO: Figure out how to get time since posted rather than date of post
        timeAgo.append(timeData[num].get_text())  # Adds each element to the headlines list

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
        timeAgo.append(timeData[num].get_text())  # Adds each time to the timeAgo list

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
        timeAgo.append(timeInfo[num].get_text())  # Adds time to the list

    return headlines, categories, timeAgo