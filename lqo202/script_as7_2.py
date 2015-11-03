"""Program for question 2: Creates a static method for cimputing the results
In case there is some sort of arithmetic error, it catches the exception
 """
import numpy as np


__author__ = 'luisa'

class assignment7question2():
    @staticmethod
    def question2():
        a = np.arange(25).reshape(5, 5)
        b = np.array([1., 5, 10, 15, 20])
        finalresult = np.zeros(shape=(5,5))
        for i in range(a.shape[1]):
            try:
                finalresult[:, i] = a[:, i]/b[i]
            except ArithmeticError:
                'Some arithmetic error'
        return finalresult
