import requests
import urllib
import time
from bs4 import BeautifulSoup, Comment
import re
import webbrowser


# page = requests.get("http://www.ozfoxes.com/fauxpas.htm").content

# soup = BeautifulSoup(page, "html5lib")

# comicImageBlock = soup.find("td",{"valign":"top"})

# comicImageTag = comicImageBlock.find("center")

# comicURL = comicImageTag['a']

# comicTitle = comicImageTag["href"]




# for comment in soup.findAll(text=lambda text:isinstance(text, Comment)):
    # if comment in ['PUT FACEBOOK SHARE HERE']:
        # print comment.next_element.strip()

webbrowser.open_new_tab("http://www.ozfoxes.com/fauxpas.htm")


