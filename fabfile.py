
# First we import the Fabric api
from fabric.api import *

# We can then specify host(s) and run the same commands across those systems
env.user = 'user'

env.password = 'pass'

env.hosts = [
    'xxx.xxx.xxx.xxx',
    'xxx.xxx..xxx.xxx',
    ]

#Roles fab -R command
env.roledefs = {
    'tomcat_servers' : ['server01','server02']
}

#Restrict the role to chamans only
@roles('tomcat_servers')

def uptime():
    run("uptime")
    
def hostnameip():
    run("hostname")
    put('ip.sh', '/tmp/')
    run('/bin/bash /tmp/ip.sh')
    sudo('whoami')
def anonymous():
    run("uname -a")
    


def hello():
	print("Hello World")


