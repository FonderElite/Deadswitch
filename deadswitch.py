import colorama
from colorama import Fore
import signal
import time
import sys
import platform
from bs4 import BeautifulSoup as soup
wi = Fore.WHITE
rd = Fore.RED
cy = Fore.CYAN
os = platform.system()
TIMEOUT3 = int(multi) * 86400 #days
TIMEOUT1 = int(multi) * 60 #mins
TIMEOUT4 = int(multi) * 2678400 #months
TIMEOUT5 = int(multi) * 32140800 # years
TIMEOUT2 = int(multi) * 3600 # hours
# secs to wait for interaction
banner = print(Fore.CYAN + '''

''')
time.sleep(2)
help = print(yl + '''
=============================================
+|  Phone-Info  By  F o n d e r E l i t e  |+
+|-----------------------------------------|+
+|      -h          Help                   |+
+|      -d          delete                 |+
+|      -s          Start                  |+
+|      -u          Update                 |+
+|      -q          Quit                   |+
+| options: mins,hours,days,months,years   |+
+|Ex. ./deadswitch -d -s mins              |+
+|=========================================|+
''')
def interrupted(signum, frame):
    "called when read times out"
    print('Timer Done')
    time.sleep(1)
    print('Exiting')
    sys.exit()
signal.signal(signal.SIGALRM, interrupted)

def i_input():
    try:
            print("You have: " +  multi + " Minute(s) left for the alarm to execute")
            foo = input()
            return foo
    except:
            # timeout
            return
            print("Timer Done!")
            sys.exit()

def i2_input():
    try:
        print("You have: " + multi + " Hour(s) left for the alarm to execute")
        foo = input()
        return foo
    except:
        # timeout
        return
        print("Timer Done!")
        sys.exit()
def i3_input():
    try:
        print("You have: " + multi + " Day(s) left for the alarm to execute")
        foo = input()
        return foo
    except:
        # timeout
        return
        print("Timer Done!")
        sys.exit()
# set alarm
signal.alarm(TIMEOUT)
while True:
  command = input(os + "User: ")
  if command == "./deadswitch -h":
      print(help)
  elif command == "./deadswitch":
      print(help)
  elif command == "./deadswitch -u":


# disable the alarm if not wanted any longer
# signal.alarm(0)

