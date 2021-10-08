#!/usr/bin/python3
""" RZFeeser | Alta3 Research
Learn to search strings of data with complex regex patterns
"""

# Python standard library
import re

def main():
    # hardcode the string we'll search through
    contact = "Contact: <sip:+17175664428@[2600:2304:9210:ec::2]:5060;eri-generated-at=10.172.0.132>"

    # parse out the contact string using our regex logic
    conobj = re.search(r'sip:\+(\d+)@\[(.*)\]:?(\d+)?', contact)

    # searches test True if they find a match
    # False if no match
    if conobj:
        # display the match
        print(conobj.group())

        # display the phone number (group 1)
        print("The phone number is...")
        print(conobj.group(1))

        # display the IPv6 (group 2)
        print("The IPv6 is...")
        print(conobj.group(2))

        # display the port (group 3)
        print("The port is...")
        print(conobj.group(3))

if __name__ == "__main__":
    main()

