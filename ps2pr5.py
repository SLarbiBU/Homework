# Sarah Larbi
# slarbi@bu.edu

# Question 1

def add_spaces(s):
    """ returns a string formed by adding spaces between each pair of adjacent characters in the input string.
    """
    if len(s) < 2:
        return s[0]
    else:
        rest = ((' ') + add_spaces(s[1:]))
        return (s[0] + rest)

# Question 2



def num_diff(s1, s2):
    """"takes two input strings and returns the number of differences between them.
    """
    if s1 == s2:
        return 0
    else:
        rest = num_diff(s1[1:], s2[1:])
        if s1[0] != s2[0]:
            return (1 + rest)
        else:
            return num_diff(s1[0], s2[0])  + rest

# Question 3

def index(elem, seq):
    """ takes input elem and seq and returns the index of the first occurance of elem in seq.
        seq can be a lst or a str.
    """
    if seq == []:
        return 0
    if seq == (''):
        return 0
    else:
        rest = index(elem, seq[1:])
        if seq[0] == elem:
            return 0
        else:
            return 1 + rest

# Question 4

def one_dna_to_rna(c):
    """ takes a single character string c representing a DNA nucleotide and returns the corresponding messenger-RNA nucleotide.
    """
    
    if c == 'A':
        return 'U'
    if c == 'C':
        return 'G'
    if c == 'G':
        return 'C'
    if c == 'T':
        return 'A'
    elif c != ('A','C','G','T'):
        return ''

# Question 5

def transcribe(s):
    """takes as input a string s representing a piece of DNA, and returns a string representing the corresponding RNA.
    """
    if s == (''):
        return ('')
    else: 
        rest = transcribe(s[1:])
        if s[0] == 'A':
            return 'U' + rest
        if s[0] == 'C':
            return 'G' + rest
        if s[0] == 'G':
            return 'C' + rest
        if s[0] == 'T':
            return 'A' + rest
        if s[0] != ('A','C','G','T'):
            return '' + rest

        
        
       



   
    
    
  
