# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 19:31:27 2021

@author: wanal
"""

import tensorflow as tf

from tensorflow import keras

import numpy as np

import random

import re

from tensorflow.keras import Sequential

from tensorflow.keras.layers import Dense

from tensorflow.keras import regularizers

from tensorflow.keras.preprocessing.text import Tokenizer

from tensorflow.keras.preprocessing.sequence import pad_sequences

import string


def Tokenizergenerator(data):
    #label each word and provide a dictionary of the words being used in the sentences
    tokenizer = Tokenizer()    
    tokenizer.fit_on_texts(data)
    return tokenizer

    
    
def sequence_to_text(list_of_indices):
    # Looking up words in dictionary
    words = [reverse_word_map.get(letter) for letter in list_of_indices]
    return(words)

#load the model that already saved
model=keras.models.load_model('text_prosa_model')

data_file = open("text_prosa_greetings2.txt","r")

#solving the problem of unrecoginzed word inside the dataset
train_sentences = data_file.read().replace('\xa0', ' ')

    #make the word not capitalized
train_sentences = train_sentences.lower().split("\n")
    
tokenizer = Tokenizergenerator(train_sentences)

word_map = tokenizer.word_index.items()

reverse_word_map = dict(map(reversed, tokenizer.word_index.items()))

def prosa(Name, Relationship):

    #predicting the text by giving some seed text to choose the category to want
    #warning: the word in the seed_text should be in the training_data's vocabulary
    max_sequence_len = 50
    seed_text_1 = [Name, Relationship]
    #do not forget to import random library
    
    if seed_text_1[1].lower() == 'family':
        family_1 = ["family", "let","may this", "families are","i hope" ]
        family_2 = ["i wish", "years come", "may our family" ,"cheers to"]
        family_3 = ["to my" ,"happy new year", "hope this" ,"as i look"]
        seed_text_r1 = random.choice(family_1) # first option of the seed word for the first example
        seed_text_r2 = random.choice(family_2) # second option of the seed word for the second example
        seed_text_r3 = random.choice(family_3) # third option of the seed word for the third example 
    elif seed_text_1[1].lower() == 'friends':
        friends_1 = ["wishing you", "true friendship","every year", "remember when"]
        friends_2 = ["i wish", "gather friends", "genuine friendship", "happy new year"]
        friends_3 = ["may you", "thank you", "to my" ,"friend"]
        seed_text_r1 = random.choice(friends_1)
        seed_text_r2 = random.choice(friends_2)
        seed_text_r3 = random.choice(friends_3)
    elif seed_text_1[1].lower() == 'romantic':
        romantic_1 = ["my love" ,"darling", "babe", "my princess", "wishing the happiest" ]
        romantic_2 = ["billion" ,"love" ,"happy new year" ,"you are the most" ]
        romantic_3 = ["i want" ,"starting another year with you", " to the" ,"to my"]
        seed_text_r1 = random.choice(romantic_1)
        seed_text_r2 = random.choice(romantic_2)
        seed_text_r3 = random.choice(romantic_3)
    elif seed_text_1[1].lower() == 'colleagues':
        colleagues_1 = ["we are wishing you all","happy holidays","wishing you","thank you"  ]
        colleagues_2 = ["wish you and your family","your support","we want to","cheers to the"]
        colleagues_3 = ["wish you","happy new year","have a joyous holiday","may this new year"]
        seed_text_r1 = random.choice(colleagues_1)
        seed_text_r2 = random.choice(colleagues_2)
        seed_text_r3 = random.choice(colleagues_3)
  
#frist print and predict
   
    token_list = tokenizer.texts_to_sequences([seed_text_r1])[0]
    next_words = 15
    
    for word in range(next_words):
        input = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')
        predicted = int(model.predict_classes(input, verbose=0))
        token_list.append(predicted)
    prediction = sequence_to_text(token_list)

    prediction_string = ""
    for i in prediction:
                prediction_string += i + " "
    prediction_string_1 = prediction_string[:-1].capitalize() + '. Happy New Year!'
    greeting_text_1 ="Dear " + seed_text_1[0] + "," + "\n"
    output = greeting_text_1 + prediction_string_1

#second print
    
    token_list = tokenizer.texts_to_sequences([seed_text_r2])[0]
    next_words = 15

    for word in range(next_words):
        input = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')
        predicted = int(model.predict_classes(input, verbose=0))
        token_list.append(predicted)
    prediction = sequence_to_text(token_list)

 
    prediction_string = ""
    for i in prediction:
                prediction_string += i + " "
    prediction_string_2 = prediction_string[:-1].capitalize() + '. Happy New Year!'
    greeting_text_2 ="Dear " + seed_text_1[0] + "," + "\n"
    output_2 = greeting_text_2 + prediction_string_2

    

#third print
    token_list = tokenizer.texts_to_sequences([seed_text_r3])[0]
    next_words = 15

    for word in range(next_words):
        input = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')
        predicted = int(model.predict_classes(input, verbose=0))
        token_list.append(predicted)
    prediction = sequence_to_text(token_list)

    prediction_string = ""
    for i in prediction:
                prediction_string += i + " "
    prediction_string_3 = prediction_string[:-1].capitalize() + '. Happy New Year!'
    greeting_text_3 ="Dear " + seed_text_1[0] + "," + "\n"
    output_3 = greeting_text_3 + prediction_string_3

    
    return [output, output_2, output_3]


if __name__ == "__main__":
    #example inupt for testing purposes
    seed_text_1 = ['Alice', 'friends']
    
    #alternative: seed_text_1 = pd.read_csv(" ")
    
    #predict and produce the prosa
    outputs = prosa(seed_text_1[0], seed_text_1[1])
    
    for output in outputs:

        print(output)
