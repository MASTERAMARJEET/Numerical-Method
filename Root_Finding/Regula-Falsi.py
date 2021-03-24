def regula_falsi(func, interval, tol, maxiter=100, sol=None):
    """
    This function finds the roots of the given function using regula_falsi 
    method

    Arguments:
        func: function name whose root is to be found.
        interval: a tuple of endpoints.
        tol: tolerance limit within which the root is to be found.
        maxiter [optional, default:100]: maximum number of the iterations allowed.
        sol [optional, default:None]: value of the actual solution in the interval.
    
    Returns a tuple of (root, iterations)
    """

    a,b = interval
    c = (a*func(b) - b*func(a))/(func(b)-func(a))
    i = 1

    if sol!=None:
        if sol<a or sol>b:
            print("\nWARNING! The entered solution doesn't lie in the interval.\n")
    if func(a)*func(b)>0:
        msg=('The value of the function at both the end points is of the same sign.\n'
             'Either there is no root in the interval or there are even number of roots.\n'
             'Press 1 to continue search, any other key to quit searching: ')
        key = int(input(msg))
        if key != 1:
            return None, 0
    elif func(a)==0:
        print(f'One of the endpoints, {a} is a root of the function.')
        return a, 0
    elif func(b)==0:
        print(f'One of the endpoints, {b} is a root of the function.')
        return b, 0

    while(abs(func(c))>tol and i<maxiter):
        if func(b)*func(c)<0:
            a = c
            c = (a*func(b) - b*func(a))/(func(b)-func(a))
        elif func(a)*func(c)<0:
            b = c
            c = (a*func(b) - b*func(a))/(func(b)-func(a))
        i+=1

    if i>=maxiter:
        print('Max iteration count reached!, Try with a higher iteration limit.')
        return None, i-1

    return c, i-1