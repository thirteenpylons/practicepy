"""
Module demonstrating how to write functions with objects.

This module contains two versions of the same function.  One version returns a new
value, while other modifies one of the arguments to contain the new value.

Author: Christian M. Fulton
Date: 23/06/2021
"""
import clock


def add_time1(time1, time2):
    """
    Returns the sum of time1 and time2 as a new Time object
    
    DO NOT ALTER time1 or time2, even though they are mutable
    
    Examples: 
        The sum of 12hr 13min and 13hr 12min is 25hr 25min 
        The sum of 1hr 59min and 3hr 2min is 5hr 1min 
    
    Parameter time1: the starting time
    Precondition: time1 is a Time object
    
    Parameter time2: the time to add
    Precondition: time2 is a Time object
    """
    t1h, t2h = time1.hours, time2.hours
    t1m, t2m = time1.minutes, time2.minutes
    th = t1h + t2h
    tm = t1m + t2m
    if tm >= 60:
      th += 1
      tm -= 60
    result = clock.Time(th,tm)

    return result





def add_time2(time1, time2):
    """
    Modifies time1 to be the sum of time1 and time2
    
    DO NOT RETURN a new time object.  Modify the object time1 instead.
    
    Examples: 
        The sum of 12hr 13min and 13hr 12min is 25hr 25min 
        The sum of 1hr 59min and 3hr 2min is 5hr 1min 
    
    Parameter time1: the starting time
    Precondition: time1 is a Time object
    
    Parameter time2: the time to add
    Precondition: time2 is a Time object
    """
    t2h = time2.hours
    t2m = time2.minutes
    time1.hours = time1.hours + t2h
    if time1.minutes + t2m >= 60:
      time1.hours += 1
      time1.minutes += t2m - 60
    else:
      time1.minutes += t2m