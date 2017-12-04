#!/usr/bin/python

with open('/Users/marcus/Documents/advent/adventofcode/day 4/input.txt', 'r') as myfile:
    passfile=myfile.readlines()

def part1():
    valid = 0
    for line in passfile:
        words = line.split()
        if len(words) == len(set(words)):
            valid += 1

def part2():
    valid = 0
    for line in passfile:
        words = line.split()
        sorterad =  map(lambda x: ''.join(sorted(x)), words)
        if len(sorterad) == len(set(sorterad)):
            valid += 1

    print valid


#part1()
part2()
