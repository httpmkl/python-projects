from bs4 import BeautifulSoup
import requests

def scrapeCNN():
    "Scrapes CNN to return top 3 headlines, category, and time since posted"
    page = requests.get("https://globalnews.ca/")
    soup = BeautifulSoup(page.content, 'html.parser')

    data = soup.find(class_="c-posts c-posts--tile c-posts--grid c-posts--gridMosaic c-posts--highlightFirst l-section__posts")
    headlineData = data.find_all(class_="c-posts__headlineText")
    headlineData.pop(0)  # gets rid of the repeated first header

    headlines = list()

    for num in range(len(headlineData)):
        headlines.append(headlineData[num].get_text())

    postInfo = data.find_all(class_="c-posts__info")
    categories = list()
    timeAgo = list()

    didCategory = False
    didTime = True

    for num in range(len(postInfo)):
        if not didCategory:
            categories.append(postInfo[num].get_text())
            didCategory = True
            didTime = False
        elif not didTime:
            timeAgo.append(postInfo[num].get_text())
            didCategory = False
            didTime = True

    return headlines, categories, timeAgo


def scrapeCBC():
    "Scrapes CBC to return top 4 headlines, category, and time since posted"

scrapeCBC()