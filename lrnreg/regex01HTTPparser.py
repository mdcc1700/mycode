#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
A script to demonstrate the power of Regular Expression (regex) and
performing HTTP look-ups with the python standard library."""

# standard library imports
import re    
import urllib.request

def main():
    """Search a website's content"""

    print("Where should we search?")
    url = input("> ")  # collect user input

    print(f"Great! So we'll try to open this URL {url} to search for the phrase:")
    searchFor = input("> ")


    # ALL of this is required to strip the text off the response made to the website...
    # - perform the lookup (urllib.request.urlopen(url)
    # - then read the attachment (.read())
    # - finally, translate it from "bytes" to "utf-8" (.decode("utf-8"))
    #
    # This is why the requests library was developed!

    searchMe = urllib.request.urlopen(url).read().decode("utf-8")

    # use the re.search() to determine if our website has the pattern we are looking for
    # it works by taking arguments, the first is the regex search pattern, and the second
    # is the string to search within

    if re.search(searchFor, searchMe):
        print("Found a match!")
    else:
        print("No match!")

if __name__ == "__main__":
    main()

