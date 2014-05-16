import re
import sys

# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter

count = int(sys.stdin.readline().strip())
emails = []
for x in xrange(count):
	emails.append(sys.stdin.readline().strip())

# not optimal; struggled with a few of the test addresses slipping through
#	that had @@ in the domain
regex = re.compile(r"^[a-zA-Z0-9-_]+\@[^@_]*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$")

validated_emails = filter(lambda e: regex.findall(e), emails)
print sorted(validated_emails, key=str.lower)
