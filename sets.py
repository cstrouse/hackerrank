import sets
import sys

# https://www.hackerrank.com/challenges/sets

m = int(sys.stdin.readline().strip())
m_ints = set(sys.stdin.readline().strip().split())

n = int(sys.stdin.readline().strip())
n_ints = set(sys.stdin.readline().strip().split())

results = list(m_ints.symmetric_difference(n_ints))
results.sort(key=int)

for num in results:
	print num
