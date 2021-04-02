#!/bin/bash

sudo gpio mode 22 out
sudo gpio write 22 1

print "Hello World";
echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""



