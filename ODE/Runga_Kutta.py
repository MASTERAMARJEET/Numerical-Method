import numpy as np


def rk3(f, initial, interval, h):
    """This function solves the differential equation using 3rd order Runga-Kutta
    method and initial value condition.

    Parameters
    ----------
    f : function
        function form of the differential equation to be solved
    initial : tuple
        tuple of the initial values
    interval : tuple
        tuple of the interval in which the differential eq
    h : float
        step size for each iteration

    Returns
    -------
    ts : 1d array
        array of t's
    ys : 1d array
        array of corresponding y's

    """
    a, b = interval
    ts = np.arange(a, b+h, h)
    ys = np.zeros_like(ts)

    if initial[0] != interval[0]:
        print("The point for initial value doesn't match the start of interval")
        return None, None

    ys[0] = initial[1]

    for i in range(len(ts)-1):
        p_i = f(ys[i], ts[i])
        q_i = f(ys[i] + 0.5*h*p_i, ts[i] + h*0.5)
        r_i = f(ys[i] - p_i*h + 2*q_i*h, ts[i] + h)
        ys[i+1] = ys[i] + (p_i + 4*q_i + r_i)*h/6

    return ts, ys


def rk4(f, initial, interval, h):
    """This function solves the differential equation using 4th order Runga-Kutta
    method and initial value condition.

    Parameters
    ----------
    f : function
        function form of the differential equation to be solved
    initial : tuple
        tuple of the initial values
    interval : tuple
        tuple of the interval in which the differential eq
    h : float
        step size for each iteration

    Returns
    -------
    ts : 1d array
        array of t's
    ys : 1d array
        array of corresponding y's

    """
    a, b = interval
    ts = np.arange(a, b+h, h)
    ys = np.zeros_like(ts)

    if initial[0] != interval[0]:
        print("The point for initial value doesn't match the start of interval")
        return None, None

    ys[0] = initial[1]

    for i in range(len(ts)-1):
        p_i = f(ys[i], ts[i])
        q_i = f(ys[i] + 0.5*h*p_i, ts[i] + h*0.5)
        r_i = f(ys[i] + 0.5*h*q_i, ts[i] + h*0.5)
        s_i = f(ys[i] + h*r_i, ts[i] + h)
        ys[i+1] = ys[i] + (p_i + 2*q_i + 2*r_i + s_i)*h/6

    return ts, ys
