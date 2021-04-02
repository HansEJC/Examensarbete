#!/bin/bash

sudo gpio mode 23 in
sudo gpio mode 22 in

print "Hello World";
echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""



