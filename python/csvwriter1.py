import csv
import sys
import time
import pigpio
import rotary_encoder
pos = 0
position=0
distance=int(sys.argv[2])
speed=int(sys.argv[1])
def callback(way):
    global pos
    pos += way
pi = pigpio.pi()
decoder = rotary_encoder.decoder(pi, 7, 8, callback)
with open('graf1.csv', 'w') as csvfile:
	fieldnames = ['tid', 'hastighet']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	writer.writeheader()
	for s in range(1,(distance*10)/speed+11):
		position=pos*20.7/158.2
		print("position={}".format(abs(position*s*0.1)))
		writer.writerow({'tid': s*0.1,'hastighet': abs(position/(s*0.1))})
		time.sleep(0.1)
	

		#print(s)


  # Stop the motors, even if there is an exception
  # or the user presses Ctrl+C to kill the process.
		
decoder.cancel()
pi.stop()
