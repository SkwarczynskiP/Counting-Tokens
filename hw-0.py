import argparse
import os
import re

import nltk
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str, help='The name of the input file')
parser.add_argument('-l', '-L', '--lower', help='Lower casing Tokens', action='store_true')
parser.add_argument('-le', '-LE', '--lemma', help='Lemmatizing Tokens', action='store_true')
parser.add_argument('-sr', '-SR', '--stop_rem', help='Removing Stopwords', action='store_true')
parser.add_argument('-pr', '-PR', '--punct_rem', help='Removing Punctuation', action='store_true')
args = parser.parse_args()

tempList = list()
tokens = list()
tokenCounts = list()
lemma = list()
filteredWords = list()

nltk.download('stopwords')
stopWords = set(stopwords.words('english'))

nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

with open(args.filename, 'r', encoding='utf-8') as f:
    file = f.read()

# lowercases each token
if args.lower:
    file = file.lower()

# removes all punctuation
if args.punct_rem:
    file = re.sub(r'[^\w\s]', '', file)

# removes all stopwords
if args.stop_rem:
    tempList = file.split()
    filteredWords = [tempList for tempList in tempList if tempList.lower() not in stopWords]
    file = (' '.join(filteredWords))

# lemmatization of each token
if args.lemma:
    tempList = file.split()
    lemma = [lemmatizer.lemmatize(tempList) for tempList in tempList]
    file = (' '.join(lemma))

words = nltk.word_tokenize(file)
frequency = nltk.FreqDist(words)

# prints the tokens and their corresponding frequency
xValues = []
yValues = []
with open('output.txt', 'w', encoding='utf-8') as f:
    for token, freq in frequency.most_common():
        f.write(f'{token} {freq}\n')
        xValues.append(token)
        yValues.append(freq)

os.system(f'start {'output.txt'}')

# creates the graph
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(xValues, yValues)
ax.set_yscale('log')
ax.set_ylabel('log')
plt.title("Token Frequency Distribution")
plt.xlabel("Tokens")
plt.ylabel("Frequency")
plt.show()
