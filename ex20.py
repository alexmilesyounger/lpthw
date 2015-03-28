# Import the sys module and the argv module
from sys import argv

# Set the args for argv
script, input_file = argv

# Define the print_all function
def print_all(f):
	print f.read()

# Define the rewind function
def rewind(f):
	# seek() moves around the file in bytes
	f.seek(0)			# seek(0) moves to the 0th byte

# Define the print_a_line function
def print_a_line(line_count, f):
	print line_count, f.readline()

# Set var current_file to the contents of the input_file
current_file = open(input_file)

# Run the print_all function using the contents of the input_file
print "First let's print the whole file:\n"

print_all(current_file)

# Rewind the contents of the input_file
print "Now let's rewind, kind of like a tape.\n"

rewind(current_file)

# Print three lines using the print_a_line function
print "Let's print three lines:\n"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)