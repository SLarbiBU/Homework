# Sarah Larbi
#slarbi@bu.edu

# Question 1:
def dec_to_bin(n):
    ''' returns the binary form of a given decimal number.
    '''
    
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        rest = dec_to_bin(n//2)
        if n % 2 != 0:
            return rest + '1'
        else:
            return rest + '0'
        
# Question 2:


def bin_to_dec(n):
    ''' returns a decimal number that has been converted from binary.
    '''
    if n == '1':
        return 1
    if n == '0':
        return 0
    else:
        rest = bin_to_dec(n[0:-1])
        if n[-1] == '1':
            return 2 * rest + 1
        if n[-1] == '0':
            return 2 * rest + 0
        
# Question 3:

def increment(s):
    ''' takes an 8-character str representation of a binary #, and returns the next largest binary # as an 8 charc. str.
    '''
    if s == '11111111':
        return '00000000'
    else:
        n = bin_to_dec(s)
        b = n + 1
        short = dec_to_bin(b)
        remainder = 8 - len(short)
        return '0' * remainder + short
