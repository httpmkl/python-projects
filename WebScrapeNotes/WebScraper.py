from bs4 import BeautifulSoup
import requests


page = requests.get("https://www.surreyschools.ca/Pages/default.aspx")  # retrieves the content of a webpage
soup = BeautifulSoup(page.content, 'html.parser')  # organizes the html into separate lines

data = soup.find(class_="hcf-rollup hcf-newsRollup")  # looks for subsection
subData = data.find_all('li')  # separates the subsections based on li tag

for num in range(len(subData)):
    # prints info under a tag in subsection (excludes date)
    print(subData[num].find('a').get_text())

'''

page = requests.get("https://jamesclear.com/articles")
soup = BeautifulSoup(page.content, 'html.parser')

data = soup.find(class_="all-articles__list")
print(data.get_text())

'''