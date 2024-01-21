import argparse
import os
import re
import nltk
import matplotlib.pyplot as plt
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Argument Parser (referenced https://thepythoncode.com/article/how-to-use-argparse-in-python for documentation)
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

# removes all punctuation (referenced https://www.geeksforgeeks.org/python-remove-punctuation-from-string/)
if args.punct_rem:
    file = re.sub(r'[^\w\s]', '', file)

# removes all stopwords
if args.stop_rem:
    tempList = file.split()
    filteredWords = [tempList for tempList in tempList if tempList.lower() not in stopWords]
    file = (' '.join(filteredWords))

# lemmatization of each token (referenced
# https://www.geeksforgeeks.org/python-lemmatization-approaches-with-examples/ for different examples)
if args.lemma:
    tempList = file.split()
    lemma = [lemmatizer.lemmatize(tempList) for tempList in tempList]
    file = (' '.join(lemma))

words = nltk.word_tokenize(file)
frequency = nltk.FreqDist(words)

# prints tokens and their corresponding frequency (referenced https://datagy.io/python-read-text-file/ documentation)
with open('output.txt', 'w', encoding='utf-8') as f:
    for token, freq in frequency.most_common():
        f.write(f'{token} {freq}\n')

os.system(f'start {'output.txt'}')


# creates the graph (utilized https://copilot.microsoft.com to locate matplotlib documentation)
xValues = [token for token, freq in frequency.most_common()]
yValues = [freq for token, freq in frequency.most_common()]
plt.plot(np.arange(len(xValues)), yValues)
plt.title("Token Frequency Distribution")
plt.xlabel("Tokens")
plt.ylabel("Frequency")
plt.yscale('log')
plt.show()
