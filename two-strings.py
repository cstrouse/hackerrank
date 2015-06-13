# https://www.hackerrank.com/challenges/two-strings

t = int(raw_input())

for _ in xrange(t):

    a = set(raw_input())
    b = set(raw_input())

    if len(a.intersection(b)) > 0:
        print "YES"
    else:
        print "NO"
