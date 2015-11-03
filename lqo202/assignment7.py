""" General display Assignment 7
 In this section all the answers are displayed and some exception handling is made too
 For question4, the user is asked to enter some parameters in order to display the graph
"""

__author__ = 'luisa'

import script_as7_4 as p4
import script_as7 as p1
import script_as7_2 as p2
import script_as7_3 as p3

#Handling Exceptions in Q1#
print 'Question 1:'
try:
    print 'a: %s' %p1.integ.obtainnewarrays()[0]
    print 'b: %s' %p1.integ.obtainnewarrays()[1]
    print 'c: %s' %p1.integ.obtainnewarrays()[2]
    print 'd: %s' %p1.integ.obtainnewarrays()[3]
except ArithmeticError:
    print 'ArithmeticError ocurred, not possible to do Q1'
except LookupError:
    print 'LookupError ocurred, not possible to do Q1'

#Handling Exceptions in Q2#
print 'Question 2:'
try:
    print p2.assignment7question2.question2()
except ArithmeticError:
    print 'ArithmeticError ocurred, not possible to do Q2'
except LookupError:
    print 'LookupError ocurred, not possible to do Q2'

#Handling Exceptions in Q3#
print 'Question3:'
try:
    print p3.assignment7question3.question3()
except ArithmeticError:
    print 'ArithmeticError ocurred, not possible to do Q2'
except LookupError:
    print 'LookupError ocurred, not possible to do Q2'

#Handling Exceptions in Q4#
print 'Question4: You will need to provide some parameters'
try:
    numberintervals1 = raw_input('Enter the number of values generated for the real part:')
    numberintervals2 = raw_input('Enter the number of values generated for the imaginary part:')
except KeyboardInterrupt:
    'Keyboard interrupted, try again!'
else:
    try:
        print p4.assingment7question4.calculatemandelbrot(numberintervals1, numberintervals2)
    except ArithmeticError:
        print 'ArithmeticError ocurred, not possible to do Q2'
    except LookupError:
        print 'LookupError ocurred, not possible to do Q2'




