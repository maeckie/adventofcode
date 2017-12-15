#!/usr/bin/python



def part1():
    a_fact = 16807
    b_fact = 48271
    a = 634
    b = 301
    div = 2147483647
    matches = 0
    for i in range(40000000):
        a = (a * a_fact) % div
        b = (b * b_fact) % div
        if (a & 0xffff) == (b & 0xffff):
            matches += 1

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
            a_list.append((a & 0xffff))
        if len(b_list) < 5000000 and  b % 8 == 0:
            b_list.append((b & 0xffff))


    for i in range(5000000):
        if a_list[i] == b_list[i]:
            matches += 1

    print "Found a total of: %d" % matches

#part1()
part2()
