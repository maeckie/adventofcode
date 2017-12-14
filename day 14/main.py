#!/usr/bin/python

import sys
import operator

def knotHash(inp):
    ls = map(ord, inp.strip())
    ls = ls + [17,31,73,47,23]
    xs = range(0, 256)
    pos = 0
    ss = 0
    inc = lambda x, d: (x + d) % len(xs)
    for _ in range(64):
        for l in ls:
            idxs = [inc(pos, i) for i in range(l)]
            vals = reversed([xs[i] for i in idxs])
            for i, v in zip(idxs, vals):
                xs[i] = v
            pos += l + ss
            ss += 1

    ys = []
    for i in range(0, len(xs), 16):
        block = (xs[j] for j in range(i, i+16))
        n = reduce(operator.xor, block)
        y = hex(n)[2:]
        if len(y) == 1:
            y = '0'+y
        ys.append(y)
    return ''.join(ys)


def findNeighbours(x,y):
    if res[x][y] == '1':
        res[x][y] = 'X'
    else:
        return

    if y-1 < 0:
        my = 0
    else:
        my = y-1
    if y+1 == len(res[x]):
        py = len(res[x])-1
    else:
        py = y+1
    if x+1 == len(res):
        px = len(res)-1
    else:
        px = x+1
    if x-1 < 0:
        mx = 0
    else:
        mx = x-1


    findNeighbours(x,py)
    findNeighbours(x,my)
    findNeighbours(mx,y)
    findNeighbours(px,y)



puzzle_input = 'ljoxqyyw'
#puzzle_input = 'flqrgnkx'
c_list = [i for i in range(256)]


cnt = 0
groups = 0
res = {}
poo = {}
for i in range(0,128):
    h = knotHash(puzzle_input + '-' + str(i) )
    cnt += ''.join(map(lambda z: bin(int(z, 16))[2:].zfill(4), h)).count('1')
    res[i]  = list(''.join(map(lambda z: bin(int(z, 16))[2:].zfill(4), h)))



groups = 0
for i in range(len(res)):
    for j in range(len(res[i])):
        if res[i][j] == '1':
            findNeighbours(i,j)
            groups += 1
        #print poo


print "Used count is: %d" % cnt
print "Found groups: %d" % groups
