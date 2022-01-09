"""
Module with a function to write CSV files (using data in a 2D list)

This function will be used in the main project.  You should hold on to it.

Author: Christian M. Fulton
Date: 11/08/2021
"""
import csv


def write_csv(data, filename):
    """
    Writes the given data out as a CSV file filename.
    
    To be a proper CSV file, data must be a 2-dimensional list with the first row 
    containing only strings.  All other rows may be any Python value.  Dates are
    converted using ISO formatting. All other objects are converted to their string
    representation.
    
    Parameter data: The Python value to encode as a CSV file
    Precondition: data is a  2-dimensional list
    
    Parameter filename: The file to read
    Precondition: filename is a string representing a path to a file with extension
    .csv or .CSV.  The file may or may not exist.
    """
    # assert 2d list
    # assert only strings for first row
    head = []
    body = []
    for row in data[0]:
        head.append(row)
    for row in data[1:]:
        body.append(row)
    f = open(filename, 'wt')
    wrap = csv.writer(f)
    wrap.writerow(head)
    wrap.writerows(body)
    f.close()
