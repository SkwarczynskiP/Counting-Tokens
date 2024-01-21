# Counting Tokens
CSI 4180 - Natural Language Processing - Homework 0

This text normalization project:
  - Processes an input text file and user configurations
  - Writes and opens a output text file with the unique tokens and their corresponding frequency, ranked from most common to least common
  - Visualizes the data by creating a graph

# Files
The files in this repository include:
  - "hw-0.py" the python script
  - "input.txt" the input text file with natural language that can be normalized
  - "output.txt" the output text file where the ranked tokens and their frequency will be displayed

# How to Run:
  1. Download the files
  2. Write any natural English language into the "input.txt" file. The file currently has a text copy of the novel _Great Expectations_, by Charles Dickens.
  3. Open the terminal and change directories to the location of the downloaded files
  4. Type the command "py hw-0.py input.txt [user-configurations]" to run (Example: py hw-0.py input.txt -l )

# Optional Configurations for Noramlization 
(up to all four customizations can be included)
  - '-l', or '-L', or '--lower'       -> Lowercase tokens
  - '-le', or '-LE', or '--lemma'     -> Lemmatizing okens
  - '-sr', or '-SR', or '--stop_rem'  -> Removes stopwords
  - '-pr', or '-PR', or '--punct_rem' -> Removes punctuation
