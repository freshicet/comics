#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
title = 'Girl Genius'
homepage = 'http://www.girlgeniusonline.com/comic.php'
page = requests.get(homepage).content
soup = BeautifulSoup(page, 'html5lib')
comicImageBlock = soup.find('div', {'id': 'comicbody'})
comicImageTag = comicImageBlock.find('img')
comicURL = comicImageTag['src']
comicTitle = comicImageTag['alt']