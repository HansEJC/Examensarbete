from __future__ import print_function
import time
import sys
import pigpio
import rotary_encoder
import math
from pololu_drv8835_rpi import motors, MAX_SPEED

pos = 0
rev=0
acceleration=float(sys.argv[1])*100
distance=float(sys.argv[2])
tid=math.sqrt(2*acceleration*distance)/acceleration
pwm=0
pwmb=0	
speed=0
speed2=0

try:
    motors.setSpeeds(0, 0)

    print("Motor 2 forward")
    for s in range(int(tid*10)):
        motors.motor2.setSpeed(int(pwm))
        time.sleep(0.1)

	if speed < 42:
		speed=speed+acceleration*0.1
	else:
		speed=42
	pwm=speed*10.996-470.562
	print(speed)

    for i in range(int(tid*10)):
        motors.motor2.setSpeed(int(pwmb))
        time.sleep(0.1)

	if speed2 < 42:
		speed2=speed2+acceleration*0.1
	else:
		speed2=42
	pwmb=speed2*5.0985+258.047
	print(speed2)
	

finally:
  # Stop the motors, even if there is an exception
  # or the user presses Ctrl+C to kill the process.
  motors.setSpeeds(0, 0)
print(tid)
print(tid*tid*acceleration/2)
