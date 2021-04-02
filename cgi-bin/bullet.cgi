#!/bin/bash

sudo gpio mode 7 out
sudo gpio write 7 1
sudo gpio mode 7 in

print "Hello World";
echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""



