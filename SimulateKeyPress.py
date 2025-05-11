import ctypes
import time
import datetime
from random import randint
user32 = ctypes.windll.user32

def Alt_F10(count,delta_time):
	print "-------------[capture:%06d][%04dseconds]--------------------"%(count,delta_time)
	print "AltDown:",user32.keybd_event(18,0,2,0)  #2 is the code for KEYDOWN
	time.sleep(1)
	print "F10Up:",user32.keybd_event(18,0,0,0)
	time.sleep(1)
	print "F10Up:",user32.keybd_event(121,0,0,0)  #0 is the code for KEYUP
	time.sleep(1)
	print "AltUp:",user32.keybd_event(18,0,0,0)
	print "------------------------------------------------"

time.sleep(10)
random_timediff = 30
minTime = 10
maxTime = 60*100
time_begin = datetime.datetime.now()
index = 0
print "ServerStart@",time_begin
print "[%06d] First capture in %d seconds ..."%(index,random_timediff)
while(1)
	time_now = datetime.datetime.now()
	time_diff = time_now - time_begin 
	if(time_diff.seconds > random_timediff):
		Alt_F10(index,random_timediff)
		time_begin = datetime.datetime.now()
		random_timediff = randint(minTime,maxTime) #Inclusive
		index += 1
		print "[%06d] Next capture in %d seconds ..."%(index,random_timediff)
	time.sleep(1)

#breakManually

#VOID keybd_event(BYTE bVk, BYTE bScan, DWORD dwFlags, PTR dwExtraInfo);
#user32.keybd_event(keycode,0,0,0) #is the code for KEYDUP[/code]
