#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

title = 'Buttersafe'
homepage = 'http://buttersafe.com/'
page = requests.get(homepage).content
soup = BeautifulSoup(page, 'html5lib')
comicImageBlock = soup.find('div', {'id': 'comic'})
comicImageTag = comicImageBlock.find('img')
comicURL = comicImageTag['src']
comicTitle = comicImageTag['alt']
comicTitle = comicTitle.encode('utf-8')