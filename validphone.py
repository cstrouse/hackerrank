import re
import sys

# https://www.hackerrank.com/challenges/regex-1-validating-the-phone-number

count = int(sys.stdin.readline().strip())
nums = []
for x in xrange(count):
	nums.append(sys.stdin.readline().strip())

regex = re.compile(r"^[789]\d{9}$")

for num in nums:
	if regex.findall(num):
		print "YES"
	else:
		print "NO"
