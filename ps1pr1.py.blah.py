
# Question 1

def mult(n, m):
    """ returns the product of two given integers.
    """
    if n == 0:
        return 0
    if n == 1:
        return m
    elif n < 0:
        return -mult(-n, m)

    return m + mult(n-1, m)

# Question 2

def dot(l1, l2):
    """ returns the sum of the products of the elements in the same position of two lists.
    """
    if len(l1) != len(l2):
        return 0
    else:
        if l1 == [] and l2 == []:
            return 0
        else:
            rest = dot(l1[1:], l2[1:])
            return ((l1[0] * l2[0]) + rest)
        

# Question 3

def letter_score(letter):
    """ returns the value of a lowercase letter's scrabble tile.
    """
    
    if letter in ['a','e','i','l','n','o','r','s','t','u']:
        return 1
    elif letter in ['d','g']:
        return 2
    elif letter in ['b','c','m','p']:
        return 3
    elif letter in ['f','h','v','w','y']:
        return 4
    elif letter in ['k']:
        return 5
    elif letter in ['j','x']:
        return 8
    elif letter in ['q','z']:
        return 10
    else:
        return 0

# Question 4

def scrabble_score(word):
    """ returns the scrabble score of a given string-the sum of the the scores of its letters.
    """
    if word == '':
        return 0
    else:
        rest = scrabble_score(word[1:])
        if word[0] in ['a','e','i','l','n','o','r','s','t','u']:
            return 1 + rest
        elif word[0] in ['d','g']:
            return 2 + rest
        elif word[0] in ['b','c','m','p']:
            return 3 + rest
        elif word[0] in ['f','h','v','w','y']:
            return 4 + rest
        elif word[0] in ['k']:
            return 5 + rest
        elif word[0] in ['j','x']:
            return 8 + rest
        elif word[0] in ['q','z']:
            return 10 + rest
        else:
            return 0 + rest

