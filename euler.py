# Estimation using Euler's method
from sympy import *

x,y = symbols('x y')

def euler(func, x_initial, y_initial, step_size,*values):
    """This returns the euler approximation of simple 2D functions. 
    To use:, input the function as the first argument. 
        - Example of a correct functions: 
            2*x + 3*y
            x**4 + 3*x*y + 3*x
        - Example of incorrect functions: 
            3x + 2y
            3*t + 2*z (The function must only be in x and y)
    The second and third argument take in the initial x value and y value.
    In the third argument, input the step_size, commonly known as the 'h' value
    And in the remaining arguments, input all the values you want to approximate. 
    Example of use: 
    >>> euler(3- 2*x - 0.5*y,0,1, 0.1, 1,2,3,4,5)
    2.216419789901074
    1.3396830086889504
    -0.7903039312581901
    -3.6706580353463476
    -7.000284678597275
    
    You can import this function like so:
    >>> from euler import *
    """
    f = lambdify([x,y],func)
    for i in values: # Loop through the values list.

        # Initial values 
        t_point = x_initial 
        y_point = y_initial

        value_range = round(i / step_size)
        for k in range(value_range):
            y_point = y_point + f(t_point,y_point) * step_size
            t_point += step_size
        print(y_point)
