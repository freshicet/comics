#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

title = 'Axe Cop'
homepage = 'http://axecop.com/'
page = requests.get(homepage).content
soup = BeautifulSoup(page, 'html5lib')
comicImageBlock = soup.find('div', {'id': 'comic'})
comicImageTag = comicImageBlock.find('img')
comicURL = comicImageTag['src']
comicTitle = comicImageTag['title']
