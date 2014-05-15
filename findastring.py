import re
import sys

# https://www.hackerrank.com/challenges/find-a-string

haystack = sys.stdin.readline().strip()
needle = sys.stdin.readline().strip()

# finds overlapping matches
print len(re.findall("(?=%s)" % needle, haystack))
