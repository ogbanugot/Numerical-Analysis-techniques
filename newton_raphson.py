import scipy
from scipy.misc import derivative
import math

'''Newton-Raphson method
        f is a function
        {derivative(f, a, dx=1e-6)} the derivative of f at a
        a is the left end point xn'''

maxItr = 100
def f(x):
     return x**2 - 10*x +23 


def newtonRaph(a):
       iteration = 0
       a += 0.1
       while iteration<maxItr:
              x = a - f(a)/derivative(f, a, dx=1e-6)
              iteration+=1
              print("iteration number =",iteration)
              if f(x) == 0:
                      print("the zero is",x)
                      break
              else:
                  a = x
                          
       return x
       
def main(a):
        newtonRaph(a)

