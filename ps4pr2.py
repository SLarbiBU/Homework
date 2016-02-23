# Sarah Larbi
#slarbi@bu.edu

# Question 1:

def dec_to_base(n, b):
    ''' returns a decimal number n converted to base b.
    '''
    
    if n < b:
        return str(n)
    else:
        rest = dec_to_base(n//b, b)
        if n % b != 0:
            remainder = n % b
            return rest + str(remainder)
        else:
            return str(n)

# Question 2:

def base_to_dec(s, b):
    ''' takes as inputs a string s and an integer b, where s represents a number in base b. The function should convert s to decimal and return the resulting integer.
    '''
    if int(s) < b:
        return s
    else:
        rest = base_to_dec(s[0:-1], b)
        if s[-1] == '1':
            return b * int(rest) + 1
        if s[-1] == '0':
            return b * int(rest) + 0

