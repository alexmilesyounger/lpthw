print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 10000
# beans doesn't look right, I think that should be jelly_beans 
# or it should be an array or some other kind of variable. 
# actually if secret_formula returns jelly_beans and that is then piped into beans
# this might just work, but it's funny to create a new variable for jars and crates
# or to reset the values of each. 

# Teacher answer: inside of a function a variable is temporary, it's actually
# arbitary that the other two match. What we're really doing is assinging the 
# return values of the funtion to non-temporary variables. 
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "Wed'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)