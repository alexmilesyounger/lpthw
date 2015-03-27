print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)


print "Hi"
kickoff = raw_input()
print "What's your name?"
name = raw_input()
print "Welcome to the game, %s. Are you ready to play?" % name
ready = raw_input()

print '''
So, %s. It's gonna be %s, for you by way of %s, huh? 
Ok.
Let's go. 
''' % (name, ready, kickoff)
