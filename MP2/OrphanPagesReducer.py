#!/usr/bin/env python
import sys

previous = None
sum = 0
# input comes from STDIN
word_count_d = {}
sortlist = []
for line in sys.stdin:
        key, value = line.split( '\t' )
        if key != previous:
                if previous is not None:
                        #print str( sum ) + '\t' + int(previous
                        word_count_d[previous] = sum
                previous = key
                sum = 0
        sum = sum + int(value)
#print str(sum) + '\t' + previous
word_count_d[previous] = sum
#print(word_count_d)
word_count_d1 = {k : v for k,v in word_count_d.iteritems() if v in [0]}
#print word_count_d1
#keylist = word_count_d.keys()
sortlist = sorted(word_count_d1)
#print sortlist
for line in sortlist:
	print line
