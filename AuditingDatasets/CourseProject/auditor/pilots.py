"""
Module determining pilot certifications, ratings, and endorsements.

The restrictions that we place on a pilot depend on their qualifications.  There are three
ways to think about a pilot.  

(1) Certifications.  These are what licenses a pilot has.  We also use these to classify
where the student is in the licensing process.  Is the student post solo (can fly without
instructor), but before license?  Is the student 50 hours past their license (a threshold 
that helps with insurance)?

(2) Ratings.  These are extra add-ons that a pilot can add to a license. For this project,
the only rating is Instrument Rating, which allows a pilot to fly through adverse weather
using only instruments.

(3) Endorsements. These are permission to fly certain types of planes solo.  Advanced 
allows a pilot to fly a plane with retractable landing gear. Multiengine allows a pilot
to fly a plane with more than one engine.

The file pilots.csv is a list of all pilots in the school, together with the dates that
they earned these certifications, ratings, and endorsements.  Specifically, this CSV file
has the following header:
    
    ID  LASTNAME  FIRSTNAME  JOINED  SOLO  LICENSE  50 HOURS  INSTRUMENT  ADVANCED  MULTIENGINE

The first three columns are strings, while all other columns are dates.

The functions in this class take a row from the pilot table and determine if a pilot has
a certain qualification at the time of takeoff. As this program is auditing the school 
over a course of a year, a student may not be instrument rated for one flight but might
be for another.

The preconditions for many of these functions are quite messy.  While this makes writing 
the functions simpler (because the preconditions ensure we have less to worry about), 
enforcing these preconditions can be quite hard. That is why it is not necessary to 
enforce any of the preconditions in this module.

Author: Christian M. Fulton
Date: 18/08/2021
"""
import utils


# CERTIFICATION CLASSIFICATIONS
# The certification of this pilot is unknown
PILOT_INVALID = -1
# A pilot that has joined the school, but has not soloed
PILOT_NOVICE  = 0
# A pilot that has soloed but does not have a license
PILOT_STUDENT = 1
# A pilot that has a license, but has under 50 hours post license
PILOT_CERTIFIED = 2
# A pilot that 50 hours post license
PILOT_50_HOURS  = 3


def get_certification(takeoff, student):
    """
    Returns the certification classification for this student at the time of takeoff.
    
    The certification is represented by an int, and must be the value PILOT_NOVICE, 
    PILOT_STUDENT, PILOT_CERTIFIED, PILOT_50_HOURS, or PILOT_INVALID. It is PILOT_50_HOURS 
    if the student has certified '50 Hours' before this flight takeoff.  It is 
    PILOT_CERTIFIED if the student has a private license before this takeoff and 
    PILOT_STUDENT is the student has soloed before this takeoff.  A pilot that has only
    just joined the school is PILOT_NOVICE.  If the flight takes place before the student
    has even joined the school, the result is PILOT_INVALID.
    
    Recall that a student is a 10-element list of strings.  The first three elements are
    the student's identifier, last name, and first name.  The remaining elements are all
    timestamps indicating the following in order: time joining the school, time of first 
    solo, time of private license, time of 50 hours certification, time of instrument 
    rating, time of advanced endorsement, and time of multiengine endorsement.
    
    Parameter takeoff: The takeoff time of this flight
    Precondition: takeoff is a datetime object
    
    Parameter student: The student pilot
    Precondition: student is 10-element list of strings representing a pilot
    """
    # ELEMENTS: 0 -> SID, 1 -> LName, 2 -> FName, 3 -> Time Joined school,
    # 4 -> first solo, 5 -> private license, 6 -> 50hr cert, 7 -> instrument rating,
    # 8 -> advanced endorsement, 9 -> multiengine endorsement
    loc = None
    certs = [utils.str_to_time(n) for n in student[3:7] if n != '']
    for j in certs:
        if takeoff >= j:
            loc = certs.index(j)
    if loc == 0:
        return PILOT_NOVICE
    elif loc == 1:
        return PILOT_STUDENT
    elif loc == 2:
        return PILOT_CERTIFIED
    elif loc == 3:
        return PILOT_50_HOURS
    else:
        return PILOT_INVALID
"""
    keys = ['STUDENT_ID', 'LAST_NAME', 'FIRST_NAME', 'PILOT_NOVICE', 'PILOT_STUDENT', 'PILOT_CERTIFIED',
        'PILOT_50_HOURS', 'INSTRUMENT_RATING', 'ADVANCED_ENDORSEMENT', 'MULTIENGINE']
    certs = { k:v for (k,v) in zip(keys, rdata)}
    for c, v in certs.items():
        if v != '':
            # try: take c and datetime(v) store in variable
            try:
                cleaned[c]=utils.str_to_time(v)
            except:
                print('skipped')
    for cert in keys[-7:]: # only the certs
        if cert in certs:
            if certs[cert] != '':
                ctime = utils.str_to_time(certs[cert])
                if takeoff < ctime:
                    cleaned[cert]=ctime
    res = dict(reversed(list(cleaned.items())))
    result = list(res.keys())[0]    
    return result
"""


def has_instrument_rating(takeoff,student):
    """
    Returns True if the student has an instrument rating at the time of takeoff, False otherwise
    
    Recall that a student is a 10-element list of strings.  The first three elements are
    the student's identifier, last name, and first name.  The remaining elements are all
    timestamps indicating the following in order: time joining the school, time of first 
    solo, time of private license, time of 50 hours certification, time of instrument 
    rating, time of advanced endorsement, and time of multiengine endorsement.
    
    NOTE: Just because a pilot has an instrument rating does not mean that every flight
    with that pilot is an IFR flight.  It just means the pilot could choose to use VFR
    or IFR rules.
    
    Parameter takeoff: The takeoff time of this flight
    Precondition: takeoff is a datetime object
    
    Parameter student: The student pilot
    Precondition: student is 10-element list of strings representing a pilot
    """
    # extract instrument_rating indexed(7)
    instrument_cert = utils.str_to_time(student[7])
    try:
        if takeoff >= instrument_cert:
            return True
        else:
            return False
    except:
        return False


def has_advanced_endorsement(takeoff,student):
    """
    Returns True if the student has an endorsement to fly an advanced plane at the time of takeoff.
    
    The function returns False otherwise.
    
    Recall that a student is a 10-element list of strings.  The first three elements are
    the student's identifier, last name, and first name.  The remaining elements are all
    timestamps indicating the following in order: time joining the school, time of first 
    solo, time of private license, time of 50 hours certification, time of instrument 
    rating, time of advanced endorsement, and time of multiengine endorsement.
    
    Parameter takeoff: The takeoff time of this flight
    Precondition: takeoff is a datetime object
    
    Parameter student: The student pilot
    Precondition: student is 10-element list of strings representing a pilot
    """
    adv_endorsement = utils.str_to_time(student[8])
    try:
        if takeoff >= adv_endorsement:
            return True
        else:
            return False
    except:
        return False


def has_multiengine_endorsement(takeoff,student):
    """
    Returns True if the student has an endorsement to fly an multiengine plane at the time of takeoff.
    
    The function returns False otherwise.
    
    Recall that a student is a 10-element list of strings.  The first three elements are
    the student's identifier, last name, and first name.  The remaining elements are all
    timestamps indicating the following in order: time joining the school, time of first 
    solo, time of private license, time of 50 hours certification, time of instrument 
    rating, time of advanced endorsement, and time of multiengine endorsement.
    
    Parameter takeoff: The takeoff time of this flight
    Precondition: takeoff is a datetime object
    
    Parameter student: The student pilot
    Precondition: student is 10-element list of strings representing a pilot
    """
    multi_engine = utils.str_to_time(student[9])
    try:
        if takeoff >= multi_engine:
            return True
        else:
            return False
    except:
        return False


def get_minimums(cert, area, instructed, vfr, daytime, minimums):
    """
    Returns the most advantageous minimums for the given flight category.
    
    The minimums is the 2-dimensional list (table) of minimums, including the header.
    The header for this table is as follows:
        
        CATEGORY  CONDITIONS  AREA  TIME  CEILING  VISIBILITY  WIND  CROSSWIND
    
    The values in the first four columns are strings, while the values in the last
    four columns are numbers.  CEILING is a measurement in ft, while VISIBILITY is in
    miles.  Both WIND and CROSSWIND are speeds in knots.
    
    This function first searches the table for rows that match the function parameters. 
    It is possible for more than one row to be a match.  A row is a match if ALL four 
    of the first four columns match.
    
    The first column (CATEGORY) has values 'Student', 'Certified', '50 Hours', or 'Dual'.
    If the value 'Student', it is a match if category is PILOT_STUDENT or higher.  If
    the value is 'Certified, it is a match if category is PILOT_CERTIFIED or higher. If
    it is '50 Hours', it is only a match if category is PILOT_50_HOURS. The value 'Dual' 
    only matches if instructed is True.
    
    The second column (CONDITIONS) has values 'VMC' and 'IMC'. A flight filed as VFR 
    (visual flight rules) is subject to VMC (visual meteorological conditions) minimums.  
    Similarly, a fight filed as IFR is subject to IMC minimums.
    
    The third column (AREA) has values 'Pattern', 'Practice Area', 'Local', 
    'Cross Country', or 'Any'. Flights that are in the pattern or practice area match
    'Local' as well.  All flights match 'Any'.
    
    The fourth column (TIME) has values 'Day' or 'Night'. The value 'Day' is only 
    a match if daytime is True. If it is False, 'Night' is the only match.
    
    Once the function finds the all matching rows, it searches for the most advantageous
    values for CEILING, VISIBILITY, WIND, and CROSSWIND. Lower values of CEILING and
    VISIBILITY are better.  Higher values for WIND and CROSSWIND are better.  It then
    returns this four values as a list of four floats (in the same order they appear)
    in the table.
    
    Example: Suppose minimums is the table
        
        CATEGORY   CONDITIONS  AREA           TIME  CEILING  VISIBILITY  WIND  CROSSWIND
        Student    VMC         Pattern        Day   2000     5           20    8
        Student    VMC         Practice Area  Day   3000     10          20    8
        Certified  VMC         Local          Day   3000     5           20    20
        Certified  VMC         Practice Area  Night 3000     10          20    10
        50 Hours   VMC         Local          Day   3000     10          20    10
        Dual       VMC         Any            Day   2000     10          30    10
        Dual       IMC         Any            Day   500      0.75        30    20
    
    The call get_minimums(PILOT_CERTIFIED,'Practice Area',True,True,True,minimums) matches
    all of the following rows:
        
        Student    VMC         Practice Area  Day   3000     10          20    8
        Certified  VMC         Local          Day   3000     5           20    20
        Dual       VMC         Any            Day   2000     10          30    10
    
    The answer in this case is [2000,5,30,20]. 2000 and 5 are the least CEILING and 
    VISIBILITY values while 30 and 20 are the largest wind values.
    
    If there are no rows that match the parameters (e.g. a novice pilot with no 
    instructor), this function returns None.
    
    Parameter cert: The pilot certification
    Precondition: cert is in int and one PILOT_NOVICE, PILOT_STUDENT, PILOT_CERTIFIED, 
    PILOT_50_HOURS, or PILOT_INVALID.
    
    Parameter area: The flight area for this flight plan
    Precondition: area is a string and one of 'Pattern', 'Practice Area' or 'Cross Country'
    
    Parameter instructed: Whether an instructor is present
    Precondition: instructed is a boolean
    
    Parameter vfr: Whether the pilot has filed this as an VFR flight
    Precondition: vfr is a boolean
    
    Parameter daytime: Whether this flight is during the day
    Precondition: daytime is boolean
    
    Parameter minimums: The table of allowed minimums
    Precondition: minimums is a 2d-list (table) as described above, including header
    """
    # Find all rows that can apply to this student
    # Find the best values for each column of the row
    certifications = {
                    'Student': PILOT_STUDENT,
                    'Certified': PILOT_CERTIFIED,
                    '50 Hours': PILOT_50_HOURS,
                    'Dual': PILOT_50_HOURS+1,
                    }
    result = []
    # This function first searches the table for rows that match the function parameters. 
    # It is possible for more than one row to be a match.  A row is a match if ALL four 
    # of the first four columns match.
    for m in minimums[1:]:
        check_cert = False
        check_area = False
        check_daytime = False
        check_vfr = False

        # check certification:
        # check arg == to 'SOMETHING' against minimums row
        if cert in certifications and cert >= m[index_cert]:
            check_cert = True

    #

    #If the value 'Student', it is a match if category is PILOT_STUDENT or higher.
    #If the value is 'Certified, it is a match if category is PILOT_CERTIFIED or higher.
    #If it is '50 Hours', it is only a match if category is PILOT_50_HOURS. 
    #The value 'Dual' only matches if instructed is True.

    #! MEASUREMENTS: Ceiling->ft Visibility->miles Wind/Crosswind->miles !

    #Once the function finds the all matching rows, it searches for the most advantageous
    #values for CEILING, VISIBILITY, WIND, and CROSSWIND. Lower values of CEILING and
    #VISIBILITY are better.  Higher values for WIND and CROSSWIND are better.  It then
    #returns this four values as a list of four floats (in the same order they appear)
    #in the table.

    #Student,VMC,Pattern,Day,2000,5,20,8

""" possibilities:
    ('Pattern', 'Practice Area', 'Cross Country')
('Pattern', 'Cross Country', 'Practice Area')
('Practice Area', 'Pattern', 'Cross Country')
('Practice Area', 'Cross Country', 'Pattern')
('Cross Country', 'Pattern', 'Practice Area')
('Cross Country', 'Practice Area', 'Pattern')
('Instructor', 'Alone')
('Alone', 'Instructor')
('True', 'False')
('False', 'True')
('Day', 'Night')
('Night', 'Day')
"""
    index_category, index_conditions, index_area, index_time, index_ceiling,\
    index_visibility, index_wind, index_crosswind = 0, 1, 2, 3, 4, 5, 6, 7
    # translate cert string to global var that is assigned to integer value
    certifications = {'Student': PILOT_STUDENT,
                    'Certified': PILOT_CERTIFIED,
                    '50 Hours': PILOT_50_HOURS,
                    }
    matching_areas = ['Pattern', 'Any', 'Local', 'Practice Area']
    t_alts = {'Day': True,
              'VMC': True,
             }
    f_alts = {'Night': False,
              'IMC': False,
            }

    res_rows = []
    check_cert = False
    for r in minimums[1:]: # iterate through each row in minimums
        # reset values to check for each iterations:
        check_area = False
        check_daytime = False
        check_vfr = False
        
        if r[index_category] in certifications:
            current_cert = certifications[r[index_category]]
        elif r[index_category] == 'Dual':
            if instructed:
                current_cert = PILOT_INVALID
            else:
                current_cert = PILOT_50_HOURS+1
        if cert >= current_cert and cert != PILOT_50_HOURS:
            check_cert = True
        if check_cert:
            if r[index_area] == 'Cross Country':
                check_area = area == r[index_area]
            elif r[index_area] in matching_areas:
                check_area = any(area == i for i in matching_areas)
                
        if check_cert and check_area:
            if r[index_time] in t_alts and daytime in t_alts.values():
                check_daytime = True
            elif r[index_time] in f_alts and daytime in f_alts.values():
                check_daytime = True
                
        if check_cert and check_area and check_daytime:
            # if vfr: can only fly 'VMC' elif vfr is False: # can fly 'VMC' or 'IMC'
            if vfr is True:
                check_cert = r[index_conditions] == 'VMC'
            else:
                check_cert = True
            #if r[index_conditions] in t_alts and vfr in t_alts.values():
            #    check_vfr = True
            #elif r[index_conditions] in f_alts and vfr in f_alts.values():
            #    check_vfr = True

        # if it all matches append res_rows with row
        if check_cert and check_area and check_daytime and check_vfr:
            res_rows.append(r)
    result = []
    final_result = []
    for r in res_rows:
        result.append(r[4:])
    vals = {0:[],1:[],2:[],3:[]} # dict to organize values
    # organize the values to compare:
    for r in result:
        for i in r:
            i_index = r.index(i)
            if i_index in vals:
                vals[i_index].append(float(i)) # convert to float
            r[i_index] = 0
    if len(result) > 0:
        for v in vals:
            if v == 0:
                final_result.append(min(vals[v]))
            if v == 1:
                final_result.append(min(vals[v]))
            if v == 2:
                final_result.append(max(vals[v]))
            if v == 3:
                final_result.append(max(vals[v]))
    if len(final_result) > 0:
        return final_result
    else:
        return None