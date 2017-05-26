#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import lxml

title = 'The Perry Bible Fellowship'
homepage = 'http://pbfcomics.com'
url = homepage

page = requests.get(url).content
soup = BeautifulSoup(page, 'lxml')
comicImageBlock = soup.find('div', {'id': 'comic'})
comicImageTag = comicImageBlock.find('img')
comicURL = comicImageTag['src']
comicTitle = comicImageTag['alt']
