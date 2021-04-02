from __future__ import print_function
import time
import sys
import pigpio
import rotary_encoder
from PIDcontroller import PID
from pololu_drv8835_rpi import motors, MAX_SPEED

pos = 0
position=pos*20.7/158.2
speed=float(sys.argv[1])
pwm=speed*10.996-470.562
pwmb=speed*5.0985+258.047
distance=float(sys.argv[2])

p=PID(3,0,0)
p.setPoint(speed)



def callback(way):
    global pos
    pos += way
    print("pos={}".format(abs(pos*20.7/158.2)))
pi = pigpio.pi()
decoder = rotary_encoder.decoder(pi, 7, 8, callback)

#for s in range(1,(int(distance)*20)/int(speed)+21):#inte klar
try:
    motors.setSpeeds(0, 0)

    print("Motor 2 forward")
    for s in range(1,int(distance*10/speed)+1):
        pid=p.update((pos*20.7/158.2)/s*10)
        motors.motor2.setSpeed(int(pwm)) 
        time.sleep(0.1)
	
        print("speed={}".format(pid))
    
    #motors.motor2.setSpeed(int(pwm))
    #time.sleep(distance/speed)

    motors.motor2.setSpeed(0)
    time.sleep(2)

    #motors.motor2.setSpeed(int(pwmb))
    #time.sleep(distance/speed)
    for s in range(int(distance*10/speed)):
        motors.motor2.setSpeed(int(pwmb))
        time.sleep(0.1)

finally:
  # Stop the motors, even if there is an exception
  # or the user presses Ctrl+C to kill the process.
  motors.setSpeeds(0, 0)


print("position={}".format(pid))
print("position={}".format(pos*20.7/158.2))
decoder.cancel()
pi.stop()
