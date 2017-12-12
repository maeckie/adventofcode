#!/usr/bin/python
import operator
import sys
with open('/Users/marcus/Documents/advent/adventofcode/day 11/input.txt', 'r') as myfile:
    puzzle_input=''.join(line.rstrip() for line in myfile)

directions = {}

directions['n'] =  [0,1,-1]
directions['ne'] = [-1,1,0]
directions['se'] = [-1,0,1]
directions['s'] =  [0,-1,1]
directions['sw'] = [1,-1,0]
directions['nw'] = [1,0,-1]



puzzle_input = puzzle_input.split(',')
#puzzle_input = ['ne','ne','ne', 'sw','sw','sw']
#puzzle_input = ['ne','ne','sw','sw']
#puzzle_input = ['se','sw','se','sw','sw']

z = [(1,2,3), (1,2,3), (2,5,6)]
print reduce((lambda x,y: map(operator.add, x,y)), z)
sys.exit(1)
### Alternative as a one liner. Not keeping track of max distance :(
# print max(map(abs,reduce((lambda x, y: map(operator.add,x,y)), map(lambda a: directions[a], puzzle_input))))

dist = [0,0,0]
m_dist = 0

for p in puzzle_input:
    x = directions[p]
    for i in range(0,len(dist)):
        dist[i] += x[i]
    if max(map(abs, dist)) > m_dist:
        m_dist = max(map(abs, dist))


dist = map(abs, dist)
print "Disance from centre: %d" % max(dist)
print "Max distance EVER from centre: %d" % m_dist
