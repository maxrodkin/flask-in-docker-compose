#!/usr/bin/python

import urllib
import sys

responce_code = urllib.urlopen(sys.argv[1])
if responce_code.getcode() == 200:
    print ("Test Ok")
else:
    print ("Test Failed")
