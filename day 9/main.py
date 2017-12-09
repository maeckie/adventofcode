#!/usr/bin/python
import sys
with open('/Users/marcus/Documents/advent/adventofcode/day 9/input.txt', 'r') as myfile:
    puzzle_input=''.join(line.rstrip() for line in myfile)


#puzzle_input = '{}' ## 1
#puzzle_input = '{{{}}}' ## 6
#puzzle_input = '{{},{}}' ## 5
#puzzle_input = '{{{},{},{{}}}}' ## 16
#puzzle_input = '{<a>,<a>,<a>,<a>}' ## 1
#puzzle_input = '{{<ab>},{<ab>},{<ab>},{<ab>}}' ## 9
#puzzle_input = '{{<!!>},{<!!>},{<!!>},{<!!>}}' ## 9
#puzzle_input = '{{<a!>},{<a!>},{<a!>},{<ab>}}' ## 3
#puzzle_input = '<random characters>' ## 17
#puzzle_input = '<<<<>' ## 3
#puzzle_input = '<{!>}>' ## 2
#puzzle_input = '<!!>' ## 0
#puzzle_input = '<!!!>>' ## 0
#puzzle_input = '<{o"i!a,<{i<a>' ## 10

stack = []
summa = 0
in_garbage = False
i = 0
garbCount = 0
while i < len(puzzle_input):
    if puzzle_input[i] == '!':
        i += 2
        continue
    if not in_garbage and puzzle_input[i] == '<':
        i += 1
        in_garbage = True
        continue
    if puzzle_input[i] == '>':
        in_garbage = False
    if in_garbage:
        garbCount += 1
        i += 1
        continue
    if puzzle_input[i] == '{':
        stack.append(i)
    if puzzle_input[i] == '}':
        summa += len(stack)
        stack.pop()
    i += 1


print "The sum of all groups are: %d" % summa
print "The garbage count is: %d" % garbCount
