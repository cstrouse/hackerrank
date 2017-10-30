if __name__ == '__main__':
  n = int(raw_input())

  if n & 1:
    print "Weird"
  if not n & 1:
    if n >= 2 and n <= 5:
      print "Not Weird"
    if n >= 6 and n <= 20:
      print "Weird"
    if n > 20:
      print "Not Weird"

