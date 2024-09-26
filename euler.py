# Estimation using Euler's method
from sympy import *
x,y = symbols('x y') # The variables here are arbitrary. 

def euler(func, step_size,*values):
    """This returns the euler approximation of simple 2D functions. 
    To use:, input the function as the first argument. 
        - Example of a correct function: 2*x + 3*y
        - Example of an incorrect function: 2x + 3y. 
    In the second argument input the step_size, commonly known as the 'h' value
    And in the remaining arguments, input all the values you want to approximate (can be 1,2,3 to n values). 
    Example of use: 
    >>> euler(3- 2*x - 0.5*x, 0.1, 1,2,3,4,5)
    2.216419789901074
    1.3396830086889504
    -0.7903039312581901
    -3.6706580353463476
    -7.000284678597275
    
    IMPORTANT: Make sure to 
    >>> import sympy 
    
    AND to define your symbols using
    >>> a,b = symbols('a b')
    """
    f = lambdify([x,y],func)
    for i in values: # Loop through the values list.

        # Initial values 
        t_point = 0 
        y_point = 1 

        value_range = int(i / step_size)
        for i in range(value_range):
            y_point = y_point + f(t_point,y_point) * step_size
            t_point += step_size
        print(y_point)

# Call the function here:
euler(3 - 2*x - 0.5*y,0.05,1,2,3,4,5) 
