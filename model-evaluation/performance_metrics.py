import numpy as np

def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
	# Implement your code here
	actual=np.array(actual)
	predicted=np.array(predicted)
	
	TP = float(np.sum((actual==1) & (predicted==1)))
	FN = float(np.sum((actual==1) & (predicted==0)))
	FP = float(np.sum((actual==0) & (predicted==1)))
	TN = float(np.sum((actual==0) & (predicted==0)))
	
	precision = TP / (TP + FP) if (TP + FP) > 0 else 0
	recall = TP / (TP + FN)	if (TP + FN) > 0 else 0
	
	accuracy = float(np.mean(actual == predicted))
	
	if (precision + recall) == 0:
		f1 = 0
	else:
		f1 = float(2 * (precision*recall) / (precision + recall))
		
	confusion_matrix =[[TP,FN],[FP,TN]]
	specificity = TN / (TN + FP)
	negativePredictive = TN / (TN + FN)
	return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)


actual = [1, 0, 1, 0, 1]
predicted = [1, 0, 0, 1, 1]
print(performance_metrics(actual, predicted))

# ([[2, 1], [1, 1]], 0.6, 0.667, 0.5, 0.5)
	