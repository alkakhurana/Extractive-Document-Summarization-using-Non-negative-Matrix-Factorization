import os
import csv
import string
import textmining
import numpy as np
import nltk
from nltk import tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords


#Removing Punctuation
def strip_punctuation(s):
        table = str.maketrans({key: None for key in string.punctuation})
        return s.translate(table)


def preprocess(inputFile,f_name):
        
        # Read the text file
        file = open(inputFile, 'r')
        
        text = file.read()      
        
        text = text.replace('\n',' ')

        #Number of words in the text
        words_count = len(word_tokenize(strip_punctuation(text)))
  
        # split in to sentences and store the sentences in a list
        sentences = tokenize.sent_tokenize(text)
        
        #Original Sentences
        sentences_backup = list(sentences)
        
        
        filtered_sentences = []

        
        # Apply stop word removal to each sentence
        stop_words = set(stopwords.words('english'))
            
        for i in range(len(sentences_backup)):
            temp = []
            word_tokens = word_tokenize(strip_punctuation(sentences_backup[i]))
            for w in word_tokens:
                if w.lower() not in stop_words:
                    temp.append(w.lower())
            filtered_sentences.append(temp)

        tdm = textmining.TermDocumentMatrix()
        for i in range(len(sentences)):
            sent = " ".join(filtered_sentences[i])
            tdm.add_doc(sent)
        
        temp = list(tdm.rows(cutoff=1))
        vocab = tuple(temp[0])
        
        X = np.array(temp[1:],dtype = 'float64')
        X1 = X.transpose()

        
        fileObj = ".\\Pre_Processed\\"+f_name.replace('.txt','')+".csv"
        np.savetxt(fileObj, X1, fmt='%1.5f', delimiter=",")
        vocab1 = tuple(zip(vocab))

os.chdir("\\path to working directory")
for f in os.listdir(".\\Documents"):
    inputFile = ".\\Documents\\"+f
    preprocess(inputFile,f)
