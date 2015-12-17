from string import split

# https://www.hackerrank.com/challenges/any-or-all

def is_palindrome(x):
    if int(str(x)[::-1]) is x:
        return True
    return False

def is_positive(x):
    if x > 0:
        return True
    return False

n = int(raw_input())
nums = map(lambda x: int(x), split(raw_input()))

if all([is_positive(x) for x in nums]):
    if any([is_palindrome(x) for x in nums]):
        print True
    else:
        print False
else:
    print False
