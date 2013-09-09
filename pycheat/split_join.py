import sys

sentence = "Cats in the cradle"
print sentence.split()
print sentence.split(',')

#Split words separated by a string:
sentence="theONEcatONEcradleONE"
print sentence.split("ONE")

#Split only the first two words in a comma separated string
sentence = "cat,in,the,dark"
print sentence.split(',',2)



print sentence.swapcase()
print sentence.replace('the','one')
