import psutil
import time
from win10toast import ToastNotifier
import pyttsx3

i = 0
j = 0
reset = True

engine = pyttsx3.init()
engine.setProperty('rate', 125)
engine.setProperty('volume',1.0)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def notification(heading,paragraph):
	toaster = ToastNotifier()
	toaster.show_toast(heading,paragraph,duration=3,icon_path="geeks.ico")

def resetadd():
	battery=psutil.sensors_battery()
	plugged = battery.power_plugged
	global reset
	reset = plugged

def resetvarables(status):
	global i
	global j
	global reset
	if status != reset:
		i=0
		j=0
		reset = status

def change(status):
	global i
	global j
	battery=psutil.sensors_battery()
	plugged = battery.power_plugged
	if status == plugged:
		time.sleep(60)
		change(status)
	else:
		i=0
		j=0


def cpu():
	global i
	global j
	try:
		battery=psutil.sensors_battery()
		plugged = battery.power_plugged
		percentage = battery.percent

		resetvarables(plugged)
		
		if plugged and percentage>90:
			notification("Charging","Greater than 90%")
			speak("Charging is Greater than 90% unplug your charger BOSS")
			i=i+1

		if plugged == False and percentage<20:
			notification("Charging","Less than 20%")
			speak("Charging is Less than 20% plugin ASAP BOSS")
			j=j+1

		if i>=3 or j>=3:
			change(plugged)
			
		time.sleep(60)
		cpu()
	except:
		quit()


if __name__ == "__main__":
	time.sleep(60)
	resetadd()
	time.sleep(10)
	cpu()