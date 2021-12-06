import pyfiglet 
import sys 
import socket 
from datetime import datetime 

#Outputs banner

ascii_banner =pyfiglet.figlet_format("KICK ASS PORT SCANNER")
print(ascii_banner)

if len(sys.argv) == 2: 

    target = socket.gethostbyname(sys.argv[1])
else:
    print("Don't forget to enter the IP")

#Outputs wording on screen 

print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))

#Does the actual scanning action

try: 

    for port in rang(1,1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target,port))
        if result ==0:
            prtint("Port {} is open".format(port))
        s.close()

#socket.AF_INET=IPV4 
#socket.SOCK_STREAM=TCP protocals 

except KeyboardInterrupt: 
    print("\n Exitting Program !!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()
