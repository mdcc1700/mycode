#!/usr/bin/env python3

# Common Functions
def common_fn():
    # Common Function Usage
    print("Common Function Usage")
    x=5
    list_1=[1,5,3,2,4]
    int(x)
    float(x)
    str(x)
    len(str(x))
    print("list_1 is type", type(list_1), "with value", list_1)
    print("The min value is:", min(list_1))
    print("The max value is:", max(list_1))
    firstname_1 = input("Please enter your first name: ")
    lastname_1 = input("Please enter your last name: ")
    print("Your name is",firstname_1,lastname_1)
    print("Your name is ",firstname_1,lastname_1,sep="")

common_fn()
