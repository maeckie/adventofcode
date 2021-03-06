#!/usr/bin/python
from collections import deque

def part1():
    circular_buffer = [0]
    pos = 0
    for i in range(1,2018):
        for j in range(367):
            pos += 1
            if pos == len(circular_buffer):
                pos = 0
        pos += 1
        circular_buffer.insert(pos, i)

    print circular_buffer[pos+1]


def part1_better():
    circular_buffer = [0]
    pos = 0
    for i in range(1,2018):
        pos = (367 + pos) % i
        pos += 1
        circular_buffer.insert(pos, i)
    print circular_buffer[pos+1]


def part2():
    circular_buffer = deque([0])
    for i in range(1,50000000):
        circular_buffer.rotate(-367)
        circular_buffer.append(i)
    print circular_buffer[list(circular_buffer).index(0)+1]

def part2_better():
    circular_buffer = [0]
    pos = 0
    keep = 0
    for i in range(1,50000000):
        pos = (367 + pos) % i
        pos += 1
        if pos == 1:
            keep = i
        #circular_buffer.insert(pos, i)

    print keep
    #25674054

part1()
part1_better()
part2()
part2_better()
