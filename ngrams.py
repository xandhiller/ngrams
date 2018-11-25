#! /usr/bin/python3

import pandas
import sys

################################################################################
# Parameters
################################################################################

# Trigram model by default
n = 3

################################################################################
# Classes
################################################################################

#TODO:
# class clArg:
#   def __init__(self, argName, argSpec):
#     self.argName = argName
#     self.argSpec = argSpec
#     # Limit the printing of the argSpec to 80 characters per line minus what is
#     #   used on tabbing in the table.
      

    
    
################################################################################
# Functions
################################################################################
def main():
  print(sys.argv)


def helpClMsg():
  print("\nngram.py command-line arguments:\n\n"
        "-n\tChanges the ngram model to an integer specified.\n"
        "\tMaximum of 6. Must be an integer.\n\n"
        "-help\tRuns this message.\n")
        

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

