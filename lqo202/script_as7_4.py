"""Program for question 4: Creates a static method for cimputing the results
The method created, asks the user for two inputs, that are the number of values to be in the grid in each axis
It saves an image with the name mandelbrot.png and also displays it
 """
__author__ = 'luisa'

import warnings
import numpy as np
import matplotlib.pyplot as plt
from numpy import newaxis

warnings.simplefilter("ignore")

class assingment7question4:
    @staticmethod
    def calculatemandelbrot(numberx, numbery):
        Nummax = 50
        some_threshold = 50

        xvalues = np.array(np.linspace(-2, 1, numberx),dtype=np.float128)
        yvalues = np.array(np.linspace(-1.5, 1.5, numbery),dtype=np.float128)
        gridvalues = xvalues[:, newaxis] + 1j*yvalues[newaxis, :]
        z = gridvalues
        for v in xrange(Nummax):
            z = z**2 + gridvalues

        mandelbrotset = (abs(z) < some_threshold)
        plt.imshow(mandelbrotset.T, extent=[-2, 1, -1.5, 1.5])
        plt.gray()
        plt.savefig('mandelbrot.png')
        plottedmandelbrot=plt.show()
        return plottedmandelbrot