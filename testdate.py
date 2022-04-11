from datetime import datetime,timedelta
from threading import Timer
import time



start_time = time.time()
now = datetime.now()
date_time = now.strftime("%m/%d/%Y,%H:%M:%S") 
currenttime =  '04/11/2022,13:20:34'
if (currenttime < date_time):
 print('System Expired | ', date_time, currenttime)
else : 
 print('System Left | ', date_time, currenttime)

run = True
def timechecks():
	global run
	timechecks()
	if run:
		Timer(0, timechecks).start()