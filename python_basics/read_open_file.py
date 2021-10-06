#!/usr/bin/env python3
"""
    Date: 2021-10-06
    From: Michael Ding
    Subject: read_open_file.py
    # /x,xs/^/  /
"""

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<MODULES>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
# import getopt        # C-style parser for command line options.
# import os            # Operating system dependent functionality.
import sys           # System-specific parameters and functions.
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 

def readfile_fn():
# Method 1, which automatically close file
    with open(sys.argv[1],'r') as myfile:
        print(myfile.read())
    
    # Method 2, which manually close file
    # myfile=open(sys.argv[1],'r')
    # print(myfile.read())
    # myfile.close()
    
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def main():
    readfile_fn()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Calling our main function
if __name__ == "__main__":
     main()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
