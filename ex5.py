# _*_ coding: utf-8 _*_

name = 'Alex Miles Younger'
age = 33 # not a lie
height = 74 # inches
h_centimeters = height * 2.54
weight = 198 # lbs
w_kilograms = weight * (1.0 / 0.453592)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "If we're using the metric system he's %d centimeters \
tall and %d kilograms heavy." % (h_centimeters, w_kilograms)

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)

# Print an %r variable, shows quotes
print "Go fuck yourself %r you're an asshole." % (name)

# Print an %s variable, just string
print "Go fuck yourself %s you're an asshole." % (name)

# Print an %r variable, shows digit
print "Go fuck yourself %r you're an asshole." % (h_centimeters)

# Print an %d variable, just integer
print "Go fuck yourself %d you're an asshole." % (h_centimeters)


