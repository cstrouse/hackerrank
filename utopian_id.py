import re
import sys

# https://www.hackerrank.com/challenges/utopian-identification-number

count = int(sys.stdin.readline().strip())
ids = []
for x in xrange(count):
	ids.append(sys.stdin.readline().strip())

regex = re.compile(r"^[a-z]{,3}\d{2,8}[A-Z]{3,}$")

for id in ids:
	if regex.findall(id):
		print "VALID"
	else:
		print "INVALID"
