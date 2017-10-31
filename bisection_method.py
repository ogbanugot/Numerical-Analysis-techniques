import sys
import math
'''bisection method
        f is a function
        a and  b are the end points'''
def f(x):
       return x**2- 10*x + 23 
       
def bisection(a,b):
       c = (a+b)/2.0
       iteration = 0
       while True:
              iteration+=1
              print("iteration number =",iteration)
              if f(c) == 0:
                      print("the zero is",c)
                      break
              elif f(a)*f(c) < 0:
                     b = c
              else :
                     a = c
              c = (a+b)/2.0
              
       return c
       
def main(x,y):
        bisection(x,y)     
