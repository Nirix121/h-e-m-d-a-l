 # CODE NIRIX

import os
import time
import getpass

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

os.system("clear")
time.sleep(2)

print (W + '''
 ____________________________________________
|(1) free Shodan          |(7) Fake traffic
|                         |
|(2) Sms bomber           |(8) Link masking
|                         |
|(3) Wifi hack (sudo)     |(9) Darknet search
|                         | 
|(4) Scaner (detail 4_1)  |(10)find password 
|                         |    from the root
|(5) phishing (detail 5.1)|(11)
|                         |
|(6) DDOS ip (test)       |(12) 
|_________________________|__________________

''')

var = int(input("Enter your choise here:"))

#--------------------
if var == 1 :
    cmd = os.system(" cd hemdal1 && python3 hm1.py ")
#--------------------
elif var == 2 :
    cmd = os.system(" cd hemdal2 && python3 hm2.py ")
#--------------------
elif var == 3 :
    cmd = os.system(" cd hemdal3 && python3 hm3.py ")
#--------------------
elif var == 4 :
    cmd = os.system(" cd hemdal4 && python3 hm4.py ")
#--------------------
elif var == 4_1 :
    print ('''Scanner 0.1 :
[1]Scaner phone    [5]Torrent
[2]avito           [6]Parse Proxy
[3]car-uk 
[4]BSSID-Locate 
    ''')
    time.sleep(10)
    os.system("clear")
    cmd = os.system(" python3 hm.py ")
#--------------------
elif var == 5 :
    cmd = os.system(" cd hemdal5 && bash hm5.sh ")
#--------------------
elif var == 5.1 :
    print (''' phishing 
[01] Facebook      [11] Twitch       [21] DeviantArt
[02] Instagram     [12] Pinterest    [22] Badoo
[03] Google        [13] Snapchat     [23] Origin
[04] Microsoft     [14] Linkedin     [24] DropBox
[05] Netflix       [15] Ebay         [25] Yahoo
[06] Paypal        [16] Quora        [26] Wordpress
[07] Steam         [17] Protonmail   [27] Yandex
[08] Twitter       [18] Spotify      [28] StackoverFlow
[09] Playstation   [19] Reddit       [29] Vk
[10] Tiktok        [20] Adobe        [30] XBOX
[31] Mediafire     [32] Gitlab       [33] Github
    ''')
    time.sleep(3)
    cmd = os.system("python3 hm.py")
#-------------------
elif var == 6 :
    cmd = os.system(" cd hemdal6 && python3 hm6.py ")
#-------------------  
elif var == 7 :
    cmd = os.system(" cd hemdal7 && python3 hm7.py ")
#-------------------
elif var == 8 :
    cmd = os.system("cd hemdal8 && python3 hm8.py ")
#-------------------
elif var == 9 :
    cmd = os.system(" cd hemdal9 && python3 hm9.py ")
#-------------------
elif var == 10 :
    cmd = os.system(" cd hemdal10 && python3 ch.py ")



