# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 19:28:41 2021

@author: wanal
"""

import tensorflow as tf

from tensorflow import keras

import numpy as np

import random

#import re

#import pandas as pd

from tensorflow.keras import Sequential

from tensorflow.keras.layers import Dense

from tensorflow.keras import regularizers

from tensorflow.keras.preprocessing.text import Tokenizer

from tensorflow.keras.preprocessing.sequence import pad_sequences

def Tokenizergenerator(data):
    #label each word and provide a dictionary of the words being used in the sentences
    tokenizer = Tokenizer()    
    tokenizer.fit_on_texts(data)
    return tokenizer

def sequence_to_text(list_of_indices):
    # Looking up words in dictionary
    words = [reverse_word_map.get(letter) for letter in list_of_indices]
    return(words)


def model():
    #set up training model
    model = Sequential()
    model.add(tf.keras.layers.Embedding(total_words,100,input_length = max_sequence_len-1))
    model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(150)))
    model.add(Dense(total_words,activation='softmax'))
    adam = keras.optimizers.Adam(lr=0.01)
    model.compile(loss='categorical_crossentropy',optimizer=adam,metrics=['accuracy'])
    history=model.fit(xs,ys,epochs=100,verbose=1)
    return history,model


if __name__ == "__main__":
    
    #load data set and prepare format:
    #data_path = "C:/Users/wanal/Desktop/groupproject/Prosa_greetings2.txt"
    
    data_file = open('text_prosa_greetings2.txt')
    
    #solving the problem of unrecoginzed word inside the dataset
    train_sentences = data_file.read().replace('\xa0', ' ')
    
    train_sentences = train_sentences.lower().split("\n")
    
    #alternative: train_sentences = pd.read_csv(" ")
    #add punctuations
    
    tokenizer = Tokenizergenerator(train_sentences)
    #encoding input and ouput sentences
    
    input_sequences = []
    
    for line in train_sentences:
    
        token_list = tokenizer.texts_to_sequences([line])[0]
    
        for i in range(1,len(token_list)):
    
            n_gram_sequence = token_list [:i+1]
    
            input_sequences.append(n_gram_sequence)
    
    max_sequence_len = max([len(x)for x in input_sequences])
    
    input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len,padding='pre'))
    
    xs = input_sequences[:,:-1]
    
    labels = input_sequences[:,-1]
    
    total_words = len(tokenizer.word_index)+1
    
    ys = tf.keras.utils.to_categorical(labels, num_classes=total_words) 
    
    
    #print(xs)
    
    #print(labels)
    
    #print(ys)
    
    history,model=model()
    word_map = tokenizer.word_index.items()
    
    reverse_word_map = dict(map(reversed, tokenizer.word_index.items()))
    model.save('./text_prosa_model')

