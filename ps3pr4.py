#
# ps3pr4.py (Problem Set 3, Problem 3)
#
# sorting
#
# name: Sarah Larbi
# email:slarbi@bu.edu

# Partners Name: Sheryn Chung
# Partner's Email: sherync@bu.edu

# Question 1

def rem_first(elem, s):
    """ returns a version of list in which *only the first* occurrence
        of elem (if any) has been removed.
        inputs: elem is an arbitrary value
                list is an arbitrary list
    """
    if s == '':
        return ''
    elif s[0] == elem:
        return s[1:]
    else:
        rest = rem_first(elem, s[1:])
        return s[0] + rest

# Question 2
# We first checked to see if the first lettter in the first list was in the second list. if it was, we assigned it a score of 1 and created a recursive function that then looked at the next letter in the first list, and all of the letters in the second list that occured after we the first letter we found.
# If the first letter was not in the second list than we did the same thing except we didn't assign the first position a score of 1.
def jscore(s1, s2):
    """ returns the Jotto score of s1 compared with s2.
    """
    if s1 == '' or s2 == '':
        return 0
    if s1[0] in s2:
        rest_s2 = rem_first(s1[0:], s2)
        return 1 + jscore(s1[1:], rest_s2)
    if s1[0] not in s2:
        rest_s2 = rem_first(s1[0:], s2)
        return jscore(s1[1:], rest_s2)
        
    
    
# Question 3


def lcs(s1, s2):
    """ returns the longest common subsequence that they share.
    """
    if s1 =='' or s2 =='':
        return ''

    if s1[0] == s2[0]:
        return s1[0] + lcs(s1[1:], s2[1:])
    else:
        results1 = lcs(s1, s2[1:])
        results2 = lcs(s1[1:], s2)
        return max([len(results1), results1], [len(results2), results2])[1]
