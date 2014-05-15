from math import sqrt
import sys

# https://www.hackerrank.com/challenges/map-and-lambda-expression

# lazily borrowed a fast fib method from SO
#	http://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence-in-python

# Since this problem focuses on map and lambda I used them as much as possible

fib = lambda n: int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
cube = lambda n: n * n * n

count = int(sys.stdin.readline().strip())

print map(cube, map(fib, xrange(count)))
