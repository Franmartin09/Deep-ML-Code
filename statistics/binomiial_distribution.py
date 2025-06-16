import math

def binomial_probability(n, k, p):
	"""
    Calculate the probability of achieving exactly k successes in n independent Bernoulli trials,
    each with probability p of success, using the Binomial distribution formula.
    """
	# Your code here
	probability = (math.factorial(n) / (math.factorial(n-k)*math.factorial(k))) * p**k * (1-p)**(n-k)
	return round(probability, 5)


n = 6
k = 2
p = 0.5
print(binomial_probability(n, k, p))
# 0.23438


# The function calculates the Binomial probability, the intermediate steps include calculating the binomial coefficient, raising p and (1-p) to the appropriate powers, and multiplying the results.