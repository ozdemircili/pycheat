# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:21:25 2013

@author: ozdemircili
"""

""" ConfigParser lets you read from and write to config files

install with:

pip install ConfigParser

For the example to work create parser.ini in the same directory and
add the following input:

[pyconfig]
url= www.codensys.com
project = pycheat
description = A Universal Python Sample Database


"""

''' Read Config files '''
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('parser.ini')

print parser.get('pyconfig','url')


''' Check if config files exists '''

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('parser.ini')

config_files = ['parser.ini','doesnotexist.ini']

found = parser.read(config_files)
missing = set(config_files) - set(found)

print 'Found config files:', sorted(found)
print 'Missing files     :', sorted(missing)


''' Test if values are present '''

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('parser.ini')

for sections in [ 'pyconfig', 'testing' ]:
    print '%-12s: %s' % (sections, parser.has_section(sections))
    
''' Compare results of the sections '''

""" Create types.ini file with the following content:

[ints]
positive = 1
negative = -5

[floats]
positive = 0.2
negative = -3.14

[booleans]
number_true = 1
number_false = 0
yn_true = yes
yn_false = no
tf_true = true
tf_false = false
onoff_true = on
onoff_false = false

"""

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('types.ini')

print 'Integers:'
for name in parser.options('ints'):
    string_value = parser.get('ints', name)
    value = parser.getint('ints', name)
    print '  %-12s : %-7r -> %d' % (name, string_value, value)

print '\nFloats:'
for name in parser.options('floats'):
    string_value = parser.get('floats', name)
    value = parser.getfloat('floats', name)
    print '  %-12s : %-7r -> %0.2f' % (name, string_value, value)

print '\nBooleans:'
for name in parser.options('booleans'):
    string_value = parser.get('booleans', name)
    value = parser.getboolean('booleans', name)
    print '  %-12s : %-7r -> %s' % (name, string_value, value)
    
    
    
''' Add sections to Config Files '''

import ConfigParser

parser = ConfigParser.SafeConfigParser()

parser.add_section('newsection')
parser.set('newsection', 'url', 'http://www.codensys.com')
parser.set('newsection', 'username', 'ozdemircili')
parser.set('newsection', 'password', 'reallysecret')

for section in parser.sections():
    print section
    for name, value in parser.items(section):
        print '  %s = %r' % (name, value)
        
        
        
''' Remove sections from Config Files '''

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('type.ini')

print 'Read values:\n'
for section in parser.sections():
    print section
    for name, value in parser.items(section):
        print '  %s = %r' % (name, value)
        
parser.remove_option('booleans', 'number_true')
parser.remove_section('floats')
        
print '\nModified values:\n'
for section in parser.sections():
    print section
    for name, value in parser.items(section):
        print '  %s = %r' % (name, value)
