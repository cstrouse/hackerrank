# https://www.hackerrank.com/challenges/python-string-formatting

n = int(raw_input())

colwidth = len(bin(n)[2:])

for num in range(1, n+1):
    for base in 'doXb':
        print '{0:{width}{base}}'.format(num, base=base, width=colwidth),
    print
