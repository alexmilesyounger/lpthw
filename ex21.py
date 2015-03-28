def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b


def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d\n" % (
	age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, 
	divide(iq, 2))))

print "That becomes:", what, "Can you do it by hand?\n"

half_iq = divide(iq, 2)
weight_times_half_iq = multiply(weight, half_iq)
height_minus_wthiq = subtract(height, weight_times_half_iq)
age_plus_hmwthiq = add(age, height_minus_wthiq)
what_reborn = age_plus_hmwthiq

print "I just did it by hand. The answer is %d." % what_reborn