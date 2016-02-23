#
# ps7pr3.py (Problem Set 7, Problem 3)
#
# More image processing!
#
# Computer Science 111
#
# name: Sarah Larbi
# email:slarbi@bu.edu
# 
# This problem is an individual-only problem that you should complete
# on your own.
#

# IMPORTANT: This file is for your solutions to problem 3.
# Your solutions to problem 2 should go in ps7pr2.py instead.

from cs111png import *

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100
    
### PUT YOUR WORK FOR PROBLEM 3 BELOW. ###

def bw(filename, threshold):
    ''' loads the PNG image file with the specified filename and creates a new image that is a black-and-white version of the original image.
    '''
    
    img = load_image(filename)

    for r in range(img.get_height()):
        for c in range(img.get_width()):
            pixel = img.get_pixel(r, c)
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            if brightness(pixel) > threshold:
                new_pixel = ([255, 255, 255])
                img.set_pixel(r,c,new_pixel)
            if brightness(pixel) < threshold:
                new_pixel = ([0, 0, 0])
                img.set_pixel(r,c,new_pixel)
                
    new_filename = 'bw_' + filename
    img.save(new_filename)

# question 2

def mirror_horiz(filename):
    '''loads the PNG image file with the specified filename and creates a new image in which the original image is “mirrored” horizontally.
    '''
 
    img = load_image(filename)
    height = img.get_height()
    width = img.get_width()
    new_img = Image(height, width)
    
    for r in range(height):
        for c in range(0, width//2 + 1):
            pixel = img.get_pixel(r,c)
            left_pixel = new_img.set_pixel(r, c, pixel)
            right_pixel = new_img.set_pixel(r, width - 1 - c, pixel)

            
    new_filename = 'mirror_horiz_' + filename
    new_img.save(new_filename)

# Question 3

def extract(filename, rmin, rmax, cmin, cmax):
    '''loads the PNG image file with the specified filename and extracts a portion of the original image that is specified by the other four parameters.
    '''

    img = load_image(filename)
    height = rmax - rmin
    width = cmax - cmin
    new_img = Image(height, width)

    for r in range(rmin, rmax):
        for c in range(cmin, cmax):
            pixel = img.get_pixel(r, c)
            
            new_img.set_pixel(r-rmin, c-cmin, pixel)
                  
    new_filename = 'extract_' + filename
    new_img.save(new_filename)
            

    
