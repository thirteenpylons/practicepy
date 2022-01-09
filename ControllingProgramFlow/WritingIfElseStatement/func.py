"""  
A function to search for the first vowel position

Author: Christian M. Fulton
Date: 05/05/2021
"""
import introcs


def first_vowel(s):
    """
    Returns the position of the first vowel in s; it returns len(s) if there are no vowels.
    
    We define the vowels to be the letters 'a','e','i','o', and 'u'.  The letter
    'y' counts as a vowel only if it is not the first letter in the string.
    
    Examples: 
        first_vowel('hat') returns 1
        first_vowel('grrm') returns 4
        first_vowel('sky') returns 2
        first_vowel('year') returns 1
    
    Parameter s: the string to search
    Precondition: s is a nonempty string with only lowercase letters
    """
    result = len(s)
    a = introcs.find_str(s, "a")
    e = introcs.find_str(s, "e")
    i = introcs.find_str(s, "i")
    o = introcs.find_str(s, "o")
    u = introcs.find_str(s, "u")
    y = introcs.find_str(s, "y")
 
    vowels = []
    if "a" in s:
        vowels.append(a)
        result = min(vowels)
    if "e" in s:
        vowels.append(e)
        result = min(vowels)
    if "i" in s:
        vowels.append(i)
        result = min(vowels)
    if "o" in s:
        vowels.append(o)
        result = min(vowels)
    if "u" in s:
        vowels.append(u)
        result = min(vowels)
    if "y" in s[1:] and s[:1] != "y":
        vowels.append(y)
        result = min(vowels)
    return result