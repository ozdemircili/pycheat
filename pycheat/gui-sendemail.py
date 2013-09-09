""" If you need to do something irregularly, randomly during the weekday, you
often forget. This script gives you mail, sms or popup window indefinitely in
random interval to remind you of doing it. It runs forever. If you want to
send emails, uncomment the row sendMail() and fill variable me, to, smtp,
name, login in function sendMail(). """

# -*- coding: utf-8 -*-
import time, random, sys, os, smtplib

if sys.version < '3':
    from Tkinter import *
else:
    from tkinter import *

# ----------------- variables ----------------------------------
mytimefrom=6        # from 6 pm
mytimeto=22         # to 22  am
mydelayfrom=1*3600    # random delay in secs from
mydelayto=5*3600      # random delay in secs to
randommsgnext="randommsgnext.txt"     # place to save time of next message

# ----------------- defs ----------------------------------

def showMessage():
    # show reminder message window
    root=Tk()
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry("+%d+%d" % (x, y))
    root.protocol('WM_TAKE_FOCUS', root.update )
    root.wait_visibility(root)
    root.attributes('-topmost',1)
    label=Label(root, text="Do what you should do.").pack({"side": "left"})
    button=Button(text="OK", width="10", command=lambda:root.destroy()).pack()
    root.mainloop()

def sendMail():
    # sends mail
    s = smtplib.SMTP(smtp)
    s.login(name, password)

    subject="Reminder"
    fromaddr=fromadr
    toaddrs= [toadr]
    text= "Do what you should do.\n%s" % time.ctime()
    msg = ("Subject: %s\nFrom: %s\nTo: %s\n\n%s" % (subject, fromaddr, ", ".join(toaddrs), text))

    s.sendmail(fromaddr, toaddrs, msg)
    s.quit()

def sendSMS():
    # sends sms
    message={'user': user, 'password': password, 'sender': fromnumber, 'recipient': tonumber, 'message': "goodbye"}
    if sys.version < '3':
        import urllib
        params = urllib.urlencode(message)
        f=urllib.urlopen(http, params)
    else:
        import urllib.parse
        import urllib.request
        params = urllib.parse.urlencode(message)
        f = urllib.request.urlopen(http % params)

def checktime(nowtime):
    # do not remind at night
    if nowtime.tm_hour<=mytimefrom or nowtime.tm_hour>=mytimeto:
        return False
    return True

def timenextwritef():
    # save next time in file
    f=open(randommsgnext,"a")
    timenext=time.mktime (nowtime)+delaysec
    f.write(time.ctime(timenext)+"\n")
    f.close()
    os.utime(randommsgnext, None)

# ----------------- main app ----------------------------------

nowtime=time.localtime()
os.chdir(os.path.dirname(sys.argv[0]))  # to have "randommsgnext" in the same dir

while True:
    delaysec=random.randint(mydelayfrom,mydelayto)
    timenextwritef()
    time.sleep(delaysec)
    nowtime=time.localtime()
    if checktime(nowtime):
#        sendSMS()
#        sendMail()    # uncomment if you want sending mails
        showMessage()

