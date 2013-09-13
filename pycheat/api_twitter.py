# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:38:20 2013

@author: ozdemircili
"""

"""

Install:

pip install twitter

"""

import twitter

# see "Authentication" section below for tokens and keys
t = Twitter(
            auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                       CONSUMER_KEY, CONSUMER_SECRET)
           )

# Get your "home" timeline
t.statuses.home_timeline()

# Get a particular friend's timeline
t.statuses.friends_timeline(id="billybob")

# Also supported (but totally weird)
t.statuses.friends_timeline.billybob()

# to pass in GET/POST parameters, such as `count`
t.statuses.home_timeline(count=5)

# to pass in the GET/POST parameter `id` you need to use `_id`
t.statuses.oembed(_id=1234567890)

# Update your status
t.statuses.update(
    status="Using @sixohsix's sweet Python Twitter Tools.")

# Send a direct message
t.direct_messages.new(
    user="billybob",
    text="I think yer swell!")

# Get the members of tamtar's list "Things That Are Rad"
t._("tamtar")._("things-that-are-rad").members()

# Note how the magic `_` method can be used to insert data
# into the middle of a call. You can also use replacement:
t.user.list.members(user="tamtar", list="things-that-are-rad")

# An *optional* `_timeout` parameter can also be used for API
# calls which take much more time than normal or twitter stops
# responding for some reasone
t.users.lookup(screen_name=','.join(A_LIST_OF_100_SCREEN_NAMES), _timeout=1)

# Overriding Method: GET/POST
# you should not need to use this method as this library properly
# detects whether GET or POST should be used, Nevertheless
# to force a particular method, use `_method`
t.statuses.oembed(_id=1234567890, _method='GET')


# Search for the latest tweets about #pycon
t.search.tweets(q="#pycon")


#Using the returned data
x = twitter.statuses.home_timeline()

# The first 'tweet' in the timeline
x[0]

# The screen name of the user who wrote the first 'tweet'
x[0]['user']['screen_name']

#Generate raq data
twitter = Twitter(format="xml")


#Retrive all messages from users stream

auth = OAuth(
    consumer_key='[your consumer key]',
    consumer_secret='[your consumer secret]',
    token='[your token]',
    token_secret='[your token secret]'
)
twitter_userstream = TwitterStream(auth=auth, domain='userstream.twitter.com')
for msg in twitter_userstream.user():
    if 'direct_message' in msg:
        print msg['direct_message']['text']
        
        
