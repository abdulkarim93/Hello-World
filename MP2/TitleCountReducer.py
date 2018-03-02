#!/usr/bin/env python
from operator import itemgetter
import sys

#TODO

previous = None
sum = 0
# input comes from STDIN
word_count_d = {}
for line in sys.stdin:
	key, value = line.split( '\t' )
	if key != previous:
		if previous is not None:
			#print str( sum ) + '\t' + previous
			word_count_d[previous] = sum
		previous = key
		sum = 0
	sum = sum + int(value)
#print str(sum) + '\t' + previous
word_count_d[previous] = sum
#print(word_count_d)
list = sorted(word_count_d, key=lambda key: (-word_count_d[key], key))
#print(list)
#sortlist = sorted(list[0:5])
for line in list[0:10]:
#	print "%s\t%s" % (line,word_count_d[line])
	sys.stdout.write(str(line) + '\t' + str(word_count_d[line]) + '\n')
