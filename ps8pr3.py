#
# ps8pr3.py (Problem Set 8, Problem 3)
#
# Matrix operations
#
# Computer Science 111
#
# name:Sarah Larbi
# email:slarbi@bu.edu
# 

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Enter a new matrix')
    print('(1) Negate the matrix')
    print('(2) Multiply a row by a constant')
    print('(3) Add one row to another')
    print('(4) Add a multiple of one row to another')
    print('(5) Transpose the matrix')
    print('(6) Quit')
    print()


def print_matrix(matrix):
    """ prints the specified matrix in rectangular form.
        input: matrix is a 2-D list numbers
    """
    height = len(matrix)
    width = len(matrix[0])
    for r in range(height):
        for c in range(width):
            print('%7.2f' % matrix[r][c], end=' ')

        print()
            
def get_matrix():
    """ gets a new matrix from the user and returns it
    """
    matrix = eval(input('Enter a new 2-D list of numbers: '))
    return matrix

def negate_matrix(matrix):
    """ negates all of the elements in the specified matrix
        inputs: matrix is a rectangular 2-D list of numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] *= -1
    # We don't need to return the matrix!
    # All changes to the matrix will still be there when the
    # function returns, because we received a copy of the
    # *reference* to the matrix used by main().

def mult_row(matrix, r, m):
    
    for c in range(len(matrix[r])):
        matrix[r][c] *= m

def add_row_into(matrix, rs, rd):
    ''' takes a specified 2-D matrix and adds each element of row rs (the source row) to the corresponding element of row rd(the destination row).
    '''
    for c in range(len(matrix[rs])):
        matrix[rd][c] += matrix[rs][c]
        
def add_mult_row_into(matrix, m, rs, rd):
    '''takes the specified 2-D list matrix and adds each element of row rs (the source row), multiplied by m, to the corresponding element of row rd (the destination row).
    '''

    for c in range(len(matrix[rd])):
        matrix[rd][c] += m*(matrix[rs][c])

def create_row(width):
    """ creates and returns a "row" with the specified width --
        i.e., a list containing width zeros.
        input: width is a non-negative integer
    """
    row = []
    
    for col_num in range(width):
        row += [0]    # add one 0 to the end of the row

    return row


def create_matrix(height, width):
    """ creates and returns a 2-D list of height rows and width columns in which all of the cells
    """
    matrix = []

    for row_num in range(height):
        matrix += [create_row(width)]    # add a whole row

    return matrix

def transpose(matrix):
    """takes the specified 2-D list matrix and creates and returns a new 2-D list that is the transpose of matrix"""
    height = len(matrix[0])
    width = len(matrix)
    new_matrix = create_matrix(height, width)

    for r in range(len(new_matrix)):
        for c in range(len(new_matrix[0])):
            new_matrix[r][c] = matrix[c][r]

    return new_matrix
    

### Add your functions for options 2-5 here. ###

def main():
    """ the main user-interaction loop
    """
    ## The default starting matrix.
    ## DO NOT CHANGE THESE LINES.
    matrix = [[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]]

    while True:
        print()
        print_matrix(matrix)
        display_menu()
        choice = int(input('Enter your choice: '))

        if choice == 0:
            matrix = get_matrix()
        elif choice == 1:
            negate_matrix(matrix)
        elif choice == 2:
            r = int(input('Index of row: '))
            m = float(input('Multiplier: '))
            mult_row(matrix, r, m)
        elif choice == 3:
            rs = int(input('Index of source row: '))
            rd = int(input('Index of destination row:'))
            add_row_into(matrix, rs, rd)
        elif choice == 4:
            rs = int(input('Index of source row: '))
            rd = int(input('Index of destination row:'))
            m = float(input('Multiplier: '))
            add_mult_row_into(matrix, m, rs, rd)
        elif choice == 5:
            matrix = transpose(matrix)
        elif choice == 6:
            break
        else:
            print('Invalid choice. Try again.')
