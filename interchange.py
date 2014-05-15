import sys

# https://www.hackerrank.com/challenges/interchange-two-numbers

a,b = sys.stdin.readline(), sys.stdin.readline()

(a,b) = (b,a)

print "%s\n%s" % (a,b)
