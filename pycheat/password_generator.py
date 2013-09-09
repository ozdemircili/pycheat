__author__ = 'ozdemircili'

#Other ways of doing it is calling a sys param
#os.system('< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-16};echo;')


import random
import sys

def main(argv):

	if (len(sys.argv) != 2):
		sys.exit('Usage: simple_pass.py <password_length>')

	password = ''
	for i in range(int(argv[0])):
		password += chr(random.randint(33,126))

	print 'You new password is: ' + password

if __name__ == "__main__":
	main(sys.argv[1:])
