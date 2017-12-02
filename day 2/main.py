#!/usr/bin/python

with open('/Users/marcus/Documents/advent/adventofcode/day 2/input.txt', 'r') as myfile:
    spreadsheet=myfile.readlines()

checksum = 0
for row in spreadsheet:
    row = row.replace('\n','').split('\t')
    row = map(int, row)
    row.sort()
    checksum = checksum + row[-1] - row[0]


print checksum
