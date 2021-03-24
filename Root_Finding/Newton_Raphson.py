def newton(func, dfunc, initial, tol, maxiter=100):
    """This function finds the roots of the given function using Newton-Raphson method

    Parameters
    ----------
    func : function
        function name whose root is to be found
    dfunc : function
        derivative of the function
    initial : tuple
        starting point(two tuple) for finding the root
    tol : float
        tolerance limit within which the root is to be found
    maxiter : int, optional
        maximum number of the iterations allowed. Default is 100

    Returns
    -------
    root : float
        computed root of the function
    iteration : int
        number of iterations used to arrive at the `root`

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