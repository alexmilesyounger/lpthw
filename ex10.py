tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list: 
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
Is it hard to put things in "quotes" when you're using triple-double-quotes?
"""

# You can't comment out stuff in triple single-or-double-quotes
# Carriage returns destroy everything before them it seems
thin_cat = '''
I'll do a list:\n\t* Cat food\n\t* Fishies\n\t* Catnip\n\t* Grass
How do you work with Carriage Returns?
Here's a phrase with a \r Carriage Return right before this word. 
What's it look like?
How do you put things in "quotes" when you're using triple-single-quotes?
There's a line of string variables like %s and %s and %s.
''' % ('gold', 'black', 'tan')


striped_cat = '''
I'll do a list:\n\t* Cat food\n\t* Fishies\n\t* Catnip\n\t* Grass
How do you work with Carriage Returns?
Here's a phrase with a \r Carriage Return right before this word. 
What's it look like?
How do you put things in "quotes" when you're using triple-single-quotes?
There's a line of rep variables like %r and %r and %r.
''' % ('gold', 'black', 'tan')


print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print thin_cat
print striped_cat

# while True: 
# 	for i in ["/","-","|","\\","|"]:
# 		print "%s\r" % i,

print "\\" # Backslash
print "\'" # Single-quote
print "\"" # Double-quote
print "\f" # formfeed
print "\n" # linefeed
print "\r ASCII" # Carriage Return
print "\t ASCII" # Horizontal Tab
print "\v" # Vertical Tab


