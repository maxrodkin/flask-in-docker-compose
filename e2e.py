#!/usr/bin/python

import urllib
import sys
try:
    responce_code = urllib.urlopen(sys.argv[1])
    if responce_code.getcode() == 200:
        print ("Test Ok")
    else:
        print ("Test Failed")
except Exception as e:
    print ("Test Failed. App not running.")
