# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:18:01 2013

@author: ozdemircili
"""

from linkedin import linkedin

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
USER_TOKEN = ''
USER_SECRET = ''

RETURN_URL = '' # Not required for developer authentication

# Instantiate the developer authentication class

auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                USER_TOKEN, USER_SECRET, 
                                RETURN_URL, 
                                permissions=linkedin.PERMISSIONS.enums.values())

# Pass it in to the app...

app = linkedin.LinkedInApplication(auth)
# Use the app...

app.get_profile()


# Getting your connections
app.get_connections(selectors=['headline', 'first-name', 'last-name'], params={'start':10, 'count':5})


#SEARCHING

#Search profiles
application.search_profile(selectors=[{'people': ['first-name', 'last-name']}], params={'keywords': 'apple microsoft'})

#Search companies
application.search_company(selectors=[{'companies': ['name', 'universal-name', 'website-url']}], params={'keywords': 'apple microsoft'})

#Search jobs
application.search_job(selectors=[{'jobs': ['id', 'customer-job-code', 'posting-date']}], params={'title': 'python', 'count': 2})


#GROUPS

#Get grouo by id
app.get_group(41001)

#Get members of the group
app.get_memberships(params={'count': 20})

#Get posts 
app.get_posts(41001)


#COMPANY

#Get company
app.get_companies(company_ids=[1441], universal_names=['apple'], selectors=['name'], params={'is-company-admin': 'true'})

#Get updates about the company
app.get_company_updates(1441,params={'count': 2})

#Follow a compoany
app.follow_company(1441)

#Unfollow a company
app.unfollow_company(1441)


#JOBS

#Get information about a job offer
app.get_job(job_id=5174636)


#SHARE

#Share using api
application.submit_share('Posting from the API using JSON', 'Your title', None, 'http://www.linkedin.com', 'http://d.pr/3OWS')

#NETWORK

from linkedin.linkedin import NETWORK_UPDATES
print NETWORK_UPDATES.enums

update_types = (NETWORK_UPDATES.CONNECTION, NETWORK_UPDATES.PICTURE)
application.get_network_updates(update_types)


#INVITATION

#Invite a friend

from linkedin.models import LinkedInRecipient, LinkedInInvitation
recipient = LinkedInRecipient(None, 'john.doe@python.org', 'John', 'Doe')
print recipient.json

invitation = LinkedInInvitation('Hello John', "What's up? Can I add you as a friend?", (recipient,), 'friend')
print invitation.json

application.send_invitation(invitation)


