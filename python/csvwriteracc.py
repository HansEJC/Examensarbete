import csv
import sys
import time
import pigpio
import rotary_encoder
import math
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN)

pos = 0
position=0
displacement=0
distance=int(sys.argv[2])
acceleration=float(sys.argv[1])*100
prevhast=0
x=5
acc=0
mellanpos=0
hastighet=0
#t=sqrt(2ad)/a
tid=math.sqrt(2*acceleration*distance)/acceleration

def callback(way):
    global pos
    pos += way
pi = pigpio.pi()
decoder = rotary_encoder.decoder(pi, 7, 8, callback)
with open('graf2.csv', 'w') as csvfile:
	fieldnames = ['tid', 'distance', 'hastighet', 'hastighet2','acceleration','acc','pendel']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	writer.writeheader()
	for s in range(1,int(tid*20)+20):
		position=pos*20.7/158.2
		hastighet=abs(position*2/(10*s))
		acc=abs(position/(0.4*s*s))
		if displacement==0: #nar vagnen star still
			#x=x+1
			hastighet=0
			acc=0
			mellanpos=position
		if displacement<0: #nar vagnen kor tillbaka
			x=x+1
			hastighet=(position-mellanpos)/(x*5)
			acc=(position-mellanpos)/(0.4*x*x)
		#print("position={}".format(abs(position)))
		pend = GPIO.input(25) #read pendel status
		writer.writerow({'tid': s*0.1,'distance': abs(position/100),'hastighet': hastighet, 'hastighet2': displacement/10,'acceleration': acc, 'acc': (abs(position*2/(10*s))-prevhast)/0.1, 'pendel':(not pend)*acceleration/100})
		if (not pend):
			#print("Button pressed")
			writer.writerow({'tid':s*0.1,'distance': abs(position/100),'hastighet': hastighet, 'hastighet2': displacement/10,'acceleration': acc, 'acc': (abs(position*2/(10*s))-prevhast)/0.1, 'pendel': acceleration/100})
		
		time.sleep(0.1)
		displacement=pos*20.7/158.2-position
		prevhast=abs(position*2/(10*s))
		#print(s)


  # Stop the motors, even if there is an exception
  # or the user presses Ctrl+C to kill the process.
		
decoder.cancel()
pi.stop()
