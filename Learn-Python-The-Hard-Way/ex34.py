animals = ['bear', 'python', 'peacock','kangraoo', 'whale', 'platypus']
i = 0
while i < 6:
  if i == 0:
    print "The 1st animal is at %d and is a %s." % (i, animals[i])
    i = i + 1
  elif i == 1:
    print "The 2nd animal is at %d and is a %s." % (i, animals[i])
    i = i + 1
  elif i == 2:
    print "The 3rd animal is at %d and is a %s." % (i, animals[i])
    i = i + 1
  else:
    print "The %dst animal is at %d and is a %s." % ((i + 1), i, animals[i])
    i = i + 1
