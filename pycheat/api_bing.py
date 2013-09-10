"""
Created on Tue Sep 10 11:34:59 2013

@author: ozdemircili
"""
"""
Do not forget to install the API by:

pip install pybing

"""

from pybing import Bing

bing = Bing('<addyourappidhere')
response = bing.search.web('pycheat github')
print response['SearchResponse']['Web']['Total']
results = response['SearchResponse']['Web']['Results']
print len(results)