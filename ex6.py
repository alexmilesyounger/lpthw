# Define variable x
x = "There are %d types of people. " % 10

# Define variable binary
binary = "binary" 

# Define variable do_not
do_not = "don't"

# Define variable y using variables binary, and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

# Print X
print x

# Print Y
print y

# Print X w/ quotes
print "I said: %r" % x

# Print y w/ quotes
print "I also said: '%s'." % y

# Define variable hilarious as boolean false
hilarious = False

# Define variable joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

# Print joke_evaluation using variable hilarious
print joke_evaluation % hilarious

# Define variables w, and e
w = "This is the left side of..."
e = "a string with a right side."

# Print variables w, e and combine the results as strings
print w + e