#
# julia_sequence.py - Generates Julia Set images
# Written by Ted Burke
# Last updated 10-2-2012
#
 
import numpy
 
# Specify image width and height
w, h = 200, 200
 
# Specify real and imaginary range of image
re_min, re_max = -2.0, 2.0
im_min, im_max = -2.0, 2.0
 
# Generate evenly spaced values over real and imaginary ranges
real_range = numpy.arange(re_min, re_max, (re_max - re_min) / w)
imag_range = numpy.arange(im_max, im_min, (im_min - im_max) / h)
 
# Frame counter
frame = 0
 
# Iterate over a range of c values
for c_im in numpy.arange(0.0, 1.0, 0.01):
    # Increment frame counter
    frame += 1
     
    # Open file and write PGM header info
    filename = "{0:03d}.pgm".format(frame)
    print(filename)
    fout = open(filename, 'w')
    fout.write('P2\n# Julia Set image\n' + str(w) + ' ' + str(h) + '\n255\n')
     
    # Generate pixel values
    for im in imag_range:
        for re in real_range:
            z = complex(re, im)
            c = complex(0.0,c_im)
            n = 255
            while abs(z) < 10 and n >= 5:
                z = z*z + c
                n = n - 5
            # Write pixel value to file
            fout.write(str(n) + ' ')
        fout.write('\n')
         
    # Close file
    fout.close()
