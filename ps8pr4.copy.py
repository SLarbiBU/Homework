#
# ps8pr4.py (Problem Set 8, Problem 4)
#
# Images as lists
#
# Computer Science 111
# 
# name:
# email:
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#


# Mystery.png looks like the red.png except all the pixels are yellow.
# This makes sense because the red component and the green component are both at the max 255, and red and green together make yellow!



from hmcpng import *

def create_pixel_row(width, pixel):
    """ creates and returns a "row" of pixels with the specified width
        in which all of the pixels have the RGB values specified by pixel.
        input: width is a non-negative integer
               pixel is a list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    row = []
    
    for col_num in range(width):
        row += [pixel]

    return row
#1.
def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and width columns in which all of the pixels have the RGB values given by pixel."""
    column = []
    for row_num in range(height):
        column += [create_pixel_row(width, pixel)]

    return column


#3.
def blank_image(height, width):
    """creates and returns a 2-D list of pixels with height rows and width columns in which all of the pixels are green (i.e., have RGB values [0,255,0])."""
    pixel = [0, 255, 0]
    
    blank = create_uniform_image(height, width, pixel)

    return blank


#4.
def flip_horiz(pixels):
    '''takes the 2-D list pixels containing pixels for an image, and that creates and returns a new 2-D list of pixels for an image in which the original image is “flipped” horizontally.'''

    height = len(pixels)
    width = len(pixels[0])
    new_pixels = blank_image(height,width)

    for r in range(height):
        for c in range(width):

            new_pixels[r][c] = pixels[r][((width-1)-c)]

    return new_pixels

#5.
def transpose(pixels):
    """takes the specified 2-D list matrix and creates and returns a new 2-D list that is the transpose of matrix"""
    height = len(pixels[0])
    width = len(pixels)
    new_pixels = blank_image(height, width)

    for r in range(len(new_pixels)):
        for c in range(len(new_pixels[0])):
            new_pixels[r][c] = pixels[c][r]

    return new_pixels

    
   
