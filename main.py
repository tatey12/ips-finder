import requests
import os
import random
global failures
global passes
import subprocess
import time
from selenium import webdriver
import sys
#How much to sleep between each request (affects all scripts)
os.environ["WAIT"] = "2"
imgur = subprocess.Popen(["python","imgur.py"])
os.system('chmod 777 ncat')
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
    time.sleep(int(os.environ["WAIT"]))
    ip = genIP()
    print("I Am Do" + str(ip) + " on port " + str(port))
    ping = os.system("./ncat -w 2 " + str(ip) + " " + str(port))
    if ping == 1:
        print("EPIC FAIL! for " + ip )
        failures += 1
    elif ping == 0:
        print("WIN!!!")
        requests.post("https://canary.discord.com/api/webhooks/815337051293614101/eNTPpsp0YkqlONrRRaYAmTRw4cq03EsOmUHAy7a-DR6vQ6fX_Iu56fQMahT_M2rCXW5k",data={"content":"http://" + str(ip) + ":" + str(port)})
        requests.post("https://canary.discord.com/api/webhooks/778773447274528768/dHQaxbNAfuzuNZbeA263FhW4jjdQPBebo11VSW5n7LGHPCWKfDkn3uXdreiBfeHYNrRd",data={"content":"http://" + str(ip) + ":" + str(port)})
        passes += 1
        #try:
        #    driver = webdriver.Chrome()
        #    driver.get('http://' + str(ip))
        #    driver.get_screenshot_as_file("screenshot.png")
        #    files = {'file': open('screenshot.png', 'rb')}
        #    requests.post("https://canary.discord.com/api/webhooks/815337051293614101/eNTPpsp0YkqlONrRRaYAmTRw4cq03EsOmUHAy7a-DR6vQ6fX_Iu56fQMahT_M2rCXW5k",files=files)
        #    driver.quit()
        #except:
        #    requests.post("https://canary.discord.com/api/webhooks/815337051293614101/eNTPpsp0YkqlONrRRaYAmTRw4cq03EsOmUHAy7a-DR6vQ6fX_Iu56fQMahT_M2rCXW5k",data={"content":"Donkey Kong Banana's Error: \n ```" + sys.exc_info()[0] + "```"})
while True:
    pingIP(1,80)
