def format_factorials(n, lim):
	"""
	:param n: start item
	:param lim: stop item
	:returns list: of factorial items
	"""
	flag = 0 
	factorials = []
	for i in range(n, 0,-1):
		if flag < lim:
			factorials.append(i)
			flag += 1
	return factorials

def sum_factorials(factorial_list):
	"""
	:param factorial_list: list of int items
	:returns product of the list items
	"""
	return reduce(lambda x, y: x*y, factorial_list)


def fact_lim(n, lim):
	"""
	:main function: given n and lim calculate the summation of factorials 
	with constraints of n to n-lim
	"""
	grand_total = 0
	for i in range(n, 0,-1):
		if lim != 1:
			factorials = format_factorials(i, lim)
			factorial_total = sum_factorials(factorials)
			grand_total += factorial_total
		else:
			grand_total += i 
	return grand_total
	
print fact_lim(2, 1)
