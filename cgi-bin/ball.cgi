#!/bin/bash


print "Hello World";
echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""

sudo python /home/pi/wiringPi/WiringPi2-Python/drv8835-motor-driver-rpi/brake.py
sudo gpio mode 7 out
sudo gpio write 7 1
sudo gpio mode 7 in




