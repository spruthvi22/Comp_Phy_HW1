"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Finding Singular Value Decompoition

"""

import numpy as np
import numpy.linalg as lin
import time

A=np.array([[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]])
strt_tim=time.time()
E=lin.eigh(np.dot(np.transpose(A),A))       # Finding Eigen values and vectors of A'.A
ix=E[0].argsort()[::-1]                     # Rearranging Eigen values in decending order 
S=E[0][ix]
V=np.transpose(E[1][:,ix])                  # Rearranging Eigen vectors according to eigen values and taking tranpose to get V
Ue=lin.eigh(np.dot(A,np.transpose(A)))      # Finding Eigen values and vectors of A.A'
ixu=E[0].argsort()[::-1]                    # Rearranging Eigen values in decending order
U=(Ue[1][:,ixu])                            # Rearranging Eigen vectors according to eigen values and taking tranpose to get U
end_time=time.time()
print("S using Code =",np.sqrt(S))
print("Time of execution using code =", (end_time-strt_tim))

strt_tim=time.time()
U,S,V=lin.svd(A)                            # Using svd library function  
end_time=time.time()
print("S uding svd function =",S)
print("Time of execution svd function =", (end_time-strt_tim))

# The values of V match, with exception of negative signs in spesific rows (if v is normalized eigen vector then -v is also normalized eigen vector)
# The values of U match, with exception to eigen vectors corrosponding to 0, which do not make any difference to svd
