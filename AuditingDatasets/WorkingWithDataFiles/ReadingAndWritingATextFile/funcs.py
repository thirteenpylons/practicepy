"""
Functions for simple reading to and writing from a file.

Author: Christian M. Fulton
Date:   11/08/2021
"""


def count_lines(filepath):
    """
    Returns the number of lines in the given file.
    
    Lines are separated by the '\n' character, which is standard for Unix files.
    
    Parameter filepath: The file to be read
    Precondition: filepath is a string with the FULL PATH to a text file
    """
    count = 0
    with open(filepath, "r") as rfile:
        for line in rfile:
            count += 1
    return count


def write_numbers(filepath, n):
    """
    Writes the numbers 0..n-1 to a file.
    
    Each number is on a line by itself.  So the first line of the file is 0,
    the second line is 1, and so on. Lines are separated by the '\n' character, 
    which is standard for Unix files.  The last line (the one with the number
    n-1) should NOT end in '\n'
    
    Parameter filepath: The file to be written
    Precondition: filepath is a string with the FULL PATH to a text file
    
    Parameter n: The number of lines to write
    Precondition: n is an int > 0.
    """
    # HINT: You can only write strings to a file, so convert the numbers first
    # take n and write that many lines in a file
    with open(filepath, "wt") as rfile:
        for i in range(n):
            if i != n-1:
                rfile.write(str(i)+'\n')
            else:
                rfile.write(str(i))