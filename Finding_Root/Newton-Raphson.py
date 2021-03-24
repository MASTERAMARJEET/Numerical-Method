from math import *
import numpy as np
import sympy as sp

print('\t\t\t\t Welcome to Equation solver !!!!!')
print('This Module is to solve polynomials in one variable using Newton-Raphson Method.\n')


x = sp.symbols('x')
y = 3*x - sp.cos(x) - 1

def f(p):
    return(y.subs(x,p))

def D_f(p):
    z = sp.diff(y,x)
    return(z.subs(x,p))

a = float(input('Enter a:'))

print('f(a) = {}, D_f(a) = {}'.format(f(a),D_f(a)))

if f(a) == 0:
    print('{} is the root of the equation:'.format(a))

i = int(input('Enter the number of iteration to do:'))
j = i
while i>0:
    c = a - f(a)/D_f(a)

    print('x{}  = {}, f(x{})  = {}, D_f(x{}) = {}'.format(j-i+1,float(c),j-i+1,float(f(c)),j-i+1,float(D_f(c))))

    if f(c) == 0:
        print('{} is the root of the equation:'.format(c))
        i = -1

    a = float(c)

    i -= 1