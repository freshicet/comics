#!/usr/bin/python
# -*- coding: utf-8 -*-
import feedparser
import requests
from bs4 import BeautifulSoup
import re
title = 'Flaky Pastry'
homepage = 'http://flakypastry.runningwithpencils.com/'
page = requests.get(homepage).content
soup = BeautifulSoup(page, 'html5lib')

images = soup.find_all('img', {'src': re.compile('Falingard.jpg')})

for x in images:
    comicURL = x['src']


comicTitle = title
comicURL = homepage + comicURL


lis = 'http://flakypastry.runningwithpencils.com/flakypastryrssxml'
d = feedparser.parse(lis)
s = d.entries
print s
