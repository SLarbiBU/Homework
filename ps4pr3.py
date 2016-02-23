# Sarah Larbi
# slarbi@bu.edu

from ps4pr1 import *

def add(s1, s2):
    ''' takes 2 strings that represent binaru numbers and returns their sum'''

    sum_int =  bin_to_dec(s1) + bin_to_dec(s2)
    return dec_to_bin(sum_int)
