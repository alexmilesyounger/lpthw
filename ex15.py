# Import the sys module and the argv function
# from sys import argv

# Unpack argv, script is required, 
# then one argument for each variable we want
# script, filename = argv

# Define text as the contents of filename
filename = raw_input("What file would you like to work with? ")
txt = open(filename)

# Print quote + variable
print "Here's your file %r:" % filename

# Print contents read() of txt variable
print txt.read()
txt.close()


# Accept new input for file_again var
print "Type the filename again:"
file_again = raw_input("> ")

# Define txt_again as the contents of file_again
txt_again = open(file_again)

# Print contents read() of txt_again var
print txt_again.read()
txt_again.close()