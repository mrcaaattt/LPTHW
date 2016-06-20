from sys import argv

script, first, second, third = argv
fourth = raw_input("What is the fourth thing you want to say? ")

print "So first you said %r then %r and then %r and finally you said %r" % (first, second, third, fourth)
