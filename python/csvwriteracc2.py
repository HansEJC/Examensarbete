import csv
import sys
import time
import pigpio
import rotary_encoder
import math
pos = 0
position=0
distance=int(sys.argv[2])
acceleration=float(sys.argv[1])*1000

#t=sqrt(2ad)/a
tid=math.sqrt(2*acceleration*distance)/acceleration

def callback(way):
    global pos
    pos += way
pi = pigpio.pi()
decoder = rotary_encoder.decoder(pi, 7, 8, callback)
with open('graf22.csv', 'w') as csvfile:
	fieldnames = ['tid', 'acceleration']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	writer.writeheader()
	for s in range(1,int(tid*20)+20):
		position=pos*20.7/158.2
		#print("position={}".format(abs(position)))
		writer.writerow({'tid': s*0.1,'acceleration': abs(position/(1000*s*s*0.1))})
		time.sleep(0.1)
	
	
		#print(s)


  # Stop the motors, even if there is an exception
  # or the user presses Ctrl+C to kill the process.
		
decoder.cancel()
pi.stop()
