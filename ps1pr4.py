Sarah Larbi
slarbi@bu.edu

#Question 1

def ends_match(s):
    """ returns a boolean expression of True or False depending on if the first and last character of the string match.
    """
    if s[0] == s[-1]:
       return True
    if s[0] != s[-1]:
        return False
    
#Question 2

def front3(s):
    """ Returns the first 3 characters of a given string, unless there are less than 3 characters, in which case it print what is given.
    """
    if len(s) <= 3:
        return s * 3
    elif len(s) > 3:
        return s[0:3] * 3

#Question 3

def every_other(s):
    """ Returns a list containing every other value from the original list.
    """
    return s[0::2]

# Question 4

def begins_with(word, prefix):
    """ Returns true if 'word' begins with 'prefix,' and false if it doesn't
    """
    if word[0:len(prefix)] == prefix:
        return True
    elif word[0:len(prefix)] != prefix:
        return False
