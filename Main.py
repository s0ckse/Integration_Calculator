from sympy import *
from numpy import *
import numpy as np
import sympy as sym
from numpy import sin, cos, tan, cosh, tanh, sinh,log
import numpy.polynomial.legendre as leg
import math
import re

#passes the function first checks for the limits and then calculates the integral
def Guass_Quad(func,n,zeroes,weights,a,b,flag):
    intgrl=0
    
    if(a!=-1 or b!=1):
        func = "("+func+")*((b-a)/2)"
        
    for i in range(n):
        z=zeroes[i]
        if(a!=-1 or b!=1): 
            x=a+(((b-a)*(z+1))/2)
        else:
            x=z
        if(flag==1):
            x=np.tan(z)
        code = compile(func, "<string>", "eval")
        fx = eval(code)
        
        intgrl = intgrl + (weights[i]*fx) #THE INTEGRAL CALCULATION USING GAUSSIAN-QUADRATURE
    return intgrl

#inputs for zeros and weights
def Guass_basis(n):
    return leg.leggauss(n)

#function to convert input into float or constants
def my_float(s):
    constants = {"pi": np.pi, "e": np.e,"-pi":-np.pi,"-e":-np.e,"inf":inf,"-inf":-inf,"pi/2":np.pi/2,"-pi/2":np.pi/2}
    if s in constants:
        return constants[s]
    elif(re.search('[a-zA-Z]', s)!=None):
        code = compile(s, "<string>", "eval")
        fx = eval(code)
        return fx
    else:
        return float(s)

#Function to check for infinity and adjust the limits
def Inf_checkpoint(a,b,func):
    flag=0
    if(a==inf or a==-inf or b==inf or b==-inf):
        a=math.atan(a)
        b=math.atan(b)
        func="("+func+")*(sec(x)**2)"
        flag=1
    return a,b,func,flag    
    
# Driver Program
# Taking the Iput from the user
n = int(input("Enter order of Guassian Quadrature to be used:"))
print("\nEnter the Limits in form of numbers , pi, e or inf")
inp_a= input("\nEnter the Lower limit:")
inp_b= input("\nEnter the Upper limit:")
#Passing it to function to convert string to Floating points
a=my_float(inp_a)
b=my_float(inp_b)

#input the function
func= input("\nEnter a Polynomial function: (for example: 2*x**3 + x*2 + I = 2x^3+i or sin(x),cos(x)**2) : ")

#Checking the limits for Infinity
a,b,func,flag=Inf_checkpoint(a,b,func)

#Calculation of the Weights and Zeroes using pre-defined Function
arr= Guass_basis(n)
zeroes = arr[0]
weights = arr[1]  
#Passing the integral into the function to calculate the integral
intgrl = Guass_Quad(func,n,zeroes,weights,a,b,flag)
print('\nThe Integral is : ' , round(intgrl,5))

 

# Method to Calculate the Weights and the Xi for the Guass Quadrature Formula in comments Manually
# which adds to error so not implemented in the program
'''
# Recursive generation of the Legendre polynomial of order n
def Legendre(n,x):
    x=array(x)
    if (n==0):
        return x*0+1.0
    elif (n==1):
        return x
    else:
        return ((2.0*n-1.0)*x*Legendre(n-1,x)-(n-1)*Legendre(n-2,x))/n

# Derivative of the Legendre polynomials
def DL(n,x):
    return sym.diff(x)

def Roots(order,tolerance=1e-20):
    if order<2:
        er=1 # bad order no roots can be found
    else:
        roots=[]
        # The polynomials are alternately even and odd functions. So we evaluate only half the number of roots. 
        for i in range(1,int(order/2) +1):
            x=cos(pi*(i-0.25)/(order+0.5))
            error=10*tolerance
            i=0
            while (error>tolerance) and (i<1000):
                    dx=-Legendre(order,x)/DL(order,x)
                    x=x+dx
                    i=i+1
                    error=abs(dx)
            roots.append(x)
        # Use symmetry to get the other roots
        roots=array(roots)
        if order%2==0:
            roots=concatenate( (-1.0*roots, roots[::-1]) )
        else:
            roots=concatenate( (-1.0*roots, [0.0], roots[::-1]) )
        er=0 # successfully determined roots
    return [roots, er]

# Weight coefficients
def Weights(order):
    W=[]
    [x,er]= Roots(order)
    if er==0:
        W=2.0/( (1.0-xis*2)*(DL(order,x)**2) )
        er=0
    else:
        er=1 # could not determine roots - so no weights
    return [W, x, er]
    '''
