import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	probabilities = []
	z=[]
	for feature in features:
		suma=0
		for idx, feat in enumerate(feature):
			suma += (weights[idx]*feat)
		z.append(suma+bias)
	probabilities = [round( 1 / (1 + math.exp(-i)),4) for i in z]
	suma = 0
	for idx, value in enumerate(labels):
		suma += (probabilities[idx]-value)**2
	mse = round(suma / len(labels),4)
	return probabilities, mse

features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]]
labels = [0, 1, 0]
weights = [0.7, -0.4]
bias = -0.1
print(single_neuron_model(features, labels, weights, bias))

# ([0,4626, 0,4134, 0,6682], 0.3349)
	# mse = (1 / len(z)) * (sum([for i in range(len(z)) for j in range(len(z)) if labels[i] != probabilities[i]]))


# 0,21399876
# 0,34409956
# 0,44649124

# 1,00458956