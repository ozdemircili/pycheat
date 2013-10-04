# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:44:50 2013

@author: ozdemircili
"""

from text.blob import TextBlob

text = TextBlob("Once upon a time a there was a program called Pycheat.It was one of the cheats")

text.tags

text.noun_phrases

text.sentiment

text.words

text.sentences

text.title

text.words[-1].singularize()
text.words[3].pluralize()


from text.blob import Word 
from text.blob import Verb

#Lemmatization
w = Word("octopi")
w.lemma

#Spelling Correction
a = TextBlob("I aem one oef a kind cheat")
print(a.correct())

t = Word('Astonised')
t.spellcheck()

#Word counts
text = TextBlob("One time there was this pycheat in github. And it was Github where all the cheats were")
text.word_counts['github']

#Translation
text = TextBlob("Frankly!Can I get a cup of coffe con leche in plaza Mayor?")
text.detect_language()
text.translate( to="es")

#Parsing

text.parse()

#Fetch words
text[0:7]

#Capital letters
text.upper()
text.lower()

#Find
text.find("leche")

#Get succesive words

text.ngrams(n=3)

#Get in json format

text.json()