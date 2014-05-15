import sys
import xml.etree.ElementTree as etree

# https://www.hackerrank.com/challenges/xml-1-find-the-score

count = int(sys.stdin.readline().strip())
data = ""
for x in xrange(count):
	data += sys.stdin.readline().strip()

tree = etree.ElementTree(etree.fromstring(data))

score = 0

for elem in tree.iter():
	score += len(elem.attrib)

print score
