import math

def softmax(scores: list[float]) -> list[float]:
	# softmax = e*x/sum(e**x)
    probabilities=[]
    for x in scores:
        probabilities.append(round(math.exp(x) / sum([math.exp(i) for i in scores]),4))
    return probabilities

scores = [1, 2, 3]

print(softmax(scores))

# [0.0900, 0.2447, 0.6652]

