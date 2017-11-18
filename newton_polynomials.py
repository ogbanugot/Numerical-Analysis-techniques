'''Newton polynomial approximation;
    Find P1(x), P2(x), P3(x),P4(x) Given;
    Centers ---> x = 0.....n
    Coefficents----> a = 0....n
    ind = independent variable, P(ind)'''
#Lets use a list to hold our centers and coefficients, index = 0...n
xData = [1,3,4,4.5]
a = [5,-2,0.5,-0.1,0.003]
x = 2.5

## module newtonPoly
'''
p = evalPoly(a,xData,x).
Evaluates Newton’s polynomial p at x. The coefficient
vector {a} can be computed by the function ’coeffts’.
a = coeffts(xData,yData).
Computes the coefficients of Newton’s polynomial.
'''
def evalPoly(a,xData,x):
    n = len(xData) - 1 # Degree of polynomial
    p = a[n]
    for k in range(1,n+1):
        p = a[n-k] + (x -xData[n-k])*p
    return p

def coeffts(xData,yData):
    m = len(xData) # Number of data points
    a = yData.copy()
    for k in range(1,m):
        a[k:m] = (a[k:m] - a[k-1])/(xData[k:m] - xData[k-1])
    return a

print(evalPoly(a,xData,x))
