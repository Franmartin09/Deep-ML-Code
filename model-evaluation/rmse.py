
import numpy as np
import math

def rmse(y_true, y_pred):
    mse = np.mean((y_true - y_pred) ** 2)
    rmse_res = np.sqrt(mse)
    return round(rmse_res,3)


y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])
print(rmse(y_true, y_pred))

# 0.612

# sqrt((0.5^2 + 0.5^2 + 0^2 + 1^2) / 4) = 0.612