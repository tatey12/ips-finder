import requests
import os
import random
global failures
global passes
doc = open("PENISES.txt","a")
def genIP():
    ipGroup = []
    for i in range(4):
        octet = random.randint(1,255)
        if (i == 1) and (octet == 10) or (octet == 127) or (octet == 172) or (octet == 192):
            print("NO!")
        else:
            ipGroup.append(str(random.randint(1,180)))
    return ".".join(ipGroup)
def pingIP(times,trip,port):
    failures = 0
    passes = 0
    liveIPs = []
    for i in range(times):
        ip = genIP()
        ping = os.system("ncat -w 2 " + str(ip) + " " + str(port))
        if ping == 1:
            print("EPIC FAIL! for " + ip )
            failures += 1
        elif ping == 0:
            print("WIN!!!")
            doc.write(ip + "\n")
            passes += 1
pingIP(100,1,80)
doc.close()
