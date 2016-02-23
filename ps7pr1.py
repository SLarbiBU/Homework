import random
import math

def throw_dart():

    
    y = random.uniform(-1.0, 1.0)
    x = random.uniform(-1.0, 1.0)
    if x**2 + y**2 <= 1:
            return True

    return False

def for_pi(n):

    throw_num = 0
    throw_hits = 0
    
    for x in range(n):
        
        throw_num += 1
        throw_hits += throw_dart()
        pi = 4* throw_hits / throw_num
        print(throw_hits , 'hits out of', throw_num , 'throws so that pi is' , pi)

    return pi

def for_pi_helper(n):

    throw_num = 0
    throw_hits = 0
    
    for x in range(n):
        
        throw_num += 1
        throw_hits += throw_dart()
        pi = 4* throw_hits / throw_num       
        
def while_pi(error):

    n = 1
    throw_num = 1
    throw_hits = 1
    pi = 4* throw_hits / throw_num
    
    if abs(pi - math.pi) > error:
            throw_num += 1
            throw_hits += throw_dart()
            pi = 4* throw_hits / throw_num
            n += 1
            print(throw_hits , 'hits out of', throw_num , 'throws so that pi is' , pi)
    

    

    return n




    return n



    
