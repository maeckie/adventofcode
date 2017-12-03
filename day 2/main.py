#!/usr/bin/python

with open('/Users/marcus/Documents/advent/adventofcode/day 2/input.txt', 'r') as myfile:
    spreadsheet=myfile.readlines()

def part1():
    checksum = 0
    for row in spreadsheet:
        row = row.replace('\n','').split('\t')
        row = map(int, row)
        row.sort()
        checksum = checksum + row[-1] - row[0]


    print "Part 1: %d" % (checksum)

def part2():
    checksum = 0
    for row in spreadsheet:
        row = row.replace('\n','').split('\t')
        row = map(int, row)
        row.sort()
        for t in row:
            for n in row:
                div = float(t)/float(n)
                if div.is_integer() and t != n:
                    checksum = checksum + int(div)


    print "Part 2: %d" % (checksum)




part1()
part2()
