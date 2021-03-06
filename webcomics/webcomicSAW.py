#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

title = 'Sandra and Woo'
homepage = 'http://www.sandraandwoo.com'
page = requests.get(homepage).content
soup = BeautifulSoup(page, 'html5lib')
comicImageBlock = soup.find('div', {'id': 'comic'})
comicImageTag = comicImageBlock.find('img')
comicURL = comicImageTag['src']
comicTitle = comicImageTag['alt']
comicURL = homepage + comicURL