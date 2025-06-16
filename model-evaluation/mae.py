import numpy as np

def mae(y_true, y_pred):
    return round((np.sum(np.abs(y_true - y_pred)) / y_true.size),3)

y_true = np.array([[0.5, 1], [-1, 1], [7, -6]])
y_pred = np.array([[0, 2], [-1, 2], [8, -5]])

print(mae(y_true, y_pred))

# 0.750