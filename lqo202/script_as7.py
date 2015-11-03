"""Program for question 1: Uses a Matrix class (which is a subclass or numpy)  and calculates the arrays asked in Q1
The function used returns a list of arrays of the answers
 """
import numpy as np
import functools


__author__ = 'lqo202'


class ExceptionMatrix:
    def __init__(self, msg):
        self.msg = msg


class Matrix:
    def __init__(self):
        self._array = np.transpose(np.resize(np.arange(1, 15, 1), (3, 5)))

    #This part of the code was modified from the original in stackoverflow#
    def __getattr__(self, attributematrix):
        try:
            return getattr(self._array, attributematrix)
        except AttributeError:
            f = getattr(np, attributematrix, None)
            if hasattr(f, '__call__'):
                return functools.partial(f, self._array)
            else:
                raise AttributeError(attributematrix)

    def obtainnewarrays(self):
        arraysecondfourthrow = self._array[(1, 3), :]
        arraysecondcolumn = self._array[:, 1]
        arrayselection = self._array[1:-1, 0:]
        arrayelements = self._array[(self._array>3) & (self._array<11)]
        return [arraysecondfourthrow, arraysecondcolumn, arrayselection, arrayelements]

    def __repr__(self):
        newmatrix = ["%.2f" % x for x in Matrix.obtainnewarrays(self)]
        for i in range(len(Matrix.obtainnewarrays(self))):
            printstring = 'Result %s is ' %i + str(newmatrix[i])
            print printstring

integ=Matrix()
