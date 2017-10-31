import sys
import math
'''false position method
        f is a function
        a and  b are the end points'''
maxItr = 100
def f(x):
       return x**2 - 10*x + 23
       
def regFalsi(a,b):
       iteration = 0
       while iteration<maxItr:
              x = a - f(a)*((b-a)/(f(b) - f(a)))
              iteration+=1
              print("iteration number =",iteration)
              if f(x) == 0:
                      print("the zero is",x)
                      break
              else:
                  a = x
                          
       return x
       
def main(x,y):
        regFalsi(x,y)
        
