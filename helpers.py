from matplotlib import pylab
import japa

def create_antigen(name):
    image_matrix = pylab.imread('digits/' + name + '.png')
    shape = []

    for row in image_matrix:
        shape += [all(pixel) == 0 for pixel in row] # Converts colour to boolean (black = True)

    return japa.Antigen(shape)
