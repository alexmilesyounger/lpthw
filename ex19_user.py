def user_wants_a_cookie(have_you_been_good, when_is_it):
	print "So, you want a cookie, huh?"
	print "Well, since it's %s and since you've been %s" % (when_is_it, have_you_been_good)
	print "You can have a cookie.\n"

# Call with variables
yes_been_good = 'Yes'
time_for_cookie = 'Now'

user_wants_a_cookie(yes_been_good, time_for_cookie)	

# Call with direct input
user_wants_a_cookie('Sort of', 'About now-ish')

# Call with direct input mix of string and integer
user_wants_a_cookie('I\'ve been very good', 8)