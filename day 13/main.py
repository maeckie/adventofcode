#!/usr/bin/python
import re
from collections import deque
import copy

with open('/Users/marcus/Documents/advent/adventofcode/day 13/input.txt', 'r') as myfile:
    puzzle_input=myfile.readlines()

firewall = {}
for p in puzzle_input:
    m = re.search('(\d+)\:\s+(\d+)', p)
    #firewall[int(m.group(1))] = (deque([0]*int(m.group(2))),'+')
    #firewall[int(m.group(1))][0][0] = 'S'
    firewall[int(m.group(1))] = [0] * int(m.group(2))

def passTroughFw(delay):
    severity = 0
    times = 0
    for i in range(0,max(firewall, key=int)+1):
        if i not in firewall:
            continue

        if  (i+delay) % ((len(firewall[i])-1) * 2) == 0:
            severity +=  i * len(firewall[i])
            times += 1

    return (severity, times)

def part1():
    print passTroughFw(0)[0]

def part2():
    severity = -1
    delay = 1
    while 1:
        (severity, times) = passTroughFw(delay)
        if times == 0:
            break
        delay += 1
    print delay





#part1()

part2()
