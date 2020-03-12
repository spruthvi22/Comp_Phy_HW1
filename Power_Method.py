"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Solving for dominant eigen value and vector using Power method

"""

import numpy as np
import numpy.linalg as lin
from numpy.linalg import eigh

A=np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])
n=np.shape(A)[0]
e=0
x=np.ones([n,])
for i in range(100):
    x=np.dot(A,x)       # On contineously taking xi+1 = A.xi, we reach closer to xi becoming eigen vector
    e1=lin.norm(x)      # After many iterations if x is normalized eigen vector then norm of new x is eigen value
    x=x/e1
    if np.abs((e1-e)/e1)<0.001:  # Finding the eigen value to 0.1% of previous value (spesifiying accuracy)
        break
    e=e1

print("Eigen Value =",e1)
print("Eigen Vector =",x)
