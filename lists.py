# https://www.hackerrank.com/challenges/python-lists

# TODO: Rewrite using dict instead of if/elif

cmd_count = int(raw_input())

L = []

for i in xrange(cmd_count):
    cmd = raw_input().split()
    if cmd[0] == "insert":
        L.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == "remove":
        L.remove(int(cmd[1]))
    elif cmd[0] == "append":
	L.append(int(cmd[1]))
    elif cmd[0] == "sort":
	L.sort()
    elif cmd[0] == "reverse":
	L.reverse()
    elif cmd[0] == "pop":
	L.pop()
    elif cmd[0] == "print":
        print L
