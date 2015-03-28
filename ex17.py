from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# # We could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()

# One line - works but fails to close in_file at bottom of script
indata = open(from_file).read()

# # One line does not work
# indata = open.read(from_file)

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

# # Close files using new variable names
# out_file.close()
# in_file.close()

# Close files using old variable names
from_file.close()
to_file.close()