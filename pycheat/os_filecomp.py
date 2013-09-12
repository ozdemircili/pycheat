# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:32:30 2013

@author: ozdemircili
"""


import filecmp

first = raw_input("Enter the first file to compare")
second = raw_input("Enter the second file to compare")

print "Comparing files"
print filecmp.cmp(first, second, shallow=False)


''' Comparing directories '''

import filecmp

first = raw_input("Enter the first directory to compare")
second = raw_input("Enter the second directory to compare")

filecmp.dircmp(first, second).report_full_closure()

''' Comparing directories advanced '''

import filecmp

first = raw_input("Enter the first directory to compare")
second = raw_input("Enter the second directory to compare")

comp = filecmp.dircmp(first, second).report_full_closure()
print 'Common     :', comp.common
print 'Directories:', comp.common_dirs
print 'Files      :', comp.common_files
print 'Funny      :', comp.common_funny
