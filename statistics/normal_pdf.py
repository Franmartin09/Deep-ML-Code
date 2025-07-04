import math

def normal_pdf(x, mean, std_dev):
	"""
	Calculate the probability density function (PDF) of the normal distribution.
	:param x: The value at which the PDF is evaluated.
	:param mean: The mean (μ) of the distribution.
	:param std_dev: The standard deviation (σ) of the distribution.
	"""
	# Your code here
	return round((math.exp(-(((x-mean)**2) / (2*(std_dev**2))))) / (math.sqrt(2*math.pi*(std_dev**2))),5)



print(normal_pdf(16, 15, 2.04))
# 0.17342
print(normal_pdf(0, 0, 1))
# 0.39894
print(normal_pdf(1, 0, 0.5))
# 0.10798