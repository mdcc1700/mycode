#!/usr/bin/env python3
"""
    Date: 2021-10-08
    From: Michael Ding, michael.ding@gmail.com
    Instructor: Mark Mollere

    Subject: alta3research-pythoncert01.py

    Creating Python script to automate git commands to Github
    - Make an API request to https://api.nasa.gov and display some portion of 
    the data returned in an easily read format

    - Use Matplotlib to produce a graph

    - Write a guessing game that uses the crayons library to post in green 
    YOU WIN when the correct answer is supplied

    - Use pandas to create a dataframe, and export some data into a format 
    of your choice
"""

# Modules <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
import getopt                    # C-style parser for command line options.
import os                        # Operating system dependent functionality.
import sys                       # System-specific parameters and functions.
import urllib.request            # Old-method of requests
import json                      # JavaScript Object Notation
import requests                  # Make API requests library
import numpy as np               # python3 -m pip install np
import matplotlib.pyplot as plot # python3 -m pip install matplotlib
import random                    # In-Built module Random in Python
import crayons                   # python3 -m pip install crayons
import pandas as pd              # python3 -m pip install pandas xlrd openpyxl
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def print_menu():
    print("\n")
    print("=================================================")
    print("   Michael Ding's Python Certification Program   ")
    print("=================================================")
    print("1: Display NASA API data in Human readable format")
    print("2: Use Matplotlib to produce a graph")
#    print("3: Guessing game that uses crayons library")
    print(f"3: Guessing game that uses {crayons.red('c')}{crayons.green('r')}{crayons.yellow('a')}{crayons.blue('y')}{crayons.magenta('o')}{crayons.white('n')}{crayons.cyan('s')} library")
    print("4: Use pandas for dataframe, export data")
    print("Q: Quit\n")
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def process_input():
    user_input=input("Menu Selection: ")
    try:
        if user_input == "1":
            print("Display NASA API Data in human readable format")
            apodurl='https://api.nasa.gov/planetary/apod?'
            myNASAkey='api_key=17wr3adrJmIztZcQ5BkCNdhDprdpjQTFLY5LNUTF'
            
            # Call NASA APOD URL with API key to request APOD URL object
            apodurlobj=urllib.request.urlopen(apodurl + myNASAkey)
            
            # Read APOD (Astronomy Picture of the Day) Object
            apodread=apodurlobj.read()
            
            # Decode JSON to Python Data Structure
            decodeapod=json.loads(apodread.decode('utf-8'))
            
            # Display Pythonic Data
            print ("Copyright: ",decodeapod['copyright'])
            print ("Date: ",decodeapod['date'])
            print ("Explanation: ",decodeapod['explanation'])
            print ("HD-URL Image: ",decodeapod['hdurl'])
            print ("Media Type: ",decodeapod['media_type'])
            print ("Service Version: ",decodeapod['service_version'])
            print ("Title: ",decodeapod['title'])
            print ("URL: ",decodeapod['url'])

        elif user_input == "2":
            # Get x values of the cosine wave
            time = np.arange(0,12.5, 0.1);

            # Amplitude of the cosine wave is sine of a variable like time
            amplitude = np.cos(time)

            # Plot a cosine wave using amplitude and time
            plot.plot(time, amplitude)
            
            # Give a title for the cosine wave plot
            plot.title('Cosine wave')

            # Give x axis label for the cosine wave plot
            plot.xlabel('Time')

            # Give y axis label for the cosine wave plot
            plot.ylabel('Amplitude = cos(time)')
            plot.grid(True, which='both')
            plot.axhline(y=0, color='k')
            
            # Display the graph
            # plt.show() # can try this on a Python IDE with a GUI if you like

            # SAVE the graph locally
            plot.savefig("/home/student/mycode/alta3research-python-cert/cosine.png")
            # save copy to "~/static" (the "files" view)
            plot.savefig("/home/student/static/cosine.png")
            print(crayons.blue("\nGraph (~/static/cosine.png) is created."))

        elif user_input == "3":
            answer=random.randint(1,6)
            user_guess=int(input("Guess a number between 1 and 6: "))
            while user_guess != answer:
                user_guess=int(input("Wrong! Guess again: "))
            if user_guess==answer:
                print(crayons.green("YOU WIN"))
        elif user_input == "4":
            print(crayons.yellow("Using Pandas, reading CSV to Dataframe."))
            input("Press Enter to continue...")
            df = pd.read_csv ('covid_daily.csv')
            print(df)

            # writeout dataframe to Excel
            df.to_excel("/home/student/mycode/alta3research-python-cert/covid_daily.xlsx")
            df.to_excel("/home/student/static/covid_daily.xlsx")
            print(crayons.blue("\nDataframe to Excel (~/static/covid_daily.xlsx) is created."))

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
