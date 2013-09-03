import csv
import sys

file = open('hosts.csv', 'rt')
try:
    reader = csv.reader(file)
    for row in reader:
        print row

#If try fails give error and close
except ValueError:
        pass
finally:
    file.close()
