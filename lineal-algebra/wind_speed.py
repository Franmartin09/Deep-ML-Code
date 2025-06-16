from cmath import sqrt
import numpy as np
def compute_wind_speed(u, v):
    # Your code here
    return [(sqrt(u[0]**2 + u[1]**2)).real, (sqrt(v[0]**2 + v[1]**2)).real]


print(compute_wind_speed(np.array([3, 4]), np.array([4, 3])))
