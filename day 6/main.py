#!/usr/bin/python
import sys

#puzzle_input = [0,2,7,0]
puzzle_input = "4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3".split('\t')
puzzle_input = map(int, puzzle_input)

results = {}
cycle = 0
while 1:
    shuffle = max(puzzle_input)
    pos = puzzle_input.index(max(puzzle_input))
    shuffle = puzzle_input[pos]
    puzzle_input[pos] = 0
    pos += 1

    while shuffle > 0:
        if pos == len(puzzle_input):
            pos = 0
        puzzle_input[pos] += 1
        shuffle -= 1
        pos += 1
    list_hash = hash(tuple(puzzle_input))
    cycle += 1
    if list_hash in results:
        print "Cycles since last time: %d" % (cycle - results[list_hash])
        print "It took: %d cycles" % cycle
        sys.exit(1)
    else:
        results[list_hash] = cycle
