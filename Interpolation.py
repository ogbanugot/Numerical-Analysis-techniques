import scipy
''' Interpolation methods for polynomial p(x), p'(x), I(x)
    N = degree of the polynomial
    A = dictionary of coefficient of the terms, for k = 0,1,2....N
    x = independent variable
    c = constant of integration
    scipy.linspace(start,stop,interval)...just a more efficient version of range 
    '''
N = 3
A = {0:2.08,1:-0.14,2:0.14,3:-0.04}
x = 3
c = 0

def normal(N,x,A):
    #to evaluate the value of p(x)
    B = A[N]
    for k in scipy.linspace(N-1,0,N):
        B = A[k] + (B * x)
        print("B(",k,") = ", B)

def derivative(N,x,A):
    #to evaluate the value of p'(x)
    D = N * A[N]
    for k in scipy.linspace(N-1,1,N-1):
        D = (k * A[k]) + (D * x)
        print("D(",k,") = ",D)

def integral(N,x,A,c):
    #to evaluate the definite integral I(x)
    I = (A[N])/ (N + 1)
    for k in scipy.linspace(N-1,0,N):
        I = (A[k] / (k + 1)) + (I * x)
        if k == 0:
            I = c + (I * x)
            print("I(0) = ",I)

    
normal(N,x,A)
derivative(N,x,A)
integral(N,x,A,c)
