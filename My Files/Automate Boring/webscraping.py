#webscraping

import bs4

import requests
res = requests.get('https://smile.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_3?crid=20D0B4V7XGJY1&dchild=1&keywords=automate+the+boring+stuff+with+python&qid=1591189820&sprefix=automate%2Caps%2C194&sr=8-3')
res.raise_for_status()

