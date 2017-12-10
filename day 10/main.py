#!/usr/bin/python

import sys

#skip = [3, 4, 1, 5]
#size = 5
skip = [31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33]
size = 256
c_list = [i for i in range(size)]



pos = 0
skip_size = 0
for s in skip:
    if s > len(c_list):
        pos += 1
        continue
    tmp = []
    j = pos
    k = pos
    for i in range(pos, pos + s):
        tmp.append(c_list[j % len(c_list)])
        j += 1

    for i in list(reversed(tmp)):
        c_list[k % len(c_list)] = i
        k += 1
    #print c_list


    pos = (j+skip_size) % len(c_list)
    skip_size += 1
    #print tmp
print c_list[0]*c_list[1]




#print resList
