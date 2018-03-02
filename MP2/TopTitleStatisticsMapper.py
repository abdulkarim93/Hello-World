#!/usr/bin/env python

import sys
import string

for line in sys.stdin:
	key,value  = line.split("\t")
	sys.stdout.write( "Value" + "\t" + value)
