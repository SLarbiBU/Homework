Sarah Larbi
slarbi@bu.edu

# Question 1:

def reverse(s):
    """ Returns a string in which the characters of s have been reversed.
    """
    return s[-1::-1]

# Question 2:

def outer_vals(lst):
    """ returns a list that contains onlt the first and last elements of a list.
    """
    return lst[0] , lst[-1]

# Question 3:

def flipside(s):
    """returns a string whose first hald is s's second half, and vice versa.
    """
    halfpoint = len(s)//2 
    return s[halfpoint::1] + s[0:(halfpoint):1]
    
# Question 4:

def adjust(s, length):
    """ returns a string in which the value of s has been adjusted to produce a string with the spelled length.
    """
    if len(s) < length:
        return ((' ') * (length % len(s))) + s
    return s[0:length]


