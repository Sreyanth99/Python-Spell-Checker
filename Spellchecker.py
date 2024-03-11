
#Spell checker
#Sreyanth Akella 002341544
#Tasks:
# Data cleaning
# Corpus Preparation
# Deletion
# Replacement
# Transposition
# Insertion


#import needed modules
import os
from nltk import word_tokenize
from collections import Counter
import itertools
import nltk
import re
import time
nltk.download('punkt')

#We start timer as soon as modules are loaded
start = time.time()

#Load the corpus
filename = 'corpus.txt'
file = open(filename, 'rt')
corpus = file.read()
file.close()

#1)We will clean the corpus using regular expressions
#2)We tokenize the words using word tokenizer from NLTK.
tokens = corpus
tokens = re.compile("[^a-zA-Z'-]")
tokens = word_tokenize(corpus)
unique = set()
final_tokens = []
for item in tokens:  
    if item not in unique:
        unique.add(item)
        final_tokens.append(item.lower())
corpus_words = [word.lower() for word in final_tokens]





#calculate frequencies using Counter from collections
corpus_words = Counter(corpus_words)




#Spell checker function
# Performs the following tasks:
#  Replacement: Checks to see if a word has a wrong letter
#  Deletion: Checks for missing letters
#  Insertion: Checks to see if an extra letter is present erroneously
#  Transposition: Checks for swapped letters
# Levenshtein distance is calculated between corpus words and input word
# this performs required insertion, deletion, transposition and replacement
# corrections.

def levenshtein_distance(str1, str2):
    if len(str1) > len(str2):
        str1, str2 = str2, str1

    dist = range(len(str1) + 1)
    for i2, char2 in enumerate(str2):
        dist2 = [i2+1]
        for i1, char1 in enumerate(str1):
            if char1 == char2:
                dist2.append(dist[i1])
            else:
                dist2.append(1 + min((dist[i1], dist[i1 + 1], dist2[-1])))
        dist = dist2
    return dist[-1]

#Spellcheck procedure:
#checks whether word exists in corpus and calculates levenshtein distance
#between the input word and corpus word. It appends the distances into an array
#The word from corpus with the smallest levenshtein distance is selected.
#The selected word will then replace the incorrectly spelled input word

def spellcheck(input_words):
    for j,word in enumerate(input_words):
        if (word not in list(corpus_words.keys()) and not word.isnumeric()): # ignore digits and Roman numerals
            levdists = []
            for c_word in list(corpus_words.keys()):
                levdists.append(levenshtein_distance(word,c_word))
            input_words[j] = list(corpus_words.keys())[levdists.index(min(levdists))]
        else:
            input_words[j] = word
    return ' '.join(input_words)



#Load file with input words.
text = input('Enter Filename [Without .txt]: ')
file = open(text+'.txt', 'rt')
input_text = file.read()
file.close()



#tokenize the input using a word tokenizer
input_words = word_tokenize(input_text)
for i,word in enumerate(input_words):
    input_words[i]=word.lower()
print("Given words are",input_words)
final_sentence = spellcheck(input_words)


#Write out the corrected sentence to a file
output = open('output.txt', 'w')
output.write(final_sentence)
output.close()
print("Output has been saved to file 'output.txt'")

#documenting the time it took to run
stop = time.time()
Total_Time = stop-start
print("Total time taken for execution(in seconds) is:",Total_Time)





