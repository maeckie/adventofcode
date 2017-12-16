#!/usr/bin/python
from collections import deque
import copy
import re
with open('/Users/marcus/Documents/advent/adventofcode/day 16/input.txt', 'r') as myfile:
    puzzle_input=''.join(line.rstrip() for line in myfile)

dancers = deque(list('abcdefghijklmnop'))
puzzle_input = puzzle_input.split(',')
all_uniq = []
#puzzle_input = 's1,x3/4,pe/b'.split(',')
#dancers = deque(list('abcde'))

def spin(inp, dancers):
    m = re.search('s(\d+)', inp)
    return dancers.rotate(int(m.group(1)))

def swapOnPos(inp, dancers):
    m = re.search('x(\d+)\/(\d+)', inp)
    a = int(m.group(1))
    b = int(m.group(2))
    tmp = dancers[a]
    dancers[a] = dancers[b]
    dancers[b] = tmp

def swapOnName(inp, dancers):
    m = re.search('p(\w)\/(\w)', inp)
    a = list(dancers).index(m.group(1))
    b = list(dancers).index(m.group(2))
    tmp = dancers[a]
    dancers[a] = dancers[b]
    dancers[b] = tmp

def dance(dancers, puzzle_input):
    for p in puzzle_input:
        if 's' in p:
            spin(p, dancers)
        elif 'x' in p:
            swapOnPos(p, dancers)
        elif 'p' in p:
            swapOnName(p, dancers)

## part 1:
def part1():
    dance(dancers, puzzle_input)
    print ''.join(dancers)

def part2():
    i = 0
    d_cpy = copy.deepcopy(dancers)
    while 1:
        dance(dancers, puzzle_input)
        if dancers not in all_uniq:
            all_uniq.append(copy.deepcopy(dancers))
        else:
            break
        i += 1
    actual_iterations = 1000000000 % i

    print actual_iterations
    for i in range(actual_iterations):
        dance(d_cpy, puzzle_input)

    print ''.join(d_cpy)



#print ''.join(dancers)
part2()
