#!/usr/bin/env python
import sys



# input comes from STDIN
for line in sys.stdin:
	a,b =  line.split('\n')
	sys.stdout.write(str(a) + "\n")
