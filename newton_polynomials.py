'''Newton polynomial approximation;
    Find P1(x), P2(x), P3(x),P4(x) Given;
    Centers ---> x = 0.....n
    Coefficents----> a = 0....n
    ind = independent variable, P(ind)'''
#Lets use a list to hold our centers and coefficients, index = 0...n
x = [1,3,4,4.5]
a = [5,-2,0.5,-0.1,0.003]
ind = 2.5

def P1(x,a,ind):
    P1x = a[0] + (a[1] * (ind - x[0 ]))
    return P1x

def P2(x,a,ind):
    P2x = P1(x,a,ind) + (a[2] *((ind - x[0])*(ind-x[1])))
    return P2x

def P3(x,a,ind):
    P3x = P2(x,a,ind) + (a[3] *(ind - x[0])*(ind-x[1])*(ind-x[2]))
    return P3x

def P4(x,a,ind):
    P4x = P3(x,a,ind) + (a[4] *(ind - x[0])*(ind-x[1])*(ind-x[2])*(ind-x[3]))
    return P4x


print("P1(x) = ",P1(x,a,ind))
print("P2(x) = ",P2(x,a,ind))
print("P3(x) = ",P3(x,a,ind))
print("P4(x) = ",P4(x,a,ind))
