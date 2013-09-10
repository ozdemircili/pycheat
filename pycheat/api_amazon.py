# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:31:10 2013

@author: ozdemircili
"""

"""
Make sure you install boto as:

    Install via pip:

$ pip install boto

    Install via source code:

$ git clone git://github.com/boto/boto.git
$ cd boto
$ python setup.py install

"""

'''Create connection:'''
    
import boto
import boto.s3.connection
access_key = 'put your access key here!'
secret_key = 'put your secret key here!'

conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = 'objects.dreamhost.com',
        #is_secure=False,               # uncommmnt if you are not using ssl
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

''' Listing your buckets '''

for bucket in conn.get_all_buckets():
        print "{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
        )
        
''' Creating a bucket '''

bucket = conn.create_bucket('my-new-bucket')

''' Listing bucket content '''

for key in bucket.list():
        print "{name}\t{size}\t{modified}".format(
                name = key.name,
                size = key.size,
                modified = key.last_modified,
                )
                
'''Deleting a bucket'''

conn.delete_bucket(bucket.name)

'''Creating an object'''

key = bucket.new_key('pycheat.txt')
key.set_contents_from_string('Pycheat helpsalot!')

'''Deleting an object'''

bucket.delete_key('pycheat.txt')


'''Download an object'''

key = bucket.get_key('python.txt')
key.get_contents_to_filename('/home/ozdemircili/python.txt')
