import os

#Needed for sudo
import subprocess
import shlex

uid = os.getuid()

print 'Your uid is' +  str(uid) 
username = os.system("whoami")

if username is  "root" :
	print ("r00tness!")

else:
	print("I cannot run as mortal")

#Get user input
filename = raw_input('Enter a file name: ')

#Print that name
print str(filename)

#DO something as root
subprocess.call(shlex.split('sudo id -nu'))

print "I can get root!! Allright!!"

