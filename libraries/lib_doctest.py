"""
Notes: =========================================================================
Notes: doctest module:
Notes:
Notes:      doctest.unitest
Notes:      doctest.testmod
Notes:      doctest.script_from_examples
Notes:      doctest.debug
Notes:      doctest.debugscript
Notes:
"""

import doctest

# Get to know about module doctest content
print "========================================================================"
print "doctest Module : start"
print dir(doctest)
print "doctest Module : end"
print "========================================================================"

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print average([20, 30, 70])
    40.0
    >>> print average([10, 20, 30])
    20.0
    >>> print average([10])
    10.0
    """
    return sum(values, 0.0) / len(values)

import doctest
print doctest.testmod()


import unittest

class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()
