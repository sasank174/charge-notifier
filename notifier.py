import psutil
from time import sleep
from win10toast import ToastNotifier
import pyttsx3

global i,j

def reset():
	global i,j
	i=j=0

def chargeinfo():
	battery=psutil.sensors_battery()
	plugged,percentage = battery.power_plugged,battery.percent
	return (plugged,percentage)

engine = pyttsx3.init()
engine.setProperty('rate', 125)
engine.setProperty('volume',1.0)

def notification(n):
	global i,j
	a,b = ("Greater than 90%","charging is too high bro"),("Less than 20%","charging is low bro")
	notify = a if n == 1 else b

	if n == 1:
		notify = a
		i,j=i+1,0
	elif n==0:
		notify = b
		i,j=0,j+1

	toaster = ToastNotifier()
	toaster.show_toast("CHARGING",notify[0],duration=10,icon_path="notification.ico")
	
	engine.say(notify[1])
	engine.runAndWait()

def notifier():
	global i,j
	try:
		plugged,percentage = chargeinfo()

		notification(1) if plugged and percentage>90 else notification(0) if not plugged and percentage<20 else print("")
		
		if i>=3 or j>=3:
			status = plugged
			while(True):
				plugged,percentage = chargeinfo()
				if status != plugged:
					reset()
					break
				sleep(60)

		sleep(60)
		notifier()
	except:
		quit()

if __name__ == "__main__":
	sleep(60)
	reset()
	sleep(10)
	notifier()