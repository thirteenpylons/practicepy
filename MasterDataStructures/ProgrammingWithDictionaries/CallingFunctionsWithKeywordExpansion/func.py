"""
Module to demonstrate keyword expansion.

Author: Christian M. Fulton
Date: 06/07/2021
"""
import math


def circ_area(**kwd):    # The parameter is MISSING.  Add it back. 
    """
    Returns the area of the specified circle, defined by the keywords in kwd
    
    The area of a circle is PI r*r where r is the radius
    
    The circle may be specified by 'radius' or 'diameter', but not both.  This function
    should intentionally crash (with an AssertionError) if neither 'radius' nor 'diameter' 
    are specified, or if they both are.
    
    Any keyword arguments other than 'radius' or 'diameter' are ignored.
    
    Examples: 
        circ_area(radius=3) returns approx 28.27433
        circ_area(diameter=4) returns approx 12.56637
        circ_area(radius=3,foo=20) returns approx 28.27433
        circ_area() crashes with AssertionError
        circ_area(radius=2,diameter=4) crashes with AssertionError
    
    Parameter kwd: the function keyword arguments
    Precondition: the arguments are all numbers (int or float)
    """

    if "radius" in kwd:
        assert "diameter" not in kwd
        return math.pi * kwd["radius"] **2
    elif "diameter" in kwd:
        assert "radius" not in kwd
        return 1/4 * math.pi * kwd["diameter"]**2
    else:
        assert "radius" in kwd
        assert "diameter" in kwd