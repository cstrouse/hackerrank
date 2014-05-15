import sets
import sys

# https://www.hackerrank.com/challenges/gem-stones

# I'm unsure why this was worth 60 points when it was so simple and
#	also wonder why there were so few solutions submitted

count = int(sys.stdin.readline().strip())
gemstones = []
for gem in xrange(count):
	gemstones.append( set( list( sys.stdin.readline().strip() ) ) )

print len(set.intersection(*gemstones))
