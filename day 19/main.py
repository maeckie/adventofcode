#!/usr/bin/python
import sys
with open('/Users/marcus/Documents/advent/adventofcode/day 19/input.txt', 'r') as myfile:
    lines=myfile.readlines()

maze = {}
i = 0
direction = {'U':[-1,0], 'D': [1,0], 'L': [0,-1], 'R': [0,1]}
d = 'D'
mlen = 0
for l in lines:
    if len(l) > mlen:
        mlen = len(l)

for l in lines:
    maze[i]= []
    for p in l:
        maze[i].append(p)
        maze[i]
    maze[i].pop()
    while len(maze[i]) < mlen:
        maze[i].append(' ')

    i += 1

pos = [0,maze[0].index('|')]


def getDirection(pos, d):
    y = pos[0]
    x = pos[1]
    if len(maze[y]) > 0 and maze[y][x-1] != ' ' and d != 'R':
        return 'L'

    if x+1 < len(maze[y]):
        if maze[y][x+1] != ' ' and d != 'L':
            return 'R'
    if y-1 >=0:
        print
        if maze[y-1][x] != ' ' and d != 'D':
            return 'U'
    if y+1 < len(maze.keys()) and  maze[y+1][x] != ' ' and d != 'U':
        return 'D'



letters = ''
steps = 1
while 1:

    if maze[pos[0]][pos[1]] == '+':
        d = getDirection(pos,d)


    if maze[pos[0]][pos[1]] in 'ABCDEFGHIJKLMNOPQRSTUVXYZ':
        letters += maze[pos[0]][pos[1]]


    pos[0] += direction[d][0]
    pos[1] += direction[d][1]
    if pos[0] < 0 or pos[0] > len(maze.keys()) or pos[1] < 0 or pos[1] >=len(maze[pos[0]]) or maze[pos[0]][pos[1]] == ' ':
        print "The letters are: %s" % letters
        print "The number of steps are: %d " % steps
        break
    steps += 1
