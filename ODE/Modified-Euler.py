import numpy as np

def midpoint_euler(f, initial, interval, h):
    """
    This function solves the differential equation using Ralstone's method and initial
    value condition.
      Arguments:
        f{function}: function form of the differential equation to be solved.
        initial{tuple}: tuple of the initial values (t0, y(t0))
        interval{tuple}: tuple of the interval in which the differential eq. to be solved
        h{float}: step size for each iteration
      Returns:
        A tuple of array of t's and corresponding y's
    """
    A = 0.5
    B1 = 0.0
    B2 = 1
    a, b = interval
    ts = np.arange(a, b+h, h)
    ys = np.zeros_like(ts)

    if initial[0] != interval[0]:
        print("The point for initial value doesn't match the start of interval")
        return None, None

    ys[0] = initial[1]

    for i in range(len(ts)-1):
        p_i = f(ys[i], ts[i])
        q_i = f(ys[i] + A*h*p_i, ts[i] + h*A)
        ys[i+1] = ys[i] + (B1*p_i + B2*q_i)*h

    return ts, ys


def heun(f, initial, interval, h):
    """
    This function solves the differential equation using Heun's method and initial
    value condition.
      Arguments:
        f{function}: function form of the differential equation to be solved.
        initial{tuple}: tuple of the initial values (t0, y(t0))
        interval{tuple}: tuple of the interval in which the differential eq. to be solved
        h{float}: step size for each iteration
      Returns:
        A tuple of array of t's and corresponding y's
    """
    A = 1
    B1 = 0.5
    B2 = 0.5
    a, b = interval
    ts = np.arange(a, b+h, h)
    ys = np.zeros_like(ts)

    if initial[0] != interval[0]:
        print("The point for initial value doesn't match the start of interval")
        return None, None

    ys[0] = initial[1]

    for i in range(len(ts)-1):
        p_i = f(ys[i], ts[i])
        q_i = f(ys[i] + A*h*p_i, ts[i] + h*A)
        ys[i+1] = ys[i] + (B1*p_i + B2*q_i)*h

    return ts, ys


def ralstone(f, initial, interval, h):
    """
    This function solves the differential equation using Ralstone's method and initial
    value condition.
      Arguments:
        f{function}: function form of the differential equation to be solved.
        initial{tuple}: tuple of the initial values (t0, y(t0))
        interval{tuple}: tuple of the interval in which the differential eq. to be solved
        h{float}: step size for each iteration
      Returns:
        A tuple of array of t's and corresponding y's
    """
    A = 2/3
    B1 = 0.25
    B2 = 0.75
    a, b = interval
    ts = np.arange(a, b+h, h)
    ys = np.zeros_like(ts)

    if initial[0] != interval[0]:
        print("The point for initial value doesn't match the start of interval")
        return None, None

    ys[0] = initial[1]

    for i in range(len(ts)-1):
        p_i = f(ys[i], ts[i])
        q_i = f(ys[i] + A*h*p_i, ts[i] + h*A)
        ys[i+1] = ys[i] + (B1*p_i + B2*q_i)*h

    return ts, ys