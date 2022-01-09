"""
A simple function comparing datetime objects.

Author: Christian M. Fulton
Date:   12/08/2021
"""
import datetime


def is_before(d1,d2):
    """
    Returns True if event d1 happens before d2.
    
    Values d1 and d2 can EITHER be date objects or datetime objects.If a date object,
    assume that it happens at midnight of that day. 
    
    Parameter d1: The first event
    Precondition: d1 is EITHER a date object or a datetime object
    
    Parameter d2: The first event
    Precondition: d2 is EITHER a date object or a datetime object
    """
    comp = datetime.datetime(20, 10, 12)
    if type(d1) != type(comp):
        # convert for comparison
        #d1 = datetime.datetime.fromisoformat(str(d1))
        d1 = parse(str(d1))
    if type(d2) != type(comp):
        # this works in Python 3.8.3:
        #d2 = datetime.datetime.fromisoformat(str(d2))
        # improvise:
        d2 = parse(str(d2))
    if d1 < d2:
        return True
    else:
        return False