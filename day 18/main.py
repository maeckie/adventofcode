#!/usr/bin/python
import re
import sys
from collections import deque
registry = {}

with open('/Users/marcus/Documents/advent/adventofcode/day 18/input.txt', 'r') as myfile:
    instructions=myfile.readlines()

def getVal(val):
    cmp = val.strip().lstrip('-')
    if cmp.isdigit():
        return int(val.strip())
    return registry[val.strip()]

def getVal2(registry,val):
    cmp = val.strip().lstrip('-')
    if cmp.isdigit():
        return int(val.strip())
    return registry[val.strip()]

def part1():
    lastPlayedSound = 0
    i = 0
    while i < len(instructions):

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



def runPart2(registry, i, sent, inqueue, outqueue):
        queue = deque([])
        while i < len(instructions):

            m = re.search('(\w+)\s+(\w+)(.*)', instructions[i])
            pos = m.group(2)
            pos = pos.strip()

            if pos not in registry:
                registry[pos] = 0



            if m.group(1) == 'set':
                registry[pos] = getVal2(registry,m.group(3))
            elif m.group(1) == 'add':
                registry[pos] += getVal2(registry,m.group(3))
            elif m.group(1) == 'mul':
                registry[pos] *= getVal2(registry,m.group(3))
            elif m.group(1) == 'mod':
                registry[pos] = registry[pos] % getVal2(registry,m.group(3))
            elif m.group(1) == 'snd':


                outqueue.append(getVal2(registry,pos))
                sent += 1
            elif m.group(1) == 'rcv':

                if len(inqueue) > 0:
                    registry[pos] = inqueue.popleft()
                else:
                    return (i, sent, outqueue)

            elif m.group(1) == 'jgz' and getVal2(registry,pos) > 0:
                i += getVal2(registry, m.group(3))
                i -= 1

            i += 1


def part2():
    i = 0
    j = 0
    regI = {'p':0}
    regJ = {'p':1}
    sentI = 0
    sentJ = 0
    queueI = deque([])
    queueJ = deque([])
    while 1:
        (i, sentI, queueJ) = runPart2(regI, i, sentI, queueI, queueJ)
        (j, sentJ, queueI) = runPart2(regJ, j, sentJ, queueJ, queueI)

        if len(queueI) == 0 and len(queueJ) == 0 and 'rcv' in instructions[i] and 'rcv' in instructions[j]:
            print "we have sent: %d" % sentJ
            break

#print registry
part1()
part2()
