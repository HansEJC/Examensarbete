
import time
import sys
from pololu_drv8835_rpi import motors, MAX_SPEED

speed=float(sys.argv[1])
direction=float(sys.argv[2])
pwm=speed*10.996-470.562
pwmb=speed*5.0985+258.047



if direction == 1:
	motors.setSpeeds(0, 0)
	motors.motor2.setSpeed(int(pwm))
	time.sleep(10)
else:
	motors.setSpeeds(0, 0)
	motors.motor2.setSpeed(int(pwmb))
	time.sleep(10)
	
motors.setSpeeds(0, 0)

