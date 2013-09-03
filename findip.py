
import netifaces
import os 
import commands


"""
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
"""

#commands.getoutput("route -n | grep 'UG[ \t]' | awk '{print $2}'")
#os.system("route -n | grep 'UG[ \t]' | awk '{print $2}'")
#print(socket.gethostbyname(socket.gethostname()))
print "Your gateway is: " + str(gateway)

import netifaces as ni
#print ni.interfaces()
#print ni.ifaddresses('eth0')
#print  ni.ifaddresses.__doc__
#formatedip= ni.ifaddresses('eth0')[2][0]['addr']

print "Your ip is: " + str(formatedip)

commands.getoutput()
