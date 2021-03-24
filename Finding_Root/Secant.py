# from math import exp
import numpy as np
import sympy as sp

print('\t\t\t\t Welcome to Equation solver !!!!!')
print('This Module is to solve polynomials in one variable using Secant Method.\n')


x = sp.symbols('x')
y = x**3 - x -1

def f(p):
    return(y.subs(x,p))


a = float(input('Enter a:'))
b = float(input('Enter b:'))
k = 0
if a>b:
    a,b = b,a
print('f({}) = {} , f({}) = {}'.format(a,f(a),b,f(b)))
if f(a) == 0:
    print('{} is the root of the equation:'.format(a))
elif  f(b) == 0:
    print('{} is the root of the equation:'.format(b))
    
i = int(input('Enter the number of iteration to do:'))
j = i
while i>0:
    c = b - f(b)*((b-a)/(f(b)-f(a)))

    print('x{} = {}, f(x{}) = {}'.format(j-i+1,float(c),j-i+1,float(f(c))))

    if f(c) == 0:
        print('{} is the root of the equation:'.format(c))
        i = -1
    else:
        a,b = float(b), float(c)
    i -= 1