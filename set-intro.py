from string import split

# https://www.hackerrank.com/challenges/py-introduction-to-sets

num_plants = int(raw_input())
heights = map(lambda x: int(x), set(split(raw_input())))
print sum(heights) / float(len(heights))
