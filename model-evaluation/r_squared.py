
import numpy as np

def r_squared(y_true, y_pred):
	mean = np.mean(y_true)
	SSR=np.sum(abs(y_true - y_pred)**2)
	SST=np.sum(abs(y_true - mean)**2)
	r_squared=1-SSR/SST
	return r_squared

y_true = np.array([1, 2, 3, 4, 5])
y_pred = np.array([1.1, 2.1, 2.9, 4.2, 4.8])
print(r_squared(y_true, y_pred))


# 0.989

# Task: Compute the R-squared Value in Regression Analysis
# R-squared, also known as the coefficient of determination, 
# is a measure that indicates how well the independent variables 
# explain the variability of the dependent variable in a regression model.

# Your Task: To implement the function r_squared(y_true, y_pred) 
# that calculates the R-squared value, given arrays of true values y_true and predicted values y_pre

