# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:45:54 2013

@author: ozdemircili
"""

"""
Install as:

pip install wikipedia

"""

import wikipedia

# Search
wikipedia.search("Python")
wikipedia.search("Google", results=3)
wikipedia.search("codensys, results=2,suggest=True)

#Get random page
wikipedia.random(pages=1)

#Search Python with autosuggest and allowing redirection without error
wikipedia.summary("Python",auto_suggest=True, redirect=True)

#Donate to wikipedia.Opens a webpage to donate.
wikipedia.donate()


#Wikipedia.page example
tr = wikipedia.page("Turkey")
print tr.title
print tr.url
print tr.content
print tr.images[0]
print tr.links[0]

#Change Language
wikipedia.set_lang("sp")

#Olympics 2013 - Spain.. Remember??

print wikipedia.summary("Cafe con Leche - Ana Botin")


