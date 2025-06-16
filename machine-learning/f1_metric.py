import numpy as np

def calculate_f1_score(y_true, y_pred):
	y_true=np.array(y_true)
	y_pred=np.array(y_pred)

	TP = np.sum((y_true==1) & (y_pred==1))
	FP = np.sum((y_true==0) & (y_pred==1))
	FN = np.sum((y_true==1) & (y_pred==0))
	precision = TP / (TP + FP) if (TP + FP) > 0 else 0
	recall = TP / (TP + FN)	if (TP + FN) > 0 else 0
	if (precision + recall) == 0:
		return 0.0
	f1 = 2 * (precision*recall) / (precision + recall)
	return round(f1,3)

y_true = [1, 0, 1, 1, 0]
y_pred = [1, 0, 0, 1, 1]
print(calculate_f1_score(y_true, y_pred))
# 0.667
