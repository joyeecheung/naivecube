#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys


def read_input(file):
    for line in file:
        yield line.rstrip().split('\t')


def main():
    data = read_input(sys.stdin)
    for key, group in groupby(data, itemgetter(0)):
        ids = set(uid for key, uid in group)
        print "%s\t%d" % (key, len(ids))

if __name__ == "__main__":
    main()
