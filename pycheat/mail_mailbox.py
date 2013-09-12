# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:09:06 2013

@author: ozdemircili
"""
''' Creating Mailbox'''
import mailbox
import email.utils

from_addr = email.utils.formataddr(('Sender', 'pycheat@locahost'))
to_addr = email.utils.formataddr(('Receiver', 'ozdemircili@gmail.com'))

mbox = mailbox.mbox('myinbox.mbox')

mbox.lock()
try:
    msg = mailbox.mboxMessage()
    msg.set_unixfrom('author Sat Feb  7 01:05:34 2009')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Message 1'
    msg.set_payload('This is the body.\nFrom (should be escaped).\nThere are 3 lines.\n')
    mbox.add(msg)
    mbox.flush()

    msg = mailbox.mboxMessage()
    msg.set_unixfrom('author')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Message 2'
    msg.set_payload('This is the second body.\n')
    mbox.add(msg)
    mbox.flush()
finally:
    mbox.unlock()

print open('myinbox.mbox', 'r').read()


''' Reading Mailbox '''

import mailbox

mbox = mailbox.mbox('myinbox.inbox')
for message in mbox:
    print message
    

''' Removing messages from mbox '''

import mailbox

mbox = mailbox.mbox('myinbox.mbox')
to_remove = []
for key, msg in mbox.iteritems():
    if '2' in msg['subject']:
        print 'Removing:', key
        to_remove.append(key)
mbox.lock()
try:
    for key in to_remove:
        mbox.remove(key)
finally:
    mbox.flush()
    mbox.close()

print open('myinbox.mbox', 'r').read()


''' Reading a maildirbox '''
import mailbox

mbox = mailbox.Maildir('Example')
for message in mbox:
    print message['subject']
    
    
''' Maildir folders '''
import mailbox
import os

def show_maildir(name):
    os.system('find %s -print' % name)

mbox = mailbox.Maildir('Example')
print 'Before:', mbox.list_folders()
show_maildir('Example')

print
print '#' * 30
print

mbox.add_folder('subfolder')
print 'subfolder created:', mbox.list_folders()
show_maildir('Example')

subfolder = mbox.get_folder('subfolder')
print 'subfolder contents:', subfolder.list_folders()

print
print '#' * 30
print

subfolder.add_folder('second_level')
print 'second_level created:', subfolder.list_folders()
show_maildir('Example')

print
print '#' * 30
print

subfolder.remove_folder('second_level')
print 'second_level removed:', subfolder.list_folders()
show_maildir('Example')
