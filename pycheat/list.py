import os
import sys
L = ['yellow','red','blue','green','black']

print L

#Slice
print L[0]

print L[1:-1]

#Lenght
print len(L)

#Insert 
L.insert(0,"white")
print L

#Remove
L.remove("white")

print L

#Reverse
L.reverse()

print L

#Count
L.count('red')

print L


#If clause
if 'red' in L:
	print "List contains", 'red'


@profile
	def test():
	L.count('red')

