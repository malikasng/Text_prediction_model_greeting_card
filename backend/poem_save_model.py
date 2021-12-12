# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 08:15:10 2021

@author: wanal
"""


import tensorflow as tf

from tensorflow import keras

import numpy as np

import os

import random

#import pandas as pd

from tensorflow.keras import Sequential

from tensorflow.keras.layers import Dense

from tensorflow.keras import regularizers

from tensorflow.keras.preprocessing.text import Tokenizer

from tensorflow.keras.preprocessing.sequence import pad_sequences

def Tokenizergenerator(data):

    tokenizer = Tokenizer()    
    tokenizer.fit_on_texts(data)
    return tokenizer

def sequence_to_text(list_of_indices):

    # Looking up words in dictionary
    words = [reverse_word_map.get(letter) for letter in list_of_indices]
    return(words)


def model():

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

#load data set and prepare format:

#data_path = "Poems_New_Years.txt"

data_file = open('Poems_New_Years.txt')
#current_path = os.path.dirname(__file__)
#rain_sentences = os.path.join(current_path, 'Poems_New_Years.txt')

train_sentences = data_file.read()

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


history,model=model()
word_map = tokenizer.word_index.items()

reverse_word_map = dict(map(reversed, tokenizer.word_index.items()))

model.save("./poem_model")


