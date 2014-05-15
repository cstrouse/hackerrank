import sys

# https://www.hackerrank.com/challenges/whats-your-name

fname, lname = sys.stdin.readline(), sys.stdin.readline()
print "Hello %s %s! You just delved into python." % (fname.strip(), lname.strip())
