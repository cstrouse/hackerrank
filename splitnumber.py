import re
import sys

# https://www.hackerrank.com/challenges/split-number

count = int(sys.stdin.readline().strip())

raw = []
for x in xrange(count):
	raw.append(sys.stdin.readline().strip())

regex = re.compile(r"(\d{,3})[- ](\d{,3})[- ](\d{4,10})")

for raw_phone in raw:
	phone_num = regex.findall(raw_phone)[0]
	print "CountryCode=%s,LocalAreaCode=%s,Number=%s" % (phone_num[0], phone_num[1], phone_num[2])
