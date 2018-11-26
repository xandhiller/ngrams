#! /usr/bin/python3

################################################################################
# Libraries
################################################################################

import pandas
import sys
import time


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
 
 
class ngram:
  def __init__(self):
    pass
    
    
################################################################################
# Functions
################################################################################

def main():
  print(len(englishChars))
  print(genCombinations(n, englishChars))


def helpClMsg():
  print("\n"
        "ngram.py command line arguments:\n")
  helpArg.argHelp()
  nArg.argHelp()
        

def commandLine(n):
  # System arguments for changing the n of the ngram model
  if "-n" in sys.argv: 
    if int(sys.argv[2]) < maxNgramVal:
      n = int(sys.argv[2])
    else:
      print("-n argument invalid. Defaulting to trigram (n=3) model.")
    
  if sys.argv[1] == "-help":
    helpClMsg()

  return n


def getFileDate():
  string = time.asctime()
  string = string.split(' ')[1:] # Get rid of the spaces and format
  string = '_'.join(string)
  string = string.split(':')
  string = '.'.join(string)
  string = string[0:3] + string[4:] # Format it prettier.
  return string


# Recursive function to generate all combinations
def genCombinations(n, chars):
  newChars = chars
  for c in chars:
    for i,el in enumerate(chars):
      newChars.append(el + c)

  return newChars
  

# TODO
def outputCorpus():
  pass


################################################################################
# Parameters
################################################################################

# Base 
wordBaseIO = "wordBaseFormatted.txt"

# Corpus output path.
outputPath = "corpus/" + getFileDate() + "_" + wordBaseIO[:-4] + '.txt'

# Trigram model by default
N = 3

# Maximum nGramValue to prevent combinatorial explosion
maxNgramVal = 6

# For printing command line help
wordLength = 10

# Character base, including space at the end
englishChars = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ .'")

################################################################################
# IfNEM
################################################################################

if __name__ == "__main__":
  # Init command line arguments:
  helpArg = clArg('-help', "Runs this message.")
  nArg = clArg('-n', 
               "Changes the ngram model to an integer specified."
               " Maximum of 6. Must be an integer.")

  if len(sys.argv) > 1: 
    n = commandLine(N)
    
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
