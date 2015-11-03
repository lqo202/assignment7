"""Program for question 3: Creates a static method for cimputing the results
There is an attempt code
The function selects the closest to 0.5 value of the matrix
 """
import numpy as np

__author__ = 'luisa'


class assignment7question3():
    @staticmethod
    def question3():
        randomarray = np.random.rand(10, 3)
        arrayordered = np.argsort(abs(randomarray-0.5))[:, 0]

        #Attempt 1: obtaining
        #outarray = np.zeros(10)
        #for i in range(randomarray.shape[0]):
        #    outarray[i] = randomarray[i, arrayordered[i]]

        #With fancy indexing
        maskedarray = np.random.rand(10, 3)
        for i in range(len(randomarray)):
            x = arrayordered[i]
            maskedarray[i, x]=1

        maskedarray=(maskedarray==1)
        outarray=randomarray[maskedarray].copy()
        return  outarray


