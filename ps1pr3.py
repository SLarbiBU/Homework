Sarah Larbi
slarbi@bu.edu

#Answer 0:
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# Answer 1:
def square(x):
    """ returns the sqaure of its input
        input x: any number (int or float)
    """
    power = 2
    return x**power



# Answer 2:
def interpolate(low, high, fraction):
    """ returns a number that linearly interpolates between low and high by the given fraction.
        input low, high, fraction: any number (int or float)
    """ 
    return ((high - low)*fraction) + low

# Answer 3:
def convert_from_inches(inches):
    """ returns a list of 3 integers broken up from the original inches into yards feet and inches
        input inches: any number (int or float)
    """
    yards = inches//36                    # number of yards
    inches = inches % 36                   # the leftover number of inches
    feet = inches//12                    # number of feet
    inches = inches % 12                   # final number of inches
    return [yards, feet, inches]

# Answer 4:
def median(a, b, c):
    """ returns median of the 3 values when put in increasing order
        input a, b, c: any number (int or float)
    """
    if a <= b <= c:
        return b
    elif c <= b <= a:
        return b
    elif b <= a <= c:
        return a
    elif c <= a <= b:
        return a
    elif b <= c <= a:
        return c
    elif a <= c <= b:
        return c
  
    
