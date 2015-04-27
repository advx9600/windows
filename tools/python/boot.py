import os
import time
import sys
import datetime
import subprocess

weekday = int(datetime.datetime.today().weekday())
if (weekday >-1 and weekday < 6):
    os.system("shutdown -f -s -t 1200")
else:
    os.system("shutdown -f -s -t 60")
    
    

    
# must add last,because hide the window
subprocess.call([sys.executable,"C:/Users/Administrator/Desktop/flash.py","flashImg"])