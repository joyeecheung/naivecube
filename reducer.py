#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys

def read_input(file):
	for line in file:
		yield line.rstrip().split('\t')

def main():
	data = read_input(sys.stdin)
	for rvalue, group in groupby(data, itemgetter(0)):
 		ids = set(count for rvalue, count in group)
 		print "%s\t%d" % (rvalue, len(ids))	

if __name__ == "__main__":
	main()

