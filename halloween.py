import sys

# https://www.hackerrank.com/challenges/halloween-party

count = int(sys.stdin.readline().strip())
cuts= []
for x in xrange(count):
	cuts.append(int(sys.stdin.readline().strip()))

# read editorial before coming to solution
for k in cuts:
	if (k % 2) == 0:
		print (k / 2 ) * (k / 2)
	else:
		print (k /2 ) * (k / 2 + 1)
