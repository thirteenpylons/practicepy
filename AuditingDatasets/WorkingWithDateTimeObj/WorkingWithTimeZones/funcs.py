"""
Functions for parsing time values and determining daylight hours.

Both of these functions will be used in the main project.  You should hold on to them.

Author: Christian M. Fulton
Date:   13/08/2021
"""
from dateutil.parser import parse
from pytz import timezone

def str_to_time(timestamp, tz=None):
    """
    Returns the datetime object for the given timestamp (or None if stamp is invalid)
    
    This function should just use the parse function in dateutil.parser to
    convert the timestamp to a datetime object.  If it is not a valid date (so
    the parser crashes), this function should return None.
    
    If the timestamp has a timezone, then it should keep that timezone even if
    the value for tz is not None.  Otherwise, if timestamp has no timezone and 
    tz if not None, this this function will assign that timezone to the datetime 
    object. 
    
    The value for tz can either be a string or a time OFFSET. If it is a string, 
    it will be the name of a timezone, and it should localize the timestamp. If 
    it is an offset, that offset should be assigned to the datetime object.
    
    Parameter timestamp: The time stamp to convert
    Precondition: timestamp is a string
    
    Parameter tz: The timezone to use (OPTIONAL)
    Precondition: tz is either None, a string naming a valid time zone,
    or a time zone OFFSET.
    """
    # HINT: Use the code from the previous exercise and update the timezone
    # Use localize if timezone is a string; otherwise replace the timezone if not None
    try:
        t = parse(timestamp)
        if t.tzinfo is not None:
            return t # return itself if it already has tz
        else:
            if tz is not None:
                if type(tz) == str:
                    t_zone = timezone(tz)
                    nt = t_zone.localize(t)
                    return nt # tz as str:
                else:
                    r = t.replace(tzinfo=tz)
                    return r # tz as offset:
            else:
                r = t.replace(tzinfo=tz)
                return r # if timestamp has no timezone and tz has one-> glue them
    except:
        return None
    
def daytime(time, daycycle):
    """
    Returns true if the time takes place during the day.
    
    A time is during the day if it is after sunrise but before sunset, as
    indicated by the daycycle dicitionary.
    
    A daycycle dictionary has keys for several years (as int).  The value for
    each year is also a dictionary, taking strings of the form 'mm-dd'.  The
    value for that key is a THIRD dictionary, with two keys "sunrise" and
    "sunset".  The value for each of those two keys is a string in 24-hour
    time format.
    
    For example, here is what part of a daycycle dictionary might look like:
    
        "2015": {
            "01-01": {
                "sunrise": "07:35",
                "sunset":  "16:44"
            },
            "01-02": {
                "sunrise": "07:36",
                "sunset":  "16:45"
            },
            ...
        }
    
    In addition, the daycycle dictionary has a key 'timezone' that expresses the
    timezone as a string. This function uses that timezone when constructing
    datetime objects from this set.  If the time parameter does not have a timezone,
    we assume that it is in the same timezone as the daycycle dictionary
    
    Parameter time: The time to check
    Precondition: time is a datetime object
    
    Parameter daycycle: The daycycle dictionary
    Precondition: daycycle is a valid daycycle dictionary, as described above
    """
    # HINT: Use the code from the previous exercise to get sunset AND sunrise
    # Add a timezone to time if one is missing (the one from the daycycle)
    if time.year >= 2015 and time.year <= 2019:
        # if the time parameter does not have a timezone it inherits
        # timezone from daycycle
        dtz = timezone(daycycle['timezone'])
        if time.tzinfo is None:
            time = time.replace(tzinfo=dtz) # the new time with timezone inhertied
        moday = time.strftime('%m-%d')
        set_time = daycycle[str(time.year)][moday]['sunset']
        rise_time = daycycle[str(time.year)][moday]['sunrise']
        pset, prise = parse(str(time)+' '+set_time), parse(str(time)+' '+rise_time)
        # remove inherited tz
        pset, prise = pset.replace(tzinfo=None), prise.replace(tzinfo=None)
        # assign dtz to sunset/rise
        sunset, sunrise = dtz.localize(pset), dtz.localize(prise)
        if time > sunrise and time < sunset:
            return True
        else:
            return False
    else:
        return None