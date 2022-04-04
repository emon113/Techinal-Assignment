import requests
from bs4 import BeautifulSoup

web_urls = ["https://gratisography.com/page/2/", "https://www.reshot.com/free-stock-photos/search/animal/", "https://picography.co/search/cat"]
search_tags = ["retro","african","svg","cat"]

for web_page in web_urls:                                   # For loop for iterate over the website URLs
    html_file = requests.get(url=web_page).text             # Getting the HTML file of the webpage.
    soup = BeautifulSoup(html_file,"html.parser")           # Creating an instance of BeautifulSoup with the HTML file and 'html.parser' is used as a parser.
    images = soup.find_all('img', alt=True)                 # Finding all the img tag with the 'alt'.   

    for image in images:                                    # For loop to iterate over the img tag.
        for tag in search_tags:                             # for loop to iterate over the search tags.
            if tag in image['src'] or tag in image['alt']:  # Cheecking if the image file or image alt matches with the tag or not.
                print(image['src'])                         # If matches the image URL will be printed
