import numpy as np
import sympy as sp

print('\t\t\t\t Welcome to Equation solver !!!!!')
print('This Module is to solve Linear Differential Equation in using Euler Method.\n')


x, y = sp.symbols('x y')
z = x/y

def D_f(p,q):
    return(z.subs([(x,p),(y,q)]))

X = [0.0]
Y1 = [0.0]

X[0] = float(input('Enter x0:'))
Y1[0] = float(input('Enter y0:'))
h = float(input('Enter h:'))
    
i = int(input('Enter the number of iteration to do:'))

X = X + [0.0]*i
X  = [X[0]+h*a for a in range(i+1)]
Y1 = Y1 + [0.0]*i

for i in range(1,i+1):
    Y1[i] = Y1[i-1] + h*(D_f(X[i-1],Y1[i-1]))
    print('x{} = {}, y{} = {}, f(x{},y{}) = {}'.format(i,X[i],i,Y1[i],i,i,D_f(X[i],Y1[i])))

Y2 = [0.0]*(len(Y1))
Y2[0] = Y1[0]
print(Y1)
for i in range(1,i+1):
    Y2[i] = Y2[i-1] + h*(D_f(X[i-1],Y2[i-1]) + D_f(X[i],Y1[i]))/2
    print('x{} = {}, y{} = {}, f_(x{},y{}) = {}'.format(i,X[i],i,Y2[i],i-1,i-1,D_f(X[i-1],Y2[i-1])))
