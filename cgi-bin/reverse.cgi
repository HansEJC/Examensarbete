#!/bin/bash

sudo gpio mode 23 out
sudo gpio write 23 1

print "Hello World";
echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""



