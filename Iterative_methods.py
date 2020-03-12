"""
Author: Pruthvi Suryadevara
Email:  pruthvi.suryadevara@tifr.res.in
Solving linear systems using Recurssive Methods

"""
import numpy as np

x_f=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163]) #Actual Solution 
A=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]]) # A Mtrix for solving A*x=b
b=np.array([1,2,3,4,5])
n=len(b)
x_0=np.array([0.0,0.0,0.0,0.0,0.0]) # Initial Solution

### Using Jacobi Method
I=np.identity(n)
D=A*I            # Diagonal matrix of A
R=A-D            # Sum of lower and Upper Trangular Matrices
x=x_0            # Initialize x to initial solution
D_I=np.identity(n)
for i in range(n):
    D_I[i,i]=1/D[i,i]  # Finding inverse of D, which is inverse of individual eements

for i in range(500):
    x=np.dot(D_I,(b-np.dot(R,x)))             # Finding xi+1 = D^-1*(b-(R.xi))
    if np.amax(np.absolute(x-x_f))<0.01:      # Condition for rquired accuracy
        break
print("Using Jacobi method",i+1)
print("Solution =",x)
###


### Using Gauss-Sidel Method
x=x_0            # Initialize x to initial solution
for i in range(500):
    for j in range(n):
        d=b[j]                 # Taking a variable d which equals b(j)-(A(j,0)*x(0) + A(j,1)*x(1) ...... + A(j,n)x(n)) 
        for k in range(n):
            if(j!=k):
                d=d-(A[j][k]*x[k])
        x[j]=(d/A[j][j])                   # finding updated jth component of x using  x(j)i+1 = d/A(j,j)  
    if np.amax(np.absolute(x-x_f))<0.01:   # As x(0 to j-1)are updated and used to find in finding d the method is gauss sidel
        break
print("Using Gauss Sidel method",i+1)
print("Solution =",x)
###


### Using Relaxation method
x=np.array([0.0,0.0,0.0,0.0,0.0])  # Initializing x to initial solution
w=1.25  # Relaxation coefficient
for i in range(500):
    for j in range(n):
        d=b[j]
        for k in range(n):
            if(j!=k):
                d=d-(A[j][k]*x[k])
        x[j]=(w*(d/A[j][j]))+(x[j]*(1-w))   # Adding a extra relaxation to Gauss Sidel
    if np.amax(np.absolute(x-x_f))<0.01:
        break
print("Using Relaxation method",i+1)
print("Solution =",x)
###


### Conjugate Gradient method
x=np.array([0.0,0.0,0.0,0.0,0.0])   # initializing x to initial solution
r_0=b-np.dot(A,x)
p=r_0
for i in range(500):
    al=(np.dot(r_0,r_0))/(np.dot(p,np.dot(A,p)))
    x=x+(al*p)
    r_1=r_0-(al*np.dot(A,p))
    be=(np.dot(r_1,r_1))/(np.dot(r_0,r_0))
    p=r_1+(be*p)
    r_0=r_1
    if np.amax(np.absolute(x-x_f))<0.01:
        break
print("Using CD method",i+1)
print("Sloution =",x)
###

