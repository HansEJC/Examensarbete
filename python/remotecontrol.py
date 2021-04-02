import subprocess
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)
GPIO.setup(20,GPIO.IN)
GPIO.setup(16,GPIO.IN)
import time
#initialise a previous input variable to 0 (assume button not pressed last)
prev_input = 0

while True:
  #take a reading
  forward = GPIO.input(16)
  rev = GPIO.input(20)
  exp = GPIO.input(21)
  #if the last reading was low and this one high, print
  if (forward==0):
	GPIO.setup(6,GPIO.OUT)
	GPIO.output(6,1)
	prev_input=1
  if(prev_input and forward and rev==1):
	GPIO.setup(6,GPIO.IN)
	GPIO.setup(13,GPIO.IN)
	prev_input=0
  if(exp==0):
    subprocess.call("/usr/lib/cgi-bin/bullet.cgi")
  if (rev==0):
	GPIO.setup(13,GPIO.OUT)
	GPIO.output(13,1)
	prev_input=1
  time.sleep(0.05)

	
