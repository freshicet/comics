import feedparser
import requests
from bs4 import BeautifulSoup
import re

d = feedparser.parse('http://www.giantitp.com/comics/oots.rss')

url =  d.entries[0].link
number = url[-9:] 
number = number[:4]
page = requests.get("http://www.giantitp.com/comics/oots.html").content
soup = BeautifulSoup(page, "html5lib")
comicImageBlock = soup.find("p",{"class":"ComicList"})
comicTitle = comicImageBlock.text

page = requests.get(url).content

soup = BeautifulSoup(page, "html5lib")
 
images = soup.find_all("img", {"src":re.compile(number+".png")})
 
images = images[0]
comicURL = images['src']

comicURL = 'http://www.giantitp.com' + comicURL
