import re
import sys

# https://www.hackerrank.com/challenges/hackerrank-tweets

count = int(sys.stdin.readline().strip())

tweets = []
for x in xrange(count):
	tweets.append(sys.stdin.readline().strip())

regex = re.compile(r"hackerrank", re.IGNORECASE)

tweet_count = 0
for tweet in tweets:
	if regex.findall(tweet):
		tweet_count += 1

print tweet_count
