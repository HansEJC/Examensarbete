from __future__ import print_function
import time
import sys
import pigpio
from pololu_drv8835_rpi import motors, MAX_SPEED


try:
    motors.setSpeeds(0, 0)

    print("Motor 2 forward")
    for s in range(290,481):
        motors.motor2.setSpeed(s)
        time.sleep(float(sys.argv[1]))
	
	
	print(s)

finally:
  # Stop the motors, even if there is an exception
  # or the user presses Ctrl+C to kill the process.
  motors.setSpeeds(0, 0)
