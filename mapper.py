#!/usr/bin/env python
import sys
from itertools import *

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def read_input(file):
    for line in file:
        yield line.split()

def main():
    data = read_input(sys.stdin)
    C = [i for i in powerset([2,3,4,5,6,7])]
    for e in data:
        for R in C:
            k = [e[i] for i in R]
            print "%s|%s\t%s" % (' '.join([str(i) for i in R]), ' '.join(k), str(e[1]))

if __name__ == "__main__":
    main()

