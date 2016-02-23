#
# ps3pr3.py (Problem Set 3, Problem 3)
#
# sorting
#
# name: Sarah Larbi 
# email: slarbi@bu.edu
#

# Question 1:

# My Approach: make a list of all the zeros and then a list of all the ones, and then concatenate them.
def binsort(list):
    """creates and returns a new list with the same elements as the original list, but sorted in ascending order.
    """
    lc = [ x for x in list if x < 1 ]
    lc2 = [ x for x in list if x > 0 ]
    return(lc + lc2)

# Question 2:

def insert_sorted(elem, list):
    """ I'm a helper function that
    takes a sorted list, and creates and returns a new sorted
          list containing the elements from the original list, along
          with elem in its appropriate place.
        inputs: elem is an an arbitrary value.
                list is a *sorted* list.
                elem should be of a type that allows it to be compared
                to the existing values in list.
    """
    if list == []:
        return [elem]
    elif elem < list[0]:
        return [elem] + list
    else:
        return [list[0]] + insert_sorted(elem, list[1:])


def gensort(list):
    """creates and returns a new list with the same elements as the original list, but sorted in ascending order.
    """
    if list == []:
        return list
    else:
        rest = gensort(list[1:])
        return insert_sorted(list[0], rest)
