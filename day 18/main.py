#!/usr/bin/python
import re
import sys
registry = {}
with open('/Users/marcus/Documents/advent/adventofcode/day 18/input.txt', 'r') as myfile:
    instructions=myfile.readlines()

def getVal(val):
    cmp = val.strip().lstrip('-')
    if cmp.isdigit():
        return int(val.strip())
    return registry[val.strip()]


lastPlayedSound = 0
i = 0
while i < len(instructions):
    print instructions[i]

    m = re.search('(\w+)\s+(\w+)(.*)', instructions[i])
    pos = m.group(2)
    pos = pos.strip()
    if pos not in registry:
        registry[pos] = 0



    if m.group(1) == 'set':
        registry[pos] = getVal(m.group(3))
    elif m.group(1) == 'add':
        registry[pos] += getVal(m.group(3))
    elif m.group(1) == 'mul':
        registry[pos] *= getVal(m.group(3))
    elif m.group(1) == 'mod':
        registry[pos] = registry[pos] % getVal(m.group(3))
    elif m.group(1) == 'snd':
        lastPlayedSound = registry[pos]
    elif m.group(1) == 'rcv' and registry[pos] > 0:
        print "Last played freq is: %d" % lastPlayedSound
        break
    elif m.group(1) == 'jgz' and registry[pos] > 0:
        i += int(m.group(3))
        i -= 1

    i += 1



#print registry
