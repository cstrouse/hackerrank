import sys

# https://www.hackerrank.com/challenges/basic-calculator

x, y = float(sys.stdin.readline().strip()), float(sys.stdin.readline().strip())

print "%.2f" % (x + y)
print "%.2f" % (x - y)
print "%.2f" % (x * y)
print "%.2f" % (x / y)
print "%.2f" % (x // y)
