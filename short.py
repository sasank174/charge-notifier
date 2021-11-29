import psutil as E
from time import sleep as D
from win10toast import ToastNotifier as J
import pyttsx3 as K
global A,B
def F():global A,B;A=B=0
def G():A=E.sensors_battery();B,C=A.power_plugged,A.percent;return B,C
C=K.init()
C.setProperty('rate',125)
C.setProperty('volume',1.0)
def H(n):
	global A,B;E,F=('Greater than 90%','Charging is Greater than 90% unplug your charger BOSS'),('Less than 20%','Charging is Less than 20% plugin ASAP BOSS');D=E if n==1 else F
	if n==1:D=E;A,B=A+1,0
	elif n==0:D=F;A,B=0,B+1
	G=J();G.show_toast('CHARGING',D[0],duration=10,icon_path='notification.ico');C.say(D[1]);C.runAndWait()
def I():
	global A,B
	try:
		C,E=G();H(1)if C and E>90 else H(0)if not C and E<20 else print('')
		if A>=3 or B>=3:
			J=C
			while True:
				C,E=G()
				if J!=C:F();break
				D(60)
		D(60);I()
	except:quit()
if __name__=='__main__':D(60);F();D(10);I()