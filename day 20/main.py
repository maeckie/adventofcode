#!/usr/bin/python
import re
import copy
with open('/Users/marcus/Documents/advent/adventofcode/day 20/input.txt', 'r') as myfile:
    lines=myfile.readlines()


def part1():
    particles = {}
    #p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
    i = 0
    for l in lines:
        m = re.search('p=<(.*)>,\s+v=<(.*)>,\s+a=<(.*)>',l)
        p = m.group(1).split(',')
        v = m.group(2).split(',')
        a = m.group(3).split(',')
        particles[i] = {}
        p = map(int, p)
        v = map(int, v)
        a = map(int, a)
        particles[i]['p'] = p
        particles[i]['v'] = v
        particles[i]['a'] = a
        particles[i]['d'] = p[0]
        i += 1

    for x in range(10000):
        for p in particles:
            #print particles[p]['d']
            for i in range(3):
                particles[p]['v'][i] += particles[p]['a'][i]
            for i in range(3):
                particles[p]['p'][i] += particles[p]['v'][i]
            particles[p]['d'] = sum(map(abs,particles[p]['p']))

    x = (0,10000000000)
    for p in particles:
        if x[1] > particles[p]['d']:
            x = (p, particles[p]['d'])

    print "%d: %d" % x

def part2():
    particles = {}
    allPos = {}
    #p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
    i = 0
    for l in lines:
        m = re.search('p=<(.*)>,\s+v=<(.*)>,\s+a=<(.*)>',l)
        p = m.group(1).split(',')
        v = m.group(2).split(',')
        a = m.group(3).split(',')
        particles[i] = {}
        p = map(int, p)
        v = map(int, v)
        a = map(int, a)
        particles[i]['p'] = p
        particles[i]['v'] = v
        particles[i]['a'] = a
        particles[i]['d'] = p[0]
        i += 1


    for x in range(10000):
        for ap in allPos:
            if len(allPos[ap]) > 1:
                for i in allPos[ap]:
                    if i in particles:
                        del particles[i]

        print len(particles)
        print x
        for p in particles:
            for i in range(3):
                particles[p]['v'][i] += particles[p]['a'][i]
            for i in range(3):
                particles[p]['p'][i] += particles[p]['v'][i]
            val = hash(str(particles[p]['p']))
            if val not in allPos:
                allPos[val] = []
            allPos[val].append(p)


    print "We have %d particles left" % len(particles.keys())
    for x in particles:
        print x


part2()
