import time
import pigpio
import rotary_encoder
pos = 0
rev=0
def callback(way):
    global pos
    pos += way
    print("pos={}".format(pos))
pi = pigpio.pi()
decoder = rotary_encoder.decoder(pi, 7, 8, callback)
time.sleep(5)
rev=pos/158.2
print("rev={}".format(rev))
decoder.cancel()
pi.stop()
