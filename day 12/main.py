#!/usr/bin/python
import re
import operator

with open('/Users/marcus/Documents/advent/adventofcode/day 12/input.txt', 'r') as myfile:
    puzzle_input=myfile.readlines()

pos = '0'
dic = {}
programs = {}
usedVals = []

for p in puzzle_input:
    m = re.search('^(.*)<->(.*)$', p)
    dic[m.group(1).strip()] = map(str.strip, m.group(2).split(','))

def part1():
    programs['0'] = dic['0']
    while 1:
        keys = len(programs.keys())
        for d in programs.keys():
            for p in programs[d]:
                if p not in programs:
                    programs[p] = dic[p]
        if keys == len(programs.keys()):
            break


    print len(set(programs))

def findAll(index):
    programs[index] = dic[index]
    while 1:
        keys = len(programs.keys())
        for d in programs.keys():
            for p in programs[d]:
                if p not in programs:
                    programs[p] = dic[p]
                    usedVals.append(p)
        if keys == len(programs.keys()):
            return 1
def part2():
    groups = 0
    for i in range(0,2000):
        if str(i) not in usedVals:
            groups += findAll(str(i))

    print groups
part2()
