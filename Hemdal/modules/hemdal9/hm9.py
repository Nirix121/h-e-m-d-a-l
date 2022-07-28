import os
import time
print ('''
#-----------------#
1 - programing
2 - porn
3 - hack
4 - drugs
#-----------------#
 ''')
dar = int(input(":"))
#-
if dar == 1 :
	cmd = os.system("python3 -m pip install -r requirements.txt && python3 hmo9.py --query programming")

elif dar == 2 :
	cmd = os.system("python3 -m pip install -r requirements.txt && python3 hmo9.py --query porn")

elif dar == 3 :
	cmd = os.system("python3 -m	pip install -r requirements.txt && python3 hmo9.py --query hack")

elif dar == 4 :
	cmd = os.system("python3 -m pip install -r requirements.txt && python3 hmo9.py --query drugs")