#!/usr/bin/env python
import sys
import string


def tsplit(s, sep):
    stack = [s]
    for char in sep:
        pieces = []
        for substr in stack:
            pieces.extend(substr.split(char))
        stack = pieces
    return stack

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]


stopWordList=[]
with open(stopWordsPath) as f:
    for r in f:
        stopWordList.append(r.strip())
delimiterList=[]
with open(delimitersPath) as f:
    for r in f:
        delimiterList.append(r.strip())
        

inputList = []
for line in sys.stdin:
    inputList.append(line.strip('\n').decode("utf-8-sig").encode('utf8'))

#lowercase words
new_list2 = []
for row in inputList:
    lowercase_row=row.lower()
    new_list2.append(lowercase_row)


#remove delimiters
new_list3 = []
for row in new_list2:
    split_row=tsplit(row, (",","_","(",")","[","]","\t",";",".","?","!","-",":","@","{","}","/","*"))
     #\t,;.?!-:@[](){}_*/
        ##split_row=row.split('_') ##putindelimiter
    new_list3.append(split_row)
#print(new_list3)

##flatten list
new_list4 = []
for x in new_list3:
    for y in x:
        new_list4.append(y)
        

##remove empty spaces in list
while '' in new_list4:
    new_list4.remove('')

new_list5 = []
for row in new_list4:
    if row not in stopWordList:
        new_list5.append(row)
for line in new_list5:
    sys.stdout.write(line + "\t1\n")
