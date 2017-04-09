#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

title = 'Dinosaur Comics'
homepage = 'http://www.qwantz.com/index.php'
page = requests.get(homepage).content
soup = BeautifulSoup(page, 'html5lib')
comicImageBlock = soup.find_all('td', {'align': 'middle',
                                'valign': 'middle'})

for x in comicImageBlock:
    comicImageBlock = x
comicImageTag = comicImageBlock.find('img')
comicURL = comicImageTag['src']
comicTitle = comicImageTag['title']		