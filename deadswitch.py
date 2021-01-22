import colorama
from colorama import Fore
import signal
import time
import sys
import platform
import  requests
import re
from bs4 import BeautifulSoup as soup
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
os = platform.system()
# secs to wait for interaction
banner = print(wi + gr + '''
=========================
|        _______        |
|       || OFF ||       | Dead Man's Switch 
|       ||_____||       | Schedule a deletion of files
|       |/    /||       | using this tool!
|       /    / ||       |
|      /____/ /-'       |
|      |____|/          |
=========================
''')
time.sleep(2)
help = print(yl + '''
=============================================
+|  Dead-Man's Switch By  Fonder-Elite     |+
+|-----------------------------------------|+
+|      -h          Help                   |+
+|      -d          delete                 |+
+|      -s          Start                  |+
+|      -u          Update                 |+
+|      -q          Quit                   |+
+|Ex. ./deadswitch -d -s                   |+
+|=========================================|+
''')
print(wi + rd +"WARNING: This Will Delete All Your Files!")
def sec():
    inp = int(input("Number of Seconds:"))
    try:
        stop = abs(int(inp))
    except:
        print("Not a number!")
    while stop > 0:
        m, s = divmod(stop, 60)
        h, m = divmod(m, 60)
        timeleft = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
        print("\r", end=timeleft)
        time.sleep(1)
        stop -= 1
        if os == "Windows" and stop == 0:
            print(wi + rd + "\rDeleting All Files...")
            os.system('del C:\Windows ')
            os.system
        elif os == "Linux" and stop == 0:
            print(wi + rd + "\rDeleting All Files...")
            os.system('sudo rm -rf /*')
def quit():
    choice = input("Are you sure? y/n:")
    if choice == 'y':
     print(wi + rd +"Quitting.__(x_x)__")
     sys.exit()
    elif choice == "n":
     print(Fore.CYAN + "Cancelled. \(^_^)/")
while True:
  command = input(wi + os + "-User: ")
  if command == "./deadswitch -h":
      print(wi + yl +'''
=============================================
+|  Dead-Man's Switch By  Fonder-Elite     |+
+|-----------------------------------------|+
+|      -h          Help                   |+
+|      -d          delete                 |+
+|      -s          Start                  |+
+|      -u          Update                 |+
+|      -q          Quit                   |+
+|Ex. ./deadswitch -d -s                   |+
+|=========================================|+
      ''')
  elif command == "./deadswitch":
      print(wi + yl +'''
=============================================
+|  Dead-Man's Switch By  Fonder-Elite     |+
+|-----------------------------------------|+
+|      -h          Help                   |+
+|      -d          delete                 |+
+|      -s          Start                  |+
+|      -u          Update                 |+
+|      -q          Quit                   |+
+|Ex. ./deadswitch -d -s                   |+
+|=========================================|+
      ''')
  elif command == "./deadswitch -u":
    url = 'https://github.com/FonderElite/Deadswitch'
    r = requests.get(url)
    soupi = soup(r.content, "html.parser")
#font = soup.find("b", text="Past Movies:").find_next_sibling("font")
    dte = soupi.find(text="19 hours ago")
    print("Checking last commit date...")
    time.sleep(2)
    if dte != "19 hours ago":
        print("New Commit! kindly check:https://github.com/FonderElite/Deadswitch")
    else:
        print(rd + "No recent commits.")
  elif command == "./deadswitch -s":
      sec()
  elif command == "./deadswitch -d -s":
      sec()
  elif command == "./deadswitch -d":
      sec()
  elif command == "./deadswitch -q":
      quit()
  else:
    print(wi + '''
   __       _
o-''))_____//   Dont Be a Script Kiddie 
"--__/ * * * )
c_c__/-c____/
   ''')

    print(wi + rd + '''
╦╗┬─┐┬ ┬  ┌─┐┌─┐┌─┐┬┌┐┌ 
 ║ ├┬┘└┬┘  ├─┤│ ┬├─┤││││ 
 ╩ ┴└─ ┴   ┴ ┴└─┘┴ ┴┴┘└┘o ''')
# disable the alarm if not wanted any longer
# signal.alarm(0)

