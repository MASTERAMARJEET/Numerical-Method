# from math import exp
import numpy as np
import sympy as sp

print('\t\t\t\t Welcome to Equation solver !!!!!')
print('This Module is to solve Linear Differential Equation in using Euler Method.\n')


x, y = sp.symbols('x y')
z = x/y

def D_f(p,q):
    return(z.subs([(x,p),(y,q)]))


a = float(input('Enter x0:'))
b = float(input('Enter y0:'))
h = float(input('Enter h:'))
    
i = int(input('Enter the number of iteration to do:'))
j = i
while i>0:
    c = b + h*D_f(a,b)

    print('x{} = {}, y{} = {}, f(x{},y{}) = {}'.format(j-i,a,j-i,b,j-i,j-i,D_f(a,b)))

    a,b = float(a+h), float(c)
    i -= 1