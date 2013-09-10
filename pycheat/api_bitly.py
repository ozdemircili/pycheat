# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:06:46 2013

@author: ozdemircili
"""

"""
You can install the api by:

sudo pip install bitly_api

"""
import bitlyapi
import sys
 
#Add Api data
 
API_USER = "your_api_username"
API_KEY = "your_api_key"
 
b = bitlyapi.BitLy(API_USER, API_KEY)
 
# Define how to use the program
 
usage = """Usage: python api_bitly.py [url]
python api_bitly.py https://github.com/ozdemircili/pycheat/"""
 
if len(sys.argv) != 2:
    print usage
    sys.exit(0)
 
longurl = sys.argv[1]
 
response = b.shorten(longUrl=longurl)
 
print response['url']
