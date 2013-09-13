# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:35:43 2013

@author: ozdemircili
"""

"""
Install SDK :

pip install dropbox

"""

# Include the Dropbox SDK
import dropbox

# Get your app key and secret from the Dropbox developer website
app_key = 'INSERT_APP_KEY'
app_secret = 'INSERT_APP_SECRET'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

# Have the user sign in and authorize this token
authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()

# This will fail if the user enters an invalid authorization code
access_token, user_id = flow.finish(code)

# List account info
client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()

#Upload files
f = open('working-draft.txt')
response = client.put_file('/magnum-opus.txt', f)
print "uploaded:", response

#Download files
f, metadata = client.get_file_and_metadata('/magnum-opus.txt')
out = open('magnum-opus.txt', 'w')
out.write(f.read())
out.close()
print metadata

