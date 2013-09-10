# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:25:56 2013

@author: ozdemircili
"""

import codecs

p = u"Я говорю по-русски"

print p

#This will create a file called learningrussian.txt in utf-8
with codecs.open("learningrussian.txt","w","utf-8") as stream: 
    stream.write(p + u"\n")
    