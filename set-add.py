# https://www.hackerrank.com/challenges/py-set-add

n = int(raw_input())

countries = set() 

for _ in xrange(n):
    countries.add(raw_input())

print len(countries)
