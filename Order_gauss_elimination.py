"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Finding the order of gauss elimination

"""

import numpy as np
from numpy.linalg import solve
from numpy.random import rand
import time
from scipy.optimize import curve_fit

# Defining a function to fit the time of execttion vs size of matrix of form [execttion time = constant n^(constant)] 
def pwr(n,a,b):
    return((a*(n**b)))

# Solving for execttion time for n in range 500 to 1000
n=np.geomspace(500,10000,20)     # Using geometric spacing for better accuracy       
n=n.astype(int)
exec_time=[]
for i in n:
    A=100*rand(i,i)              # Creating random matris A of size n*n                 
    b=1000*rand(i)               # Creating random vectro b of size n
    strt_tim=time.time()
    x=solve(A,b)                 # Solving A.x=b
    end_time=time.time()
    exec_time.append(end_time-strt_tim)
popt,pcov=curve_fit(pwr,n,np.array(exec_time))  # Fitting the function to find the order
print(popt[1])  # Order comes out to be around 3
