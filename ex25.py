def break_words(stuff):
	"""This function will break up words for us."""
	# It actually breaks strings into words. 
	# split(...)
 	# |      S.split([sep [,maxsplit]]) -> list of strings
 	# |
	# |      Return a list of the words in the string S, 
	# | 	 using sep as the delimiter string.  If maxsplit is given, 
	# | 	 at most maxsplit splits are done. If sep is not specified 
	# | 	 or is None, any whitespace string is a separator and 
	# | 	 empty strings are removed from the result.
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	# Oh, look, another built-in function I don't know
	# I wonder wht sorted does
	# I'm going to need to look all of this up once I have
	# internet access... or actually I don't...
	# I bet I can use pydoc even when I'm offline. 
	# I can. I can use pydoc offline. 
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off."""
	# Oh, HI pop() what do you do?
	# https://docs.python.org/2/library/stdtypes.html
	# It looks like you pull that thing out of the string 
	# and then return it. 
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)


