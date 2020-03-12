"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Solving linear systems using Gaussian Elimination

"""

import numpy as np
from numpy.linalg import solve

# Solving A*x = b
A=np.array([[1,0.67,0.33],[0.45,1,0.55],[0.67,0.33,1]])
b=np.array([2,2,2])
x=solve(A,b)
# The solution for x is [1,1,1], Which matches with the manual calculation
