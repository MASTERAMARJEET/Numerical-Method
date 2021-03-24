def secant(func, interval, tol, maxiter=100):
    """
    This function finds the roots of the given function using secant method

    Arguments:
        func: function name whose root is to be found.
        interval: a tuple of the starting end-points.
        tol: tolerance limit within which the root is to be found.
        maxiter [optional, default:100]: maximum number of the iterations allowed.
    
    Returns a tuple of (root, iterations)
    """

    x0, x1 = interval
    x = x1 - func(x1)*(x1 - x0)/(func(x1) - func(x0))
    i = 1

    if func(x0)==0:
        print(f'One of the initial point,{x0} is a solution of the function.')
        return x0, 0
    elif func(x1)==0:
        print(f'One of the initial point,{x1} is a solution of the function.')
        return x1, 0

    while(abs(func(x))>tol and i<maxiter):
        x0 = x1
        x1 = x
        x = x1 - func(x1)*(x1 - x0)/(func(x1) - func(x0))
        i+=1

    if i>=maxiter:
        print('Max iteration count reached!, Try with a higher iteration limit.')
        return None, i-1

    return x, i-1