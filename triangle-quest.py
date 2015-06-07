# https://www.hackerrank.com/challenges/python-quest-1

# This article really helps make sense of repdigits and how to figure them out

for i in range(1, input()):
    print ((10 ** i - 1) / 9) * i
