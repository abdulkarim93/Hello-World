#!/usr/bin/env python
import sys



word_count_d = {}
list = []
for line in sys.stdin:
	key, value = line.split( '\t' )
	word_count_d[key] = int(value)
	list.append(key)


sortlist = sorted(list[0:5])
for line in sortlist[0:5]:
        sys.stdout.write(str(line) + "\t" + str(word_count_d[line]) + "\n")
