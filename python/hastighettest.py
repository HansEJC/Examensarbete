from __future__ import print_function
import time
from pololu_drv8835_rpi import motors, MAX_SPEED

# Set up sequences of motor speeds.
test_forward_speeds = list(range(400, MAX_SPEED, 1))  

test_reverse_speeds = list(range(0, -MAX_SPEED, -1)) + \
  [-MAX_SPEED] * 1000 + list(range(-MAX_SPEED, 0, 1)) + [0]  

i=2

try:
    motors.setSpeeds(0, 0)

    print("Motor 2 forward")
    for s in range(481,280,-1):
        motors.motor2.setSpeed(s)
        time.sleep(0.1)
	
	
	print(s)

	#print("Motor 2 forward")
    for s in range(-430,0,1):
        motors.motor2.setSpeed(s)
        time.sleep(0.1)
	print(s)
   

finally:
  # Stop the motors, even if there is an exception
  # or the user presses Ctrl+C to kill the process.
  motors.setSpeeds(0, 0)
