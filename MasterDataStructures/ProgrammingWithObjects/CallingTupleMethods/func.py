"""
Module to show off tuple methods.

Neither this module nor the function should import the introcs module.  In addition,
the function should not use a loop or recursion.

Author: Christian M. Fulton
Date: 30/06/2021
"""


def replace_first(tup,a,b):
    """
    Returns a copy of tup with the first value of a replaced by b
    
    Examples:
        replace_first((1,2,1),1,3) returns (3,2,1)
        replace_first((1,2,1),4,3) returns (1,2,1)
    
    Parameter tup: The tuple to copy
    Precondition: tup is a tuple of integers
    
    Parameter a: The value to replace
    Precondition: a is an int
    
    Parameter b: The value to replace with
    Precondition: b is an int
    """
    if a in tup:
      i = tup.index(a)
      l = list(tup)
      l.pop(i) # pop the indexed value of a
      l.insert(i, b)
      result = tuple(l)
    else:
      result = tup
    return result

    