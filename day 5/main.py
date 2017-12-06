#!/usr/bin/python

with open('/Users/marcus/Documents/advent/adventofcode/day 5/input.txt', 'r') as myfile:
    puzzle_input=myfile.readlines()

#puzzle_input = [0,3,0,1,-3]
puzzle_input = [x.strip() for x in puzzle_input]
puzzle_input = map(int, puzzle_input)

def part1():

    i = 0
    steps = 0
    while 1:
        if i > len(puzzle_input)-1:
            print "Out of the maze in %d steps" % steps
            break
        current = puzzle_input[i]
        puzzle_input[i] += 1
        i += current
        steps += 1

def part2():
    i = 0
    steps = 0
    while 1:
        if i > len(puzzle_input)-1:
            print "Out of the maze in %d steps" % steps
            print puzzle_input
            break
        current = puzzle_input[i]
        puzzle_input[i] += -1 if puzzle_input[i] >= 3 else 1
        i += current
        steps += 1

#part1()
part2()
