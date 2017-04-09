#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

title = 'Cradboard Crack'
homepage = 'http://cardboard-crack.com/'
page = requests.get(homepage).content
soup = BeautifulSoup(page, 'html5lib')
comicImageBlock = soup.find('div', {'class': 'stat-media-wrapper'})
comicImageTag = comicImageBlock.find('img')
comicURL = comicImageTag['src']
comicTitle = title