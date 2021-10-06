#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   solution to code customization 01"""


import zipfile

def main():
    """runtime code"""

    iszip = input("What is the file you would like to examine (full or relative path)? ")

    if zipfile.is_zipfile(iszip):   # returns true if the file is a zip file
        print("Yep! That is a 'zip' file.")
    else:
        print("Nay. That is not a 'zip' file.")

if __name__ == "__main__":
    main()

