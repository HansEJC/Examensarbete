import csv
import sys
import time
import pigpio
import rotary_encoder
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN)
pos = 0
position=0
displacement=0
hastighet=0
mellanpos=0
x=0
distance=int(sys.argv[2])
speed=int(sys.argv[1])
def callback(way):
    global pos
    pos += way
pi = pigpio.pi()
decoder = rotary_encoder.decoder(pi, 7, 8, callback)
with open('graf.csv', 'w') as csvfile:
	fieldnames = ['tid', 'distance', 'hastighet', 'hastighet2', 'pendel']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	writer.writeheader()
	for s in range(1,(distance*20)/speed+21):
		position=pos*20.7/158.2
		hastighet=position/(s*0.1)
		if displacement==0: #nar vagnen star still
			hastighet=0
			mellanpos=position
		if displacement<0: #nar vagnen kor tillbaka
			x=x+1
			hastighet=(position-mellanpos)/(x*0.1)
		print("position={}".format(abs(position)))
		pend = GPIO.input(25) #read pendel status
		writer.writerow({'tid': s*0.1,'distance': abs(position), 'hastighet': hastighet, 'hastighet2': displacement/0.1, 'pendel':(not pend)*speed})
		if (not pend):
			#print("Button pressed")
			writer.writerow({'tid':s*0.1, 'distance': abs(position), 'hastighet': hastighet, 'hastighet2': displacement/0.1, 'pendel': speed})
		
	 	time.sleep(0.1)
		displacement=pos*20.7/158.2-position
		
		#print(s)


  # Stop the motors, even if there is an exception
  # or the user presses Ctrl+C to kill the process.
		
decoder.cancel()
pi.stop()
