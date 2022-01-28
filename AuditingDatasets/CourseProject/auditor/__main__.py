"""
The script code for the application.

This file should be kept simple.  If written correctly, it will have no more than
three lines of code (most of those imports).  It should call the execute() function
in module app.py, passing it the contents of sys.argv EXCEPT for the application name
(so only the command line arguments AFTER 'python auditor').

"""
import sys, app
app.execute(sys.argv[1:])
