#!/usr/bin/python
# -*- coding: utf-8 -*-
import feedparser
import requests
from bs4 import BeautifulSoup
import re

title = 'The Perry Bible Fellowship'
homepage = 'http://pbfcomics.com'
d = feedparser.parse('http://pbfcomics.com/feed/feed.xml')

url = d.entries[0].link

page = requests.get(url).content
soup = BeautifulSoup(page, 'html5lib')
comicImageBlock = soup.find('td', {'id': 'toptd'})
comicImageTag = comicImageBlock.find('img')
comicURL = comicImageTag['src']
comicTitle = comicImageTag['alt']

comicURL =  homepage + comicURL
