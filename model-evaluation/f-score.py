import numpy as np

def f_score(y_true, y_pred, beta):
    TP = np.sum((y_true==1) & (y_pred==1))
    FP = np.sum((y_true==0) & (y_pred==1))
    FN = np.sum((y_true==1) & (y_pred==0))
    precision = TP / (TP + FP)
    recall = TP / (TP+ FN) if (TP + FN) > 0 else 0
    return round((1+(beta**2)) * (precision*recall) / (((beta**2) * precision ) + recall), 4)


y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])
beta = 1

print(f_score(y_true, y_pred, beta))

# 0.857