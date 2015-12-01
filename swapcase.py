# https://www.hackerrank.com/challenges/swap-case

s = list(raw_input())

def swap(s):
    if s.isupper():
       return s.lower()
    else:
       return s.upper()

print ''.join( [swap(l) for l in s] )
