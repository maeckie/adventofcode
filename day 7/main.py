#!/usr/bin/python
import re
import sys
import copy


#with open('/Users/marcus/Documents/advent/adventofcode/day 7/input.txt', 'r') as myfile:
#    programfile=myfile.readlines()

with open('/Users/marcus/Documents/advent/adventofcode/day 7/input.txt', 'r') as myfile:
    programfile=myfile.readlines()

def findParent(stack, programId, pos):
    for program in programfile:
        if '->' in program:
            m = re.search('(\w+).*\((\d+)\)\s+->(.*)', program)
            children = map(str.strip,m.group(3).split(','))
            parent = m.group(1)
            parent_row = stack[pos+1]
            if programId in children:
                if not parent in parent_row:
                    stack[pos+1][parent] = m.group(3)


                sys.exit(1)


def hasChildInPreviousRow(pos, children):

    found = []
    for s in stack:
        for c in children:
            if c in s:
                found.append(True)
    if len(found) == len(children):
        return True
    return False
    #if set(children).issubset(stack[pos]):
    #    return True
    #else:
    #for i in range(0,len(stack)):
    #    for s in stack[i]:
    #        for c in children:
    #            if c == s:
    #                return True
    #return False

def addToCurrentRow(pos, programId, weight, children):
    if len(stack) == pos:
        stack.append({})

#def findOddManOut(pos, children):


    sumChildren = 0
    l = []
    del l[:]
    for s in stack:
        for c in children:
            if c in s:
                l.append(s[c][0])


    if pos-1 > 0:
        if len(set(l)) != 1:
            print "<------>"
            print l
            print "we found the motherload"
            for c in children:
                for s in stack:
                    if c in s:
                        print "<------>"
                        print c
                        print s[c][0]
                        print s[c][1]
                        print

            print "#######"
            sys.exit(1)

    for c in children:
        for s in stack:
            if c in s:
                sumChildren += s[c][0]


    sumChildren = int(weight) + sumChildren
    stack[pos][programId] = (sumChildren,int(weight))





stack = []

# Lets loop alot. okay ?

#find all leaves
leaves = {}
it = 0
cpy = copy.deepcopy(programfile)
for program in cpy:
    if '->' not in program:
        #print program
        m = re.search('(\w+).*\((\d+)\)', program)
        leaves[m.group(1)] =  (int(m.group(2)), 0)
        pos = programfile.index(program)
        del programfile[pos]

    it += 1

stack.append(leaves)



it = 1

while len(programfile) > 0:
    cpy = copy.deepcopy(programfile)
    i = 0
    for program in cpy:
        m = re.search('(\w+).*\((\d+)\)\s+->(.*)', program)
        programId = m.group(1)
        weight = m.group(2)
        children = map(str.strip,m.group(3).split(','))
        if hasChildInPreviousRow(it-1, children):
            addToCurrentRow(it, programId, weight, children)
            pos = programfile.index(program)
            del programfile[pos]
        i += 1

    it += 1

for s in stack:
    if 'qwada' in s:
        print s
#print stack
#while 1:
#    for k in stack[it]:

#        if it+1 == len(stack):
#            stack.append({})
#        findParent(stack, k, it)

#    break
