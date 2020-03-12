"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Finding Eigen values using QR Decomposition

"""
import numpy as np
from numpy.linalg import eigh
from numpy.linalg import qr

A=np.array([[5,-2],[-2,8]])      
D=A                                  # Taking a iteration variable D
for i in range(50):
    q,r=qr(D)                        # Finding the QR decomposition of D  
    D=np.dot(r,q)                    # updating D with r.q 
    print("D",D)                     # After some iterations D becomes diagonal matrix
print("Using QR ",np.diag(D))        # the diagonal elements are the eigen values and D is similarty transform of A
E=eigh(A)                           
print("Using Eigh ",E[0])            # Printing the eigen values using inbuilt function eigh 

#  The Eigen values match 
