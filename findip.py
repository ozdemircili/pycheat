
import os 
import socket
import netifaces as ni

"""
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
"""

os.system("route -n | grep 'UG[ \t]' | awk '{print $2}'") 


#print "Your gateway is: " str('gateway')

local = (socket.gethostbyname(socket.gethostname()))

print "Wow your local ip interestingly shows:" + str(local)


#Let`s get the interfaces and eth ip

int = ni.interfaces()
print "your interfaces are:" + str(int)
formatedip= ni.ifaddresses('eth0')[2][0]['addr']
print "Your ip is: " + str(formatedip)

