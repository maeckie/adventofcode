#!/usr/bin/python
import math

#37  36  35  34  33  32  31
#38  17  16  15  14  13  30
#39  18   5   4   3  12  29
#40  19   6   1   2  11  28
#41  20   7   8   9  10  27
#42  21  22  23  24  25  26
#43  44  45  46  47  48  49

puzzle_input=289326
#puzzle_input=12

lower_right_corner = 1
square_size = 1
laps = 1

while lower_right_corner < puzzle_input:
    square_size = square_size + 2
    lower_right_corner = square_size * square_size
    print lower_right_corner
    laps=laps+1

print "------"

#print lower_right_corner
#print square_size
#print puzzle_input
#distance from center to edge of spiral
print "SQ Size: %d" % (square_size)
print "Laps: %d" % laps
to_edge = laps-1
for i in range(0,4):

    lower_right_corner = lower_right_corner - (square_size-1)
    print "lower_right: %d" % lower_right_corner
    to_mid_on_edge = 0

    if lower_right_corner < puzzle_input:
        print "in the loop: %d" % i
        print i
        print puzzle_input
        print lower_right_corner
        mid_on_edge = math.ceil(float(square_size)/float(2))
        pos_on_edge = puzzle_input - lower_right_corner + 1

        if pos_on_edge > mid_on_edge:
            to_mid_on_edge = pos_on_edge - mid_on_edge
        else:
            to_mid_on_edge = mid_on_edge - pos_on_edge

        print "mid_on_edge: %d" % mid_on_edge
        print "to_mid_on_edge: %d" % (to_mid_on_edge)
        print "to_edge: %d" % (to_edge)
        print "Manhattan: %d" % (to_mid_on_edge + to_edge)
        break

# for i in range(1,5):
#     lower_right_corner = lower_right_corner - square_size-1
#     if lower_right_corner < puzzle_input:
#         edge_pos = puzzle_input - lower_right_corner
#         print "edge_pos_1: %d" % (edge_pos)
#         mid_pos = (square_size-1)/2+1
#         if edge_pos > mid_pos:
#             distance_to_mid = edge_pos - mid_pos
#         else:
#             distance_to_mid = mid_pos - edge_pos
#
#         print "to_edge: %d" % (to_edge)
#         print "distance_to_mid: %d" % (distance_to_mid)
#         print "edge_pos: %d" % (edge_pos)
#         print "mid_pos: %d" % (mid_pos)
#         manhattan_distance = to_edge + distance_to_mid
#
# print manhattan_distance

#find where we are on the edge
#while lower_right_corner > puzzle_input:



#manhattan_distance = to_edge + edge_distance_from_mid
#print manhattan_distance
