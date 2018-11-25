#! /usr/bin/python3
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

import pandas
import sys
from pprint import pprint

################################################################################
# Parameters
################################################################################

# Trigram model by default
n = 3

################################################################################
# Classes
################################################################################

#TODO:
class clArg:
  def __init__(self, argName, argSpec):
    self.argName = argName
    self.argSpec = argSpec
    # Limit the printing of the argSpec to 80 characters per line minus what is
    #   used on tabbing in the table.

  def argHelp(self):
    name = self.argName
    spec = self.argSpec

    print(name + "\n")
    print(lorem)  
  
    
    
################################################################################
# Functions
################################################################################
def main():
  pass

def helpClMsg():
  print("\n"
        "ngram.py command-line arguments:\n\n"
        "-n\tChanges the ngram model to an integer specified.\n"
        "\tMaximum of 6. Must be an integer.\n\n"
        "-help\tRuns this message.\n")
  nArg.argHelp()
        

def commandLine():
  # System arguments for changing the n of the ngram model
  if sys.argv[1] == "-n":
    if int(sys.argv[2]) < 6: 
      n = int(sys.argv[2])
    else:
      print("-n argument invalid. Defaulting to trigram (n=3) model.")
    
  if sys.argv[1] == "-help":
    helpClMsg()


if __name__ == "__main__":
  nArg = clArg('n', lorem)
  if len(sys.argv) > 1: 
    commandLine()
  main()


################################################################################
# TODO
################################################################################
# [DONE] Take in a system argument for the count of n for the n-gram 
# Generate class for handling command line arguments, making them easy to add 
#   to and print.
# Generate all combinations of the ngram, add to pandas dataframe
# Init a count column and a probability column. 
# Make source variable/dataframe to keep track of sources
# Read in text, add count to data frame.
# How many legal characters do I want to use?
#   Pipe in the legal characters?

