#!/usr/bin/python

with open('/Users/marcus/Documents/advent/adventofcode/day 8/input.txt', 'r') as myfile:
    instructions=myfile.readlines()

registry = {}

def initReg(a, b):
    if a not in registry:
        registry[a] = 0
    if b not in registry:
        registry[b] = 0

def actualModify(modify, operation, by):
    if operation == 'dec':
        registry[modify] -= int(by)
    else:
        registry[modify] += int(by)


def modifyReg(modify, operation, by, compareWith, compWay, compValue):
    compValue = int(compValue)
    if compWay == '>':
        if registry[compareWith] > compValue:
            actualModify(modify, operation, by)
    elif compWay == '<':
        if registry[compareWith] < compValue:
            actualModify(modify, operation, by)
    elif compWay == '>=':
        if registry[compareWith] >= compValue:
            actualModify(modify, operation, by)
    elif compWay == '<=':
        if registry[compareWith] <= compValue:
            actualModify(modify, operation, by)
    elif compWay == '==':
        if registry[compareWith] == compValue:
            actualModify(modify, operation, by)
    elif compWay == '!=':
        if registry[compareWith] != compValue:
            actualModify(modify, operation, by)
    else:
        print "We found an unknown operator: %s" % compareWith
        sys.exit(1)

maxEver = 0

for instruction in instructions:
    (modify, operation, by, om, compareWith, compWay, compValue) = map(str.rstrip,instruction.split(' '))
    initReg(modify, compareWith)
    modifyReg(modify, operation, by, compareWith, compWay, compValue)
    if registry[max(registry, key=registry.get)] > maxEver:
        maxEver = registry[max(registry, key=registry.get)]
    #print registry

print "The max value is %d" % registry[max(registry, key=registry.get)]
print "The max value ever is: %d" % maxEver
