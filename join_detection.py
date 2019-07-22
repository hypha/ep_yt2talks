#!/usr/bin/env python3
import sys

def human_duration(seconds):
    return '%02d:%02d:%02d' % (
            seconds // 3600,
            seconds % 3600 // 60,
            seconds % 60 )


threshold = 120



l = []
with open(file = sys.argv[1]) as f:
    (segstart,segend) = (0,0)
    for line in f:
        k = [float(x) for x in line.strip().split(" ")[1:]]
        if segstart == 0:
            # This is our first pair
            (segstart,segend) = k
        #print(k,(segstart,segend),(k[0] - segend))
        if k[0] - segend > threshold:
            l.append([segstart, segend])
            (segstart,segend) = k
        else:
            # Keep extending the segment
            segend=k[1]
    l.append([segstart,k[1]])
print(["%s - %s" % (human_duration(x[0]),human_duration(x[1])) for x in l])
