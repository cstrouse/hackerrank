# https://www.hackerrank.com/challenges/python-mutations

s = list(raw_input())
i, l = raw_input().split()

s[int(i)] = l

print "".join(s)
