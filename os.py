import os
print os.getcwd()
f = os.uname()

print f
os.chdir('/etc/')
print os.getcwd()
