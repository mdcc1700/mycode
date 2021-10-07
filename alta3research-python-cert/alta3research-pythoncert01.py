#!/usr/bin/env python3
"""
    Date: 2021-10-08
    From: Michael Ding, michael.ding@gmail.com
    Instructor: Mark Mollere

    Subject: alta3research-pythoncert01.py

    Creating Python script to automate git commands to Github
    - Make an API request to https://api.nasa.gov and display some portion of 
    the data returned in an easily read format

    - Use matplotlib to produce a graph

    - Write a guessing game that uses the crayons library to post in green 
    YOU WIN when the correct answer is supplied

    - Use pandas to create a dataframe, and export some data into a format 
    of your choice
"""

# Modules <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
import getopt        # C-style parser for command line options.
import os            # Operating system dependent functionality.
import sys           # System-specific parameters and functions.
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def print_menu():
    print("1: Display NASA portion of data")
    print("2: Use matplotlib to produce a graph")
    print("3: Guessing game that uses crayons library")
    print("4: Use pandas for dataframe, export data")
    print("Q: Quit")
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def process_input():
    user_input=input("Menu Selection: ")
    try:
        if user_input == "1":
            print("NASA")
        elif user_input == "2":
            print("matplotlib")
        elif user_input == "3":
            print("guessing game")
        elif user_input == "4":
            print("pandas dataframe")
    except:
        pass
    if user_input.lower() == "q":
        sys.exit()
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def main():
    while True:
        print_menu()
        process_input()
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
if __name__ == "__main__":
    main()
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
