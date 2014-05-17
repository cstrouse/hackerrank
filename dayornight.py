import sys

# https://www.hackerrank.com/challenges/digital-camera-day-or-night

# Pixel color values are in the format of (B,R,G)
raw_data = sys.stdin.readline().strip().split()
pixels = []
lum_sum = 0
for pixel in raw_data:
	pixel = map(float, pixel.split(","))
	pixels.append(pixel)
	# Close enough calculation of luminance
	lum_sum += ((0.16 * pixel[0]) + (0.33 * pixel[1]) + (0.59 * pixel[2]))

avg_luminance = lum_sum / len(pixels)
# Fails test 15; marks as day but should be night
#   Haven't been able to find the magic threshold
if avg_luminance > 46:
	print "day"
else:
	print "night"
