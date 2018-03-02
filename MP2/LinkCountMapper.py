#!/usr/bin/env python
import sys

def mysplit(s, sep):
    stack = [s]
    for char in sep:
        pieces = []
        for substr in stack:
            pieces.extend(substr.split(char))
        stack = pieces
    return stack
sublist = []
for line in sys.stdin:
	sublist.append(line.strip('\n'))
delimiters = [" "]
#print delimiters
#print stopWordsList
#print sublist
z = len(sublist)
sublist2 = []
i = 0
while i < z:
	temp = sublist[i]
#    print (temp)
	temp2 = mysplit(temp,delimiters)
	sublist2.append(temp2)
#    print(temp2)
	i += 1
#print sublist2

sublist3 = []
for line in sublist2:
    for y in line:
        sublist3.append(y)

while '' in sublist3:
    sublist3.remove('')

for line in sublist3:
	if ":" in line:
		print '%s\t%s' % (line.rstrip(':'),0)
	else:
		print '%s\t%s' % (line,1)
