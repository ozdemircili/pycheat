import sys, time
text = "Hi and welcome to pycheat. Why don`t you have a look at the examples?"
for character in text:
	sys.stdout.write(character)
	sys.stdout.flush()
	time.sleep(.08)

