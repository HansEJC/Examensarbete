import csv
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN)
import time
#initialise a previous input variable to 0 (assume button not pressed last)
prev_input = 0

with open('pendel.csv', 'w') as csvfile:
	fieldnames = ['tid', 'position']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	writer.writeheader()
	
	while True:
	  #take a reading
	  input = GPIO.input(25)
	  #if the last reading was low and this one high, print
	  if ((not prev_input) and not input):
		print("Button pressed")
	  	writer.writerow({'tid':0.1,'position': 1})
	  #update previous input
	  prev_input = not input
	  #slight pause to debounce
	  time.sleep(0.05)



	
