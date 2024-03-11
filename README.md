The code is trained with a corpus of words that are cleaned to remove irrelevant characters like numbers.
We then try to correct these words by comparing the Levenshtein distance between the selected word and the dictionary. If the word exists, we ignore it, if not it is replaced by the word with the lowest Levenshtein distance
