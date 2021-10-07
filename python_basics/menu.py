#!/usr/bin/env python3
import os
import sys
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def print_menu(menu_name_print_menu):
    print("==============================")
    print("1: Print \"date\" ten times.")
    print("2: Display directory contents.")
    print("3: Display user name.")
    print("Q:" ,menu_name_print_menu)
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
    return user_input
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def main():
    while True:
        menu_name_main=("Foobar")
        print_menu(menu_name_main)
        print(">>>",process_input(""))
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
if __name__ == "__main__":
    main()
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
