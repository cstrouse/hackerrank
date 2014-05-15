import re
import sys

# https://www.hackerrank.com/challenges/saying-hi

count = int(sys.stdin.readline().strip())
lines = []
for x in xrange(count):
	lines.append(sys.stdin.readline().strip())

regex = re.compile(r"^hi.[^d]", re.IGNORECASE)
for line in lines:
	if regex.findall(line):
		print line
