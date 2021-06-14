from numpy import array as _array


def simpson13(f, limits, ns):
    """This function calculates the area under a given curve between the given
    list of limit points using Simpson 1/3 method

    Parameters
    ----------
    f : function
        function whose area is to be calculated
    limits : tuple
        a tuple of limit points
    ns : iterable
        list of number of sub intervals

    Returns
    -------
    Intergral : List
        List of area calculated using corresponding values of ns
    hs : List
        List of h for corresponding values of ns

    """
    a, b = limits
    hs = [(b - a) / k for k in ns]

    Intergral = []

    for i in range(len(ns)):
        coeffs = _array([1.0] * (ns[i] + 1))
        coeffs[1:-1:2] = 4.0
        coeffs[2:-1:2] = 2.0
        points = _array([f(a + k * hs[i]) for k in range(ns[i] + 1)])
        area = sum(coeffs * points) * hs[i] / 3
        Intergral.append(area)

    return Intergral, hs


def simpson38(f, limits, ns):
    """This function calculates the area under a given curve between the given
    list of limit points using Simpson 3/8 method

    Parameters
    ----------
    f : function
        function whose area is to be calculated
    limits : tuple
        a tuple of limit points
    ns : iterable
        list of number of sub intervals

    Returns
    -------
    Intergral : List
        List of area calculated using corresponding values of ns
    hs : List
        List of h for corresponding values of ns

    """
    a, b = limits
    hs = [(b - a) / k for k in ns]

    intergral = []

    for i in range(len(ns)):
        coeffs = _array([1.0] * (ns[i] + 1))
        coeffs[1:-1:3] = 3.0
        coeffs[2:-1:3] = 3.0
        coeffs[3:-1:3] = 2.0
        points = _array([f(a + k * hs[i]) for k in range(ns[i] + 1)])
        area = sum(coeffs * points) * hs[i] * 0.375
        intergral.append(area)

    return intergral, hs


def trapizoidal(f, limits, ns):
    """This function calculates the area under a given curve between the given
    list of limit points using Trapezoidal method

    Parameters
    ----------
    f : function
        function whose area is to be calculated
    limits : tuple
        a tuple of limit points
    ns : iterable
        list of number of sub intervals

    Returns
    -------
    Intergral : List
        List of area calculated using corresponding values of ns
    hs : List
        List of h for corresponding values of ns

    """
    a, b = limits
    hs = [(b - a) / k for k in ns]

    Intergral = []

    for i in range(len(ns)):
        coeffs = _array([2.0] * (ns[i] + 1))
        coeffs[0] = coeffs[-1] = 1.0
        points = _array([f(a + k * hs[i]) for k in range(ns[i] + 1)])
        area = sum(coeffs * points) * hs[i] * 0.5
        Intergral.append(area)

    return Intergral, hs
