import sys

# https://www.hackerrank.com/challenges/hackerrank-language

count = int(sys.stdin.readline().strip())
requests = []
for x in xrange(count):
	requests.append(sys.stdin.readline().strip().split())

langs = ("C","CPP","JAVA","PYTHON","PERL","PHP","RUBY","CSHARP",
	 "HASKELL","CLOJURE","BASH","SCALA","ERLANG","CLISP",
	 "LUA","BRAINFUCK","JAVASCRIPT","GO","D","OCAML","PASCAL",
	 "SBCL","DART","GROOVY","OBJECTIVEC","R")

for request in requests:
	if request[1] in langs:
		print "VALID"
	else:
		print "INVALID"
