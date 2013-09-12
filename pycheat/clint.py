# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:25:49 2013

@author: ozdemircili
"""
"""
Installation:

pip install clint

"""

from clint.textui import colored, indent, puts

print 'Colored output ' + colored.yellow('pyt') + colored.blue('hon')

'''Indent Example'''
with indent(3, quote=colored.red(' >')):
    puts ('indent01')
    puts ('indent02')
    with indent(3, quote=colored.green(' |')):
        puts('that`s some juicy indent')
        puts('isn\'t?')
        
       
