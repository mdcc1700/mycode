#!/usr/bin/env python3
import os
import sys
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def print_menu():
    print("1: Print \"date\" ten times.")
    print("2: Display directory contents.")
    print("3: Display user name.")
    print("Q: Quit")
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def process_input():
    user_input=input("Menu Selection: ")
    try:
        if user_input == "1":
            for counter in range(10):
                os.system("date")
        elif user_input == "2":
            os.system("ls")
        elif user_input == "3":
            os.system("whoami")
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
