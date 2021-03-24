import numpy as np


def euler(f, initial, interval, h):
    """
    This function solves the differential equation using Euler's method and initial
    value condition.
      Arguments:
        f{function}: function form of the differential equation to be solved.
        initial{tuple}: tuple of the initial values (t0, y(t0))
        interval{tuple}: tuple of the interval in which the differential eq. to be solved
        h{float}: step size for each iteration
      Returns:
        A tuple of array of t's and corresponding y's
    """
    a, b = interval
    ts = np.arange(a, b+h, h)
    ys = np.zeros_like(ts)

    if initial[0] != interval[0]:
        print("The point for initial value doesn't match the start of interval")
        return None, None

    ys[0] = initial[1]

    for i in range(len(ts)-1):
        ys[i+1] = ys[i] + f(ys[i], ts[i])*h

    return ts, ys