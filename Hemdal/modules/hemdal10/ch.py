import os
cmd = os.system("chmod +x hemdal.sh")
print ('''1) run as administrator
2) run as user''')
var = int(input(":"))
if var == 1 :
	cmd = os.system("sudo bash ./hemdal.sh")
elif var == 2 :
	cmd = os.system("bash ./hemdal.sh")