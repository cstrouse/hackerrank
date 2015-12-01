# https://www.hackerrank.com/challenges/gem-stones

# I'm unsure why this was worth 60 points when it was so simple and
#	also wonder why there were so few solutions submitted

count = int(raw_input())

gemstones = []

for _ in xrange(count):
	gemstones.append( set( list( raw_input() ) ) )

print len(set.intersection(*gemstones))
