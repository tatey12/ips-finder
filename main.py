import requests
import os
import random
global failures
global passes
import subprocess
import time
#How much to sleep between each request (affects all scripts)
os.environ["WAIT"] = "1"
imgur = subprocess.Popen(["python","imgur.py"])
doc = open("PENISES.txt","a")
os.system('chmod 777 ncat; chmod 777 paping; chmod +s paping;')
def genIP():
    ipGroup = []
    for i in range(4):
        octet = random.randint(1,255)
        if (i == 1) and (octet == 10) or (octet == 127) or (octet == 172) or (octet == 192):
            print("NO!")
        else:
            ipGroup.append(str(random.randint(1,180)))
    return ".".join(ipGroup)
def pingIP(trip,port):
    failures = 0
    passes = 0
    liveIPs = []
    while True:
        time.sleep(int(os.environ["WAIT"]))
        ip = genIP()
        print("I Am Do" + str(ip))
        ping = os.system("./paping " + str(ip))
        
        if ping == 1:
            print("EPIC FAIL! for " + ip )
            failures += 1
        elif ping == 0:
            print("Oh! And the IP is exist!")
            print("Time To Check For De ports boi")
            for i in range(len(port)):
                penis = os.system("./ncat -w 2 " + str(ip) + " " + str(port[i]))
                if penis == 1:
                    print("No Have " + port[i])
                if penis == 0:
                    doc.write(ip + ":" + port[i] + "\n")
                    requests.post("https://canary.discord.com/api/webhooks/815337051293614101/eNTPpsp0YkqlONrRRaYAmTRw4cq03EsOmUHAy7a-DR6vQ6fX_Iu56fQMahT_M2rCXW5k",data={"content":"http://" + str(ip) + port[i]})
                    passes += 1
pingIP(1,["80","443","22","8000","8080","5000"])
