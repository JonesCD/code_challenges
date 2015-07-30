"""
Consider a function incr_dict, which takes two arguments, which behaves like this in Python:
>>> dct = {}
>>> incr_dict(dct, ('a', 'b', 'c'))
>>> dct
{'a': {'b': {'c': 1}}}
>>> incr_dict(dct, ('a', 'b', 'c'))
>>> dct
{'a': {'b': {'c': 2}}}
>>> incr_dict(dct, ('a', 'b', 'f'))
>>> dct
{'a': {'b': {'c': 2, 'f': 1}}}
>>> incr_dict(dct, ('a', 'r', 'f'))
>>> dct
{'a': {'r': {'f': 1}, 'b': {'c': 2, 'f': 1}}}
>>> incr_dict(dct, ('a', 'z'))
>>> dct
{'a': {'r': {'f': 1}, 'b': {'c': 2,'f': 1}, 'z': 1}}
>>>

incr_dict(dct, ('a', 'b', 'c')) is conceptually like:
dct['a']['b']['c'] += 1
except that it creates any necessary intermediate and leaf nodes.

* Implement incr_dict in Python or any language that supports dictionaries.
* Write executable tests for your function.
* Will your implementation continue to work well if the tuple is extremely long?
"""

# create function with parameters dct and the coming input
def incr_dict(dct, newinput):
	
	# In conditions where 'ab' is followed by 'abc' the structure is ambiguous. 
	# Since operational use for the function isn't known, I
	# will return an error in cases where the structure is unclear.
	# This happens when dct is not a dictionary and tries to 
	# append the tuple count.
	if type(dct) is not dict:
		print "Ambiguous structure. You created a case where"
		print "your input treats a leaf as a node."
		print "Ignoring most recent input, and moving on with last dct."
		return dct

	else:
		# First, imagine an input tuple that's empty
		if len(newinput) == 0:
			return dct
		
		# Now, imagine an input tuple of one thing, 
		# this will be the terminating condition too
		elif len(newinput) == 1:
			# see if it's already in the dictionary 
			if newinput[0] in dct:
				# In a case where 'abc' is followed by 'ab', there is an ambiguity.
				# The structure isn't defined, so it's safest to return an error,
				# and return to the previous point, allowing the user to try a
				# new tuple. In this case the newinput pushes the count to increment
				# on the dictionary parameter.
				if type(dct[newinput[0]]) is not int:
					print "Ambiguous structure. You created a case where"
					print "your input treats a node as a leaf."
					print "Ignoring most recent input, and moving on with last dct."
					return dct
				else:
					dct[newinput[0]] += 1
			else:
				dct[newinput[0]] = 1
			return dct
	
		else:
			# now we need to deal with longer input tuples
			# start with first bit, if it's not already in dictionary, and create room if not
			if not newinput[0] in dct:
				dct[newinput[0]] = {}
		
			# then onward! The recursive part:
			# makes the first value a new layer of dictionary, and assigned the
			# rest of the input as another new input, then run again until all 
			# the bits of the input are used				
			incr_dict(dct[newinput[0]], newinput[1:])
			return dct
		
			
			
			
def main():
	print "----------"
	print "\nI've initiated dct = {} for you." 
	print "Would you like to run a set of examples or enter your own tuples?"
	print "Or I can run some automated tests for you."
	print "Type either 'examples' or 'own' or 'test'"
	print "Or type 'quit' to leave."
	choice = raw_input("> ")
	
	if "example" in choice:
		print "----------"
		dct = {}
		print dct
		incr_dict(dct, ('a', 'b', 'c'))
		print dct
		incr_dict(dct, ('a', 'b', 'c'))
		print dct
		incr_dict(dct, ('a', 'b', 'f'))
		print dct
		incr_dict(dct, ('a', 'r', 'f'))
		print dct
		incr_dict(dct, ('a', 'z'))
		print dct
		main()
	
	elif "own" in choice:
		dct = {}
		print "----------"
		print "\nUse CRTL+C to exit at any time"
		print "Enter a new tuple, following this example: abc"
		print "Please do not add any spaces or commas"
		
		while True:
			fromuser = raw_input("> ")
			incr_dict(dct, tuple(fromuser))
			print dct
			
	elif "test" in choice:
		print "----------"
		print "\nThere are a few tests."
		tests()
		
	elif "quit" in choice:
		print "----------"
		print "Bye!"
		exit(0)
			
	else:
		print "\nI didn't understand your choice. Type examples OR own OR test only."
		main()
		
def tests():
	print "\nThere are nine tests ready to run."
	print "I will run them in order for you."
	print "Then you will have the option to run long tuples that may crash."
	
	
	print "\n0: works with empty input tuple"
	dct = {}
	incr_dict(dct, ())
	print dct
		
	print "\n1: works with input tuple length 1"
	dct = {}
	incr_dict(dct, ('a',))
	print dct
	
	print "\n2: works with input tuple length 2"
	dct = {}
	incr_dict(dct, ('a', 'b'))
	print dct
	
	print "\n3: throws error on leaf to node"
	incr_dict(dct, ('a', 'b', 'c'))
	print dct
		
	print "\n4: works with input tuple length 3"
	dct = {}
	incr_dict(dct, ('a', 'b', 'c'))
	print dct
	
	print "\n5: throws error on ambiguous back node"
	incr_dict(dct, ('a', 'b'))
	print dct
		
	print "\n6: increments repeated tuple correctly"
	dct = {}
	incr_dict(dct, ('a', 'b', 'c'))
	incr_dict(dct, ('a', 'b', 'c'))
	print dct
	
	print "\n7: branches correctly"
	incr_dict(dct, ('a', 'b', 'f'))
	print dct
	
	print "\n8: can take empty tuple even at this point"
	incr_dict(dct, ())
	print dct
	
	print "\nWould you like to test some very long tuples now? y or n"
	option = raw_input("> ")
	
	if "y" in option:
		dct = {}
		incr_dict(dct, ('a', 'b', 'c') * 50)
		print dct
		dct = {}
		incr_dict(dct, ('a', 'b', 'c') * 100)
		print dct
		dct = {}
		incr_dict(dct, ('a', 'b', 'c') * 200)
		print dct
		dct = {}
		incr_dict(dct, ('a', 'b', 'c') * 300)
		print dct
		print "\nThat just ran tuple a, b, c, 50 times, then 100 times,"
		print "then 200 times, then 300 times for recursion depth."
		print ""
		print "There is a recursion limit in Python that ruins inputs "
		print "that are longer than 1000 recursions. Would you like to"
		print "change that limit now to go further? y or n"
		
		increase = raw_input("> ")
		
		if "y" in increase:
			import sys
			sys.setrecursionlimit(10000)
			dct = {}
			incr_dict(dct, ('a', 'b', 'c') * 3000)
			print dct
			print "\nThat just ran for 3000 recursions."
			print "This would fail after 10,000 recursions. It's also taxing"
			print "the stack. If longer input tuples are desired, an iterative"
			print "program would be better, but this is easier to maintain if"
			print "it is adequate for the recursion depth required to the task."
			
		else:
			main()
	
	else:
		main()


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass