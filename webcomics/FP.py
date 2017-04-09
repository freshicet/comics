###########################
# Work just for Flakypastry
###########################

#!/usr/bin/python
# -*- coding: utf-8 -*-
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

