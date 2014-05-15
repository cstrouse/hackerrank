import sys

# https://www.hackerrank.com/challenges/finding-the-percentage

student_count = int(sys.stdin.readline().strip())

scores = []
for x in xrange(student_count):
	temp = sys.stdin.readline().split()
	scores.append({
		"name": temp[0],
		"score1": float(temp[1]),
		"score2": float(temp[2]),
		"score3": float(temp[3])
	})

target_student = sys.stdin.readline().strip()

t_scores = scores[next(index for (index, d) in enumerate(scores) if d["name"] == target_student)]

print "%0.2f" % ((t_scores["score1"] + t_scores["score2"] + t_scores["score3"]) / 3.0)
