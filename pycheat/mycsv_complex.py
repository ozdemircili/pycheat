import csv
f = open('csv/Master.csv', 'rb') # open the file
reader = csv.reader(f)
for row in reader:
	number = row[0]
	name = row[1]
	
	print number, name
#Add what ever character you wanht to seperatre
	print '?'.join(row)
	print ' '.join(row)
