#
# ps2pr4.py - Problem Set 2, Problem 4
#
# List comprehensions
#
# name: Sarah Larbi
# email: slarbi@bu.edu
#

#

# Problem 4-1: LC puzzles!


# part a
lc1 = [ x + 5 for x in range(5)]
print(lc1)

           
# part b
lc2 = [  word + 'ing' for word in ['go', 'eat', 'read']]
print(lc2)

# part c
words = ['hello', 'world', 'how', 'goes', 'it?']
lc3 = [ w[-1] for w in words]
print(lc3)

# part d
lc4 = [ c == 'a'   for c in 'aardvark']
print(lc4)

# part e
lc5 = [ x   for x in range(1, 21) if x % 5 == 0 ]
print(lc5)


# Problem 4-2: Put your definition of the powers_of() function below.

def powers_of(n, count):
    """ returns a list containing the first count powers of n, beginning with the 0th power.
    """
    lc = [ n ** x for x in range(count)]
    print(lc)


# Problem 4-3: Put your definition of the starts_with() function below.

def starts_with(prefix, wordlist):
    lc = [word for word in wordlist if word[0:len(prefix)] == prefix]
    print(lc)   

