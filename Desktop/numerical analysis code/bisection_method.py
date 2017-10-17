import sys
import math
'''bisection method
        f is a function
        a and  b are the end points'''
def f(x):
       return math.exp(x)-2-x
       
def bisection(a,b):
       c = (a+b)/2.0
       iteration = 0
       while True:
              iteration+=1
              print('Iteration Number {0}: a = {1},  b = {2} , c= {3}'.format(iteration,a,b,c))
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
        
print(main(0.5, 2.5))     
