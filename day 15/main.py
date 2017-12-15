#!/usr/bin/python

a_fact = 16807
b_fact = 48271
a = 634
b = 301
div = 2147483647

def part1():
    matches = 0
    for i in range(40000000):
        a = (a * a_fact) % div
        b = (b * b_fact) % div
        if list("{0:032b}".format(a))[-16:] == list("{0:032b}".format(b))[-16:]:
            matches += 1
        if i % 500000 == 0:
            print "loop nr: %d" % i

    print "Found a total of %d" % matches

def part2():
    a_list = []
    b_list = []
    matches = 0
    a_fact = 16807
    b_fact = 48271
    a = 634
    b = 301
    div = 2147483647

    while len(a_list) < 5000000 or len(b_list) < 5000000:
        a = (a * a_fact) % div
        b = (b * b_fact) % div
        if len(a_list) < 5000000 and a % 4 == 0 :
            a_list.append(list("{0:032b}".format(a))[-16:])
            if len(a_list) % 500000 == 0:
                print "A list len: %d" % len(a_list)
        if len(b_list) < 5000000 and  b % 8 == 0:
            b_list.append(list("{0:032b}".format(b))[-16:])
            if len(b_list) % 500000 == 0:
                print "B list len: %d" % len(b_list)

    for i in range(5000000):
        if a_list[i] == b_list[i]:
            matches += 1

    print "Found a total of: %d" % matches


part2()
