#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

page = requests.get('http://threewordphrase.com/').content
soup = BeautifulSoup(page, 'html5lib')
comicImageBlock = soup.find('table', {'width': '403'})
comicImageTag = comicImageBlock.find('img')
comicURL = comicImageTag['src']
comicTitle = 'Thee Word Phrase'
comicURL = 'http://threewordphrase.com/' + comicURL