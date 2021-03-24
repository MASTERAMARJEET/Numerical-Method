# from math import exp
import numpy as np
import sympy as sp

print('\t\t\t\t Welcome to Equation solver !!!!!')
print('This Module is to solve polynomials in one variable using Regula Falsi Method.\n')


x = sp.symbols('x')
y = x**2 - 3

def f(p):
    return(y.subs(x,p))

k=1 
while k == 1:
    a = float(input('Enter a:'))
    b = float(input('Enter b:'))
    k = 0
    if a>b:
        a,b = b,a
    print('f(a) = {} , f(b) = {}'.format(f(a),f(b)))
    if f(a) == 0:
        print('{} is the root of the equation:'.format(a))
    elif  f(b) == 0:
        print('{} is the root of the equation:'.format(b))
    elif f(a)*f(b)>0: 
        k = 1
        print('Sorry! The given pair of point do not satisfy the required conditions.\n Please try some other numbers.')

i = int(input('Enter the number of iteration to do:'))
j = i
while i>0:
    c = a - f(a)*((b-a)/(f(b)-f(a)))

    print('x{} = {}, f(x{}) = {}'.format(j-i+1,float(c),j-i+1,float(f(c))))

    if f(c) == 0:
        print('{} is the root of the equation:'.format(c))
        i = -1
    elif  f(a)*f(c) < 0:
        b = float(c)
    elif  f(b)*f(c) < 0:
        a = float(c)

    i -= 1