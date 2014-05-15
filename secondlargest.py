import sys

# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

count = int(sys.stdin.readline().strip())

numbers = [int(x) for x in sys.stdin.readline().strip().split()]
numbers = list(set(numbers))
numbers.sort()

print numbers[len(numbers) - 2]
