def newton(func, dfunc, initial, tol, maxiter=100):
    """
    This function finds the roots of the given function using newton method

    Arguments:
        func: function name whose root is to be found.
        dfunc: derivative of the function 
        initial: starting point for finding the root
        tol: tolerance limit within which the root is to be found.
        maxiter [optional, default:100]: maximum number of the iterations allowed.
    
    Returns a tuple of (root, iterations)
    """

    x0 = initial
    x = x0 - (func(x0))/dfunc(x0)
    i = 1

    if func(x0)==0:
        print('The initial point is a solution of the function.')
        return x0, 0

    while(abs(func(x))>tol and i<maxiter):
        x0 = x
        x = x0 - (func(x0))/dfunc(x0)
        i+=1

    if i>=maxiter:
        print('Max iteration count reached!, Try with a higher iteration limit.')
        return None, i-1

    return x, i-1