The code is trained with a corpus of words that are cleaned(Using Regular Expressions) to remove irrelevant characters like numbers.
We require the user to input a .txt file containing strings
If all the words in the string are correct, no corrections are made
If the input contains incorrect(i.e. it does not exist in the corpus) word(s), Then we check the lowest edit distance from each incorrect word(s) to the words in the corpus
The program outputs a .txt file with the predicted correct words.

Loading a corpus:
Any file named 'corpus.txt' that exists in the directory of the program can be loaded as a corpus. This allows for changing allowed words and specialized contexts

Input File:
The program will ask for the name of the input file(without adding '.txt' 
Any .txt file containing strings will be taken by the program, as long as it exits in the same directory as the Spellechecker.py file.

Output:
The output is stored in a file called 'output.txt'

Run the program with python Spellchecker.py
![image](https://github.com/Sreyanth99/Python-Spelling-Correction/assets/6060592/2a5f9fee-2fd8-42cb-b5a1-b6a41ca064f2)

![image](https://github.com/Sreyanth99/Python-Spelling-Correction/assets/6060592/78a4dc95-bb59-4f55-8c12-da614e768f5e)

Output

![image](https://github.com/Sreyanth99/Python-Spelling-Correction/assets/6060592/2f6e8e99-d331-4ca3-9a42-31492371dfeb)
