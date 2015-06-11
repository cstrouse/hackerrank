# https://www.hackerrank.com/challenges/python-tuples

# NOTE: You must convert the inputs to int in order for the hash() call to return the proper outputs

n = int(raw_input())
t = tuple(map(int, raw_input().split()))

print hash(t)
