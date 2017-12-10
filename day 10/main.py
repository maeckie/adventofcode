#!/usr/bin/python

import sys

#skip = [3, 4, 1, 5]
#size = 5
skip = "31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33"
part1_skip = [31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33]
size = 256
c_list = [i for i in range(size)]


def part1():
    pos = 0
    skip_size = 0
    for s in part1_skip:
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


        pos = (j+skip_size) % len(c_list)
        skip_size += 1
    product = c_list[0]*c_list[1]
    print "Part 1 product is: %d" % product

def part2(skip):

    ascii_skip = []
    l_suff = [17, 31, 73, 47, 23]
    skip = skip.split(',')

    for s in skip:
        for c in s:
            ascii_skip.append(ord(c))
        ascii_skip.append(ord(','))
    ascii_skip =  ascii_skip[:-1]
    ascii_skip.extend(l_suff)

    pos = 0
    skip_size = 0
    skip = map(ord,str(map(str, skip)))
    for it in range(64):
        for s in ascii_skip:
            s = int(s)
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
    chunks = [c_list[16*i:16*(i+1)] for i in range(len(c_list)/16 + 1)]
    finalHash = ""
    for c in chunks:
        if len(c) > 0:
            xor = reduce(lambda x,y:int(x)^int(y),c)
            finalHash = finalHash + format(xor, '02x')
    print "Part 2 hash is: " + finalHash

part1()
part2(skip)
