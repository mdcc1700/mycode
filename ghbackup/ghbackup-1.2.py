#!/usr/bin/env python3
"""
    Date: 2021-10-06
    From: Michael Ding, michael.ding@gmail.com
    Subject: gmbackup.py

    Creating Python script to automate git commands to Github

    cd ~/mycode
    git add *
    git commit -m # "studying for logic"
    git push origin
"""

# Modules <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
import getopt        # C-style parser for command line options.
import os            # Operating system dependent functionality.
import sys           # System-specific parameters and functions.
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def scan_for_arguments(git_comment):
  argumentList = sys.argv[1:]
  options      = "c:v"
  long_options = ["version"]
  version      = '1.2'
  try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
    for currentArgument, currentValue in arguments:
      if currentArgument in ("-c", "--comment"):
        return currentValue 
      elif currentArgument in ("-v", "--version"):
        print (os.path.basename(sys.argv[0]), version)
  except:
    print("Error 101")
  sys.exit()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def run_git_commands(git_comment):
  if len(sys.argv) == 1 or git_comment:
    if bool(git_comment):
      commit_message = git_comment
    else:
      commit_message = input("Commit Comment: ")
    os.chdir("/home/student/mycode")
    os.system("git add *")
    os.system('git commit -m "'+commit_message+ '"')
    os.system("git push origin")
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def main():
     run_git_commands(scan_for_arguments(""))
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
if __name__ == "__main__":
   main()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
