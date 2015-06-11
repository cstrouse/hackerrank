# https://www.hackerrank.com/challenges/python-quest-1

# This article really helps make sense of repdigits and how to figure them out
#   http://www.fact-index.com/r/re/repunit.html

for i in range(1, input()):
    print ((10 ** i - 1) / 9) * i
