#
# ps7pr2.py (Problem Set 7, Problem 2)
#
# Image processing with loops, part I
#
# Computer Science 111
#
# name: Sarah Larbi 
# email:slarbi@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name: Sheryn Chung  
# partner's email:sherync@bu.edu
# 

# IMPORTANT: This file is for your solutions to problem 2.
# Your solutions to problem 3 should go in ps7pr3.py instead.

from cs111png import *

def invert(filename):
    """ loads a PNG image from the file with the specified filename
        and creates a new image in which the colors of the pixels are
        inverted.
        input: filename is a string specifying the name of the PNG file
               that the function should process.
        No value is returned, but the new image is stored in a file
        whose name is invert_filename, where filename is the name of
        the original file.
    """
    img = load_image(filename)

    for r in range(img.get_height()):
        for c in range(img.get_width()):
            # get the colors of the current pixel at row r, column c
            pixel = img.get_pixel(r, c)            
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            # change the pixel to one in which the colors are inverted
            new_pixel = [255 - red, 255 - green, 255 - blue]
            img.set_pixel(r, c, new_pixel)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'invert_' + filename
    img.save(new_filename)

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

### PUT YOUR WORK FOR PROBLEM 2 BELOW. ###
def grayscale(filename):
    
    ''' loads the PNG image file with the specified filename, creates a new image that is a grayscale version of the original image, and stores it
    '''
    img = load_image(filename)

    for r in range(img.get_height()):
        for c in range(img.get_width()):
            pixel = img.get_pixel(r, c)
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            new_pixel = [brightness(pixel),brightness(pixel),brightness(pixel) ]
            img.set_pixel(r,c,new_pixel)
    new_filename = 'grayscale_' + filename
    img.save(new_filename)


def flip_vert(filename):
    
    ''' loads the PNG image file with the specified filename and creates a new image in which the original image is “flipped” vertically.
    '''
    
    img = load_image(filename)
    height = img.get_height()
    width = img.get_width()
    new_img = Image(height, width)
    
    for r in range(img.get_height()):
        for c in range(img.get_width()):
            pixel = img.get_pixel(r,c)


            new_img.set_pixel(height - 1 - r, c, pixel)
            
    new_filename = 'flip_vert_' + filename
    new_img.save(new_filename)
    

def reduce(filename):
    
    '''loads the PNG image file with the specified filename and creates a new image that is half the size of the original image.
    '''

    img = load_image(filename)
    height = img.get_height()//2
    width = img.get_width()//2  
    new_img = Image(height, width)
    
    for r in range(img.get_height()):
        for c in range(img.get_width()):
            pixel = img.get_pixel(r,c)

            new_img.set_pixel(r//2, c//2, pixel)
            
    new_filename = 'reduce_' + filename
    new_img.save(new_filename)
    
