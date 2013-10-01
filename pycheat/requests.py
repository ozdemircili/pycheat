# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/ozdemircili/.spyder2/.temp.py
"""

import requests
import json




r = requests.get('https://api.github.com/user', auth=('ozdemircili','mypass'))
r.status_code

if r.status_code == 200:
    print "That`s a 200! You`re logged in!"
else:
    print "Opps! Wrong user or pass"

print r.content

#Let`s open it in json for better formatting

data = json.loads(r.content)

print data

#Get a piece of info and print it

print "Your url is " + data['url']