# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:03:58 2021

@author: wanal
"""

import tensorflow as tf

from tensorflow import keras

import numpy as np

import random

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
    #build up a training model
   model = Sequential()
   model.add(keras.layers.Embedding(total_words, 100, input_length=max_sequence_len-1))
   model.add(keras.layers.Bidirectional(keras.layers.LSTM(150, return_sequences = True)))
   model.add(keras.layers.Dropout(0.2))
   model.add(keras.layers.LSTM(100))
   model.add(Dense(total_words/2, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
   model.add(Dense(total_words, activation='softmax'))
   model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
   history=model.fit(xs,ys,epochs=500,verbose=1)
   return history,model

if __name__ == "__main__":

    #upload the training data
    #data_path = "C:/Users/wanal/Desktop/Haiku.txt"
    
    data_file = open('haiku_dataset.txt')
    
    train_sentences = data_file.read()
    
    #make the word not capitalized
    train_sentences = train_sentences.lower()
    
    #replace all occurrences of the required string
    train_sentences = train_sentences.replace('christmas', 'new year')
    
    #alternative: train_sentences = pd.read_csv(" ")
    
    #split data into lines
    train_sentences = train_sentences.splitlines()
    
    #start empty string, this part is to let the machine train to understand between verses and the end of poem
    poems = ""
    
    for line in train_sentences:
    
        if line[-1] != '/':
    
            poems = poems + line + " endofline "
    
        elif line[-1] == '/':
    
            poems = poems + line[0:-1] + " endofpoem"
    
    poems = poems.lower().split("endofpoem")
    
    
    #label sentences
    tokenizer = Tokenizergenerator(poems)
    
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
    
    #call the training model
    history,model=model()
    
    #view what the individual words have been numbered or tokenized
    word_map = tokenizer.word_index.items()
    
    #decode the words
    reverse_word_map = dict(map(reversed, tokenizer.word_index.items()))
    
    #save the model
    model.save('./haiku_model')
