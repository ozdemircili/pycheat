

from elementtree import ElementTree as ET
import urllib2

#  C:\Users\Ozgur\Desktop\Python\sysmon.xml
#Example xml


#You can open URL to get the xml with urlib2:
xmlfile = urllib2.urlopen('http://server/allSystems.xml')

tree = ET.ElementTree(file=xmlfile)

root = tree.getroot()

root.tag
root.attrib

# Find and print all servers
for child in root.findall('server'):
    name = child.find('name').text
    ip = child.find('ip').text
    print name, ip

#Find audit = 1 and print condition
for child in root.findall('server'):
    name = child.find('name').text
    ip = child.find('ip').text
    audit = child.find('auditd').text
    print name, ip, audit
    if audit.find('0'):
        print "Not ok", name, ip
    else:
        print "ok"

#Find an ip

for node in tree.findall('.//systems/server'):
    aud = node.attrib.getall('auditd')
if aud != 1:
    print "ALLRIGHT", name, ip, audit
