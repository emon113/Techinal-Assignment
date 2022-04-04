from openpyxl import LXML
import requests
from bs4 import BeautifulSoup

web_urls = ["https://gratisography.com/page/2/", "https://www.reshot.com/free-stock-photos/search/animal/", "https://picography.co/search/cat"]
search_tags = ["retro","african","svg","cat"]

for web_page in web_urls:
    html_file = requests.get(url=web_page).text
    soup = BeautifulSoup(html_file,"lxml")
    images = soup.find_all('img', alt=True)

    for image in images:
        for tag in search_tags:
            if tag in image['src'] or tag in image['alt']:
                print(image['src'])
