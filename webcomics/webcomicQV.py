#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
title = 'Quantum Vibe'
homepage = 'http://www.quantumvibe.com/'
page = requests.get(homepage).content
soup = BeautifulSoup(page, 'html5lib')
comicImageBlock = soup.find('div',
                            {'style': 'width: 422px; height 1125px; float: left; display: inline;  background-color: #282746; margin: 0 auto; padding-top: 5px; '
                            })
							
comicImageTag = comicImageBlock.find('img')
comicURL = comicImageTag['src']
comicTitle = comicImageTag['alt']
comicURL = homepage + comicURL