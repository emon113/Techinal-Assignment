import requests
from bs4 import BeautifulSoup

web_urls = ["https://gratisography.com/page/2/", "https://www.reshot.com/free-stock-photos/search/animal/", "https://picography.co/search/cat"]   # List of website urls
search_tags = ["retro","african","svg","cat"]               # List of search  tag

for web_page in web_urls:                                   # For loop for iterate over the website URLs
    html_file = requests.get(url=web_page).text             # Getting the HTML file of the webpage.
    soup = BeautifulSoup(html_file,"html.parser")           # Creating an instance of BeautifulSoup with the HTML file and 'html.parser' is used as a parser.
    img_tags = soup.find_all('img', alt=True)               # Finding all the img tag along with the 'alt'.   

    for img in img_tags:                                    # For loop to iterate over the img tag.
        for tag in search_tags:                             # for loop to iterate over the search tags.
            if tag in img['src'] or tag in img['alt']:      # Cheecking if the image file or image alt matches with the tag or not.
                print(img['src'])                           # If matches the image URL will be printed
