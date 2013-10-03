# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 17:21:27 2013

@author: ozdemircili
"""

import smtplib

sender = 'pycheat@codensys.com'
receivers = ['code@codensys.com']

message = """ Testing smtp"""

smtpObj = smtplib.SMTP('localhost')
smtpObj.sendmail(sender , receivers, message)
print "Success!"


    