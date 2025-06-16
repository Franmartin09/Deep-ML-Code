import math

def poisson_probability(k, lam):
	"""
	Calculate the probability of observing exactly k events in a fixed interval,
	given the mean rate of events lam, using the Poisson distribution formula.
	:param k: Number of events (non-negative integer)
	:param lam: The average rate (mean) of occurrences in a fixed interval
	"""
	# Your code here
	# f(x)=lam^x/x! * e^-lam
	return lam**k/math.factorial(k) * math.exp(-lam)


k = 3
lam = 5
print(poisson_probability(k, lam))
# 0.14037

# Write a Python function to calculate the probability of observing exactly k events 
# in a fixed interval using the Poisson distribution formula. The function should take 
# k (number of events) and lam (mean rate of occurrences) as inputs and return the
# probability rounded to 5 decimal places.
# The function calculates the probability for a given number of events occurring in a fixed interval, based on the mean rate of occurrences.