"""
Filters duplicate IDs in Android resource folders.
author: chris @ sihrc
updated: 6-22-2014
"""
import os, re, sys

def walk_through(path):
	for dirpath, dirnames, filenames in os.walk(path):
		for filename in filenames:
			if (".xml" == filename[-4:]):
				#print "Found XML file: %s" % filename
				extractIDs(os.path.join(dirpath, filename))

def extractIDs(path):
	with open(path, 'rb') as f:
		for line in f:
			results = regex.search(line)
			if (results != None):
				matched = results.group(1)
				#print "\tFound id: %s" % matched
				if (matched in ids):
					found += 1
					ids[results.group(1)].append(path)
					print "Duplicate id: %s\n\tfound in:\n\t %s" % (matched, "\n\t".join(ids[matched]))
				else: 
					ids[results.group(1)] = [path]


if __name__ == "__main__":
	regex = re.compile("\\@\\+id/(.*)\"")
	ids = dict()
	found = 0
	print "Looking for duplicate IDs"

	walk_through(sys.argv[1])
	if (found == 0):
		print "Congratulations, none found."
