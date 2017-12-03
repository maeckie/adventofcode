#!/usr/bin/python
import math
import numpy as np

#37  36  35  34  33  32  31
#38  17  16  15  14  13  30
#39  18   5   4   3  12  29
#40  19   6   1   2  11  28
#41  20   7   8   9  10  27
#42  21  22  23  24  25  26
#43  44  45  46  47  48  49

puzzle_input=289326


def part1():
    lower_right_corner = 1
    square_size = 1
    laps = 1

    while lower_right_corner < puzzle_input:
        square_size = square_size + 2
        lower_right_corner = square_size * square_size
        laps=laps+1

    to_edge = laps-1
    for i in range(0,4):

        lower_right_corner = lower_right_corner - (square_size-1)
        to_mid_on_edge = 0

        if lower_right_corner < puzzle_input:
            mid_on_edge = math.ceil(float(square_size)/float(2))
            pos_on_edge = puzzle_input - lower_right_corner + 1

            if pos_on_edge > mid_on_edge:
                to_mid_on_edge = pos_on_edge - mid_on_edge
            else:
                to_mid_on_edge = mid_on_edge - pos_on_edge

            print "Manhattan: %d" % (to_mid_on_edge + to_edge)
            break


def getSumNeighbours(matrix, x, y):
    nSum = 0
    nSum = nSum + matrix[x-1][y-1]
    nSum = nSum + matrix[x][y-1]
    nSum = nSum + matrix[x+1][y-1]
    nSum = nSum + matrix[x-1][y]
    nSum = nSum + matrix[x+1][y]
    nSum = nSum + matrix[x-1][y+1]
    nSum = nSum + matrix[x][y+1]
    nSum = nSum + matrix[x+1][y+1]

    return nSum

def part2():
    matrix = np.zeros((100,100), dtype=np.int)

    x = 50
    y = 50
    matrix[x][y] = 1
    d = 1
    steps = 1
    it = 0
    exit = 0
    while 1:
        for t in range(0,2):
            for i in range(0,steps):

                direction = [[1,0], [0,1], [-1,0], [0,-1]]
                x = x + direction[d][0]
                y = y + direction[d][1]


                matrix[x][y] = getSumNeighbours(matrix, x, y)
                if matrix[x][y] > puzzle_input:
                    print matrix[x][y]

                    exit = 1
                    break


            if exit == 1:
                break
            d = d + 1
            if d > 3:
                d = 0


        steps = steps + 1
        if exit == 1:
            break


#part1()
part2()
