# -*- coding: utf-8 -*-
'''
Created on Mon Sep  2 17:20:12 2013

@author: ozdemircili
'''

#Reference http://docs.python.org/2/library/time.html#time.strftime

import datetime

now = datetime.datetime.now()

print
print "Current date and time using str method of datetime object:"
print str(now)

print
print "Current date and time using instance attributes:"
print "Current year: %d" % now.year
print "Current month: %d" % now.month
print "Current day: %d" % now.day
print "Current hour: %d" % now.hour
print "Current minute: %d" % now.minute
print "Current second: %d" % now.second
print "Current microsecond: %d" % now.microsecond

print
print "Current date and time using strftime:"
print now.strftime("%Y-%m-%d %H:%M")

print "You can change what you want to see using:"
print now.strftime('%U,%a,%X %x %Z,%Y,%w,%W')


#Or you can do this:

from datetime import datetime

now = datetime.now()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)

print mm,dd,yyyy,hour,mi,ss




