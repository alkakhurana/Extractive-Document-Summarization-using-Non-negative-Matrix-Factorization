# import commands
import nltk
import string
import textmining
import os
import csv
import math
import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import tokenize
from nltk.corpus import stopwords
from sklearn.decomposition import NMF


summary_length = 100

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

        return(words_count,len(sentences_backup),sentences)

def create_summary(inputFile,f_name,comp_rate):
        termSentFile = ".\\Pre_Processed\\"+f_name.replace('.txt','')+".csv"
        data = np.genfromtxt(termSentFile, dtype='float64', delimiter=',', names=None)
        A = np.asarray(data,dtype = 'float64')

        A_sum=0.0

        for i in range(A.shape[0]):
                for j in range(A.shape[1]):
                        A_sum += A[i][j]

        for i in range(A.shape[0]):
                for j in range(A.shape[1]):
                        if(A[i][j]!=0):
                                A[i][j]=1.0
        
        [words_count,no_of_sentences,sentences] = preprocess(inputFile,f_name)

        ## Number of topics
        k=  math.ceil(no_of_sentences * A.shape[0]/A_sum)
        
        model = NMF(n_components=k, init='nndsvd')
        W = model.fit_transform(A)
        H= model.components_

        
        W_sum = 0.0
        for i in range(W.shape[0]):
                for j in range(W.shape[1]):
                        W_sum = W_sum + W[i][j]
        W_sum_cols = np.sum(W, axis =0)
        
        topic_imp = np.zeros(k,dtype='float64')
        for i in range(0,k):
                topic_imp[i] = W_sum_cols[i]/W_sum


        sentence_score = np.zeros(no_of_sentences,dtype = 'float64')
        for i in range(no_of_sentences):
                score = 0.0
                for j in range(0,k):
                    score = score + H[j][i]*topic_imp[j]
                sentence_score[i]= score

        x = sentence_score.argsort()
        
        temp_ranks = np.zeros(no_of_sentences,dtype = int)
        for j in range(len(sentences)):
                temp_ranks[x[j]]=len(sentences)-j

        name = ".\\Summaries\\"+"system1_"+f_name
        file_object = open(name,"w")
        words=0
        for i in range(1,no_of_sentences+1):
            for j in range(no_of_sentences):
                if(temp_ranks[j] == i):
                        if(words < summary_length):
                            words = words + len(word_tokenize(strip_punctuation(sentences[j])))
                            file_object.write(sentences[j].replace('\n',' '))
                            file_object.write('\n')
        file_object.close()



os.chdir("\\path to working directory")
for f in os.listdir(".\\Documents"):
    print(f)
    inputFile = ".\\Documents\\"+f
    create_summary(inputFile,f,3)

