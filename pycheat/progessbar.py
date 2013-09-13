
import threading, sys, time
class loading_bar(threading.Thread):
        def run(self):
                global stop, kill
                sys.stdout.write("Loading....  ")
                sys.stdout.flush()
                type = 0
                while stop != True:
                        if type == 0: sys.stdout.write("\b/")
                        if type == 1: sys.stdout.write("\b-")
                        if type == 2: sys.stdout.write("\b\\")
                        if type == 3: sys.stdout.write("\b|")
                        type += 1
                        if type == 4: type = 0
                        sys.stdout.flush()
                        time.sleep(0.2)
                if kill == True: print "\b\b\b\b Aborting!"
                else: print "\b\b done!"
stop = kill = False
loading_bar_control = loading_bar()
loading_bar_control.start()
try:
        ##################################
        # Your processing code goes here #
        ##################################
except KeyboardInterrupt or EOFError:
        kill = True; stop = True
stop = True
