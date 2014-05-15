import re
import sys

# https://www.hackerrank.com/challenges/valid-pan-format

count = int(sys.stdin.readline().strip())

tests = []
for x in xrange(count):
	tests.append(sys.stdin.readline().strip())

regex = re.compile(r"[A-Z]{5}\d{4}[A-Z]")

for test in tests:
	if len(test) == 10:
		if regex.findall(test):
			print "YES"
		else:
			print "NO"
	else:
		print "NO"
