import math
import sys

# https://www.hackerrank.com/challenges/angry-children

n, k = int(sys.stdin.readline().strip()), int(sys.stdin.readline().strip())

packets = []
for x in xrange(n):
	packets.append(int(sys.stdin.readline().strip()))

packets.sort()

# NOTE: Not 100% clear on why this is, but was able to get it working; didn't fully
#	understand the instructions; reached solution after reading comments
unfairness = max(packets[:k]) - min(packets[:k])
for y in xrange(1, n - k):
	if (packets[y + k - 1] - packets[y]) < unfairness:
		unfairness = packets[y + k -1] - packets[y]

print unfairness
