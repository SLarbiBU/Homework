# 
# ps1pr2.py - Problem Set 1, Problem 1
#
# Indexing and slicing puzzles
#
# name: Sarah Larbi
# email: slarbi@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:n/a
# partner's email: n/a
#

#
# List puzzles
#

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example puzzle (puzzle 0):
# Creating the list [2, 5, 9] from pi and e
answer0 = [e[0]] + pi[-2:]     
print(answer0)


# Puzzle 1:
# creating the list[7, 1] from pi and e
answer1 = [e[1] , e[2]]
print(answer1)

# Puzzle 2
# Creating the list [9,1,1] from pi and e
answer2 = pi[-1:0:-2]
print(answer2)

# Puzzle 3:
# Creating the list [1,4,1,5,9] from pi and e
answer3 = pi[1:]
print(answer3)

# Puzzle 4:
# Creating the list [1,2,3,4,5] from pi and e
answer4 = e[-1::-2] + pi[0::2]
print(answer4)

#
# String puzzles
#

b = 'boston'
u = 'university'
t = 'terriers'

# Puzzle 5
# Creating the string 'bossy'
answer5 = b[:3] + t[-1] + u[-1]
print(answer5)

# Puzzle 6:
# Creating the string 'stone'
answer6 = b[2:] + t[1]
print(answer6)

# Puzzle 7:
# Creating the string 'street'
answer7 = b[2:4] + t[2] + 2*t[1] + t[0]
print(answer7)

# Puzzle 8:
# Creating the string 'nonononono'
answer8 = 5*b[-1:-3:-1]
print(answer8)

# Puzzle 9:
# Creating string 'bestever'
answer9 = b[0] + u[4::2] + t[1] + u[3:6]
print(answer9)

# Puzzle 10:
# Creating string 'serenity'
answer10 = t[-1::-2] + b[-1] + u[-3::1]
print(answer10)



