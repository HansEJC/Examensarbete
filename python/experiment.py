import subprocess
import time
import sys

delay=float(sys.argv[1])
time.sleep(delay)
subprocess.call("/usr/lib/cgi-bin/bullet.cgi")
  

	
