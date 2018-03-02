#!/usr/bin/env python
from operator import itemgetter
import sys

#TODO

previous = None
sum = 0
min = 99999999999
max = 0
variance = 0
avg = 0
# input comes from STDIN
words_count = []
for line in sys.stdin:
	key, value = line.split( '\t' )
	sum = sum + int(value)
	if (int(value) < min):
		min = int(value)
	if (int(value) > max):
		max = int(value) 
	words_count.append(int(value))	
#print str(sum)
#print str(min)
#print str(max)
#print words_count
avg = sum/len(words_count)
#print avg
for count in words_count:
	variance = variance + ((count - avg)**2)
variance = variance/len(words_count)
sys.stdout.write("Mean" + "\t" + str(avg) + "\n")
sys.stdout.write("Sum" + "\t" + str(sum) + "\n")
sys.stdout.write("Min" + "\t" + str(min) + "\n")
sys.stdout.write("Max" + "\t" + str(max) + "\n")
sys.stdout.write("Var" + "\t" + str(variance) + "\n")
