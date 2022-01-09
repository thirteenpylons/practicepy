"""
Functions for working with datetime objects.

Author: Christian M. Fulton
Date:   12/08/2021
"""
import datetime


def christmas_day(year):
    """
    Returns ISO day of the week for Christmas in the given year.
    
    The ISO day is an integer between 1 and 7.  It is 1 for Monday, 7 for Sunday 
    and the appropriate number for any day in-between. 
    
    Parameter year: The year to check for Christmas
    Precondition: years is an int > 0 (and a year using the Gregorian calendar)
    """
    result = datetime.date(year, 12, 25)
    return datetime.date.isoweekday(result)

def iso_str(d,t):
    """
    Returns the ISO formatted string of data and time together.
    
    When combining, the time must be accurate to the microsecond.
    
    Parameter d: The month-day-year
    Precondition: d is a date object
    
    Parameter t: The time of day
    Precondition: t is a time object
    """
    # HINT: Combine date and time into a datetime and use isoformat
    comp = datetime.datetime(20, 10, 12)
    if type(d1) != type(comp):
        d1 = datetime.datetime.fromisoformat(str(d1))
    if type(d2) != type(comp):
        d2 = datetime.datetime.fromisoformat(str(d2))
    if d1 < d2:
        return True
    else:
        return False