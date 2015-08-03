import random

"""
Generate n list of boolean values representing
switches that are on or off
"""
def rand_bools(n):
    r = random.getrandbits(n)
    return list( ( bool((r>>i)&1) for i in xrange(n) ) )

"""
Get list of 100 random boolean items
"""
switches = rand_bools(100)
# determine what pass it is

def count_switches(switches):
	"""
	:param switches: list of booleans
	:returns count of switches turned on once pass algorithm has occured"
	"""
	pass_count = 0
	# iterate over switches
	for i in switches:
		# generate duple of index and value
		for x in enumerate(switches):
			# only on first pass
			if pass_count == 0:
				# switch every value
				switches[x[0]] = not x[1]
			else:
				# consider offset b/c arrays start at 0
				offset_pass_count = pass_count + 1
				# flip switch on nth item excluding first items
				if x[0] % offset_pass_count == 0 & x[0] != 0:
					switches[x[0]] = not x[1]
			# increase pass count
			pass_count += 1 
	#  sum of all switches turned on		
	return sum(switches)

print count_switches(switches)


