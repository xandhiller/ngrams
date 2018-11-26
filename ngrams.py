#! /usr/bin/python3

import pandas
import sys

################################################################################
# Parameters
################################################################################

# Trigram model by default
n = 3

# For printing 
wordLength = 10

################################################################################
# Classes
################################################################################

class clArg:
  def __init__(self, argName, argSpec):
    self.argName = argName
    self.argSpec = argSpec

  def argHelp(self):
    name = self.argName
    spec = self.argSpec
  
    print(str(name), end='')
    lines = spec.split()
    lines = [' '.join(lines[i:i+wordLength]) \
             for i in range(0, len(lines), wordLength)] 

    for i in range(len(lines)): 
      print("\t" + lines[i])
    print() # Formatting.
    
    
    
################################################################################
# Functions
################################################################################
def main():
  pass

def helpClMsg():
  print("\n"
        "ngram.py command line arguments:\n")
  helpArg.argHelp()
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
  # Init command line arguments:
  helpArg = clArg('-help', "Runs this message.")
  nArg = clArg('-n', 
               "Changes the ngram model to an integer specified."
               " Maximum of 6. Must be an integer.")

  if len(sys.argv) > 1: 
    commandLine()
    
  main()


################################################################################
# TODO
################################################################################
# [DONE] Take in a system argument for the count of n for the n-gram 
# [DONE] Generate class for handling command line arguments, making them easy to add 
#   to and print.
# Generate all combinations of the ngram, add to pandas dataframe
# Init a count column and a probability column. 
# Make source variable/dataframe to keep track of sources
# Read in text, add count to data frame.
# How many legal characters do I want to use?
#   Pipe in the legal characters?
