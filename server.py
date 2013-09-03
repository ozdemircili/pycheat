#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 6878                # Reserve a port for your service.
yourip = socket.getfqdn()
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   print 'Your ip is', yourip
   c.send('Thank you for connecting' )
   c.send('Hey your address is'+ yourip )
   c.close()                # Close the connection


