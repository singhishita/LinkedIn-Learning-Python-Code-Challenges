#This solution has been given by Barron Stone, the instructor himself

import time
import sched
import winsound #to play wav sound files in Windows

def set_alarm(time, sound, message):
	s = sched.scheduler(time.time, time.sleep)
	s.enterlabs(time, 1, print, argument = (message,))
	s.enterlabs(time, 1, winsound.PlaySound, argument=(sound, winsound.SND_FILENAME))
	print('Alarm set for', time.asctime(time.localtime(time)))
	s.run()

#console

set_alarm(time.time()+1, 'alarm.wav', 'Wake up!')
