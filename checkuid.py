import os

uid = os.getuid()

print 'Your uid is' +  str(uid) 
username = os.system("whoami")

if username is  "root" :
	print ("r00tness!")
else:
	print("I cannot run as mortal")

 


