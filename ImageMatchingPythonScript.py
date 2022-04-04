from openpyxl import LXML
import requests
from bs4 import BeautifulSoup

web_urls = ['https://www.geeksforgeeks.org/', 'http://olympus.realpython.org/profiles/aphrodite', 'https://stackoverflow.com/users/1490552/adem-%c3%96zta%c5%9f']
search_tags = ["ndi", "6-min", "aphrodite", "imgur"]

for web_page in web_urls:
    html_file = requests.get(url=web_page).text
    soup = BeautifulSoup(html_file,"lxml")
    images = soup.find_all('img', alt=True)

    for image in images:
        for tag in search_tags:
            if tag in image['src'] or tag in image['alt']:
                print(image['src'])
