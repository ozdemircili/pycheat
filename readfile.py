#pswd = file( "/etc/passwd", "r" )
#for aLine in pswd
#    fields= aLine.split( ":" )
#    print fields[0], fields[1]
#pswd.close()

# open file
f = open ("/etc/passwd","r")

#Read whole file into data
data = f.read()

# Print it
print data

# Close the file
f.close()


#Read /etc/hosts
hosts = open('hosts','r')
for line in hosts:
        print line.split()[0:]


print '\n'.join(line.split(":",1)[0] for line in open("hosts"))

#For each 
host = open('hosts','r')
	for i in host:
	print i 

