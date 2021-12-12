# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 19:31:27 2021

@author: wanal
"""

import tensorflow as tf

from tensorflow import keras

import numpy as np

import random


from tensorflow.keras import Sequential

from tensorflow.keras.layers import Dense

from tensorflow.keras import regularizers

from tensorflow.keras.preprocessing.text import Tokenizer

from tensorflow.keras.preprocessing.sequence import pad_sequences



def Tokenizergenerator(data):

    tokenizer = Tokenizer()    
    tokenizer.fit_on_texts(data)
    return tokenizer

    #encoding input and ouput sentences
    
    
def sequence_to_text(list_of_indices):

    # Looking up words in dictionary
    words = [reverse_word_map.get(letter) for letter in list_of_indices]
    return(words)


# defines basic rules for grammar and punctuation
def rules(string):
    new_string = ""
    string = string.replace(".,", ",")
    string = string[1:].capitalize()
    i = string.count(".")
    for i in range(i):
        n = string.index(".")
        if string[n+2:n+5] == "and":
            new_string += string[:n] + ","
            string = string[n + 1:]
        else:
            new_string += string[:n + 1] + " "
            string = string[n+2:]
            string = string.capitalize()

    new_string = new_string.replace("i ", "I ")
    new_string = new_string.replace("i'", "I'")
    new_string = new_string.replace("god", "God")
    return new_string

#loading the pretrained model

model = keras.models.load_model('prosa_withoutcategories_model')


data_file = open("prosa_greetings_without_categories.txt","r")

train_sentences = data_file.read()


#split data
train_sentences = train_sentences.lower().split("/")

tokenizer = Tokenizergenerator(train_sentences)

word_map = tokenizer.word_index.items()

reverse_word_map = dict(map(reversed, tokenizer.word_index.items()))

def prosa_sentence(Name):

    #predicting the text by giving some seed text to choose the category to want
    #warning: the word in the seed_text should be in the training_data's vocabulary
    max_sequence_len = 10
    seed_text_1 = [Name]
    #do not forget to import random library
    seed_text_r1 = "happy new"
    #frist print
   
    token_list = tokenizer.texts_to_sequences([seed_text_r1])[0]
    next_sentences = 15

    for word in range(next_sentences):
        input = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')
        predicted = int(model.predict_classes(input, verbose=0))
        token_list.append(predicted)
    prediction = sequence_to_text(token_list)

    # apply rules for punctuation and grammar, remove repeating parts
    prediction = list(dict.fromkeys(prediction))
    next_sentences_new = len(prediction)

    # initializing three empty strings for three predictions
    prediction_string_1 = ""
    prediction_string_2 = ""
    prediction_string_3 = ""
    nonBreakSpace = u'\xa0'

    # produce 15 outputs in order to get three different versions

    # first prediction
    for i in prediction[:int(next_sentences_new/3)]:
        if not ("happy" in i and "new" in i and "year" in i):
            i = i.replace(nonBreakSpace, ' ')
            if i.count(" ") == 1:
                prediction_string_1 += "," + i + "."
            else:
                prediction_string_1 += i + "."

    prediction = prediction[int(next_sentences_new / 3):]

    # second prediction
    for i in prediction[:int(next_sentences_new/3)]:
        if not ("happy" in i and "new" in i and "year" in i):
            i = i.replace(nonBreakSpace, ' ')
            if i.count(" ") == 1:
                prediction_string_2 += "," + i + "."
            else:
                prediction_string_2 += i + "."
    prediction = prediction[int(next_sentences_new / 3):]

    #  third prediction
    for i in prediction:
        if not ("happy" in i and "new" in i and "year" in i):
            i = i.replace(nonBreakSpace, ' ')
            if i.count(" ") == 1:
                prediction_string_3 += "," + i + "."
            else:
                prediction_string_3 += i + "."

    # applying other grammar rules
    prediction_string_1 = rules(prediction_string_1)
    prediction_string_2 = rules(prediction_string_2)
    prediction_string_3 = rules(prediction_string_3)

    # generating nice output, with name and ending
    greeting_text ="Dear " + seed_text_1[0].capitalize() + "," + "\n"
    output_1 = greeting_text + prediction_string_1 + 'Happy New Year!'
    output_2 = greeting_text + prediction_string_2 + 'Happy New Year!'
    output_3 = greeting_text + prediction_string_3 + 'Happy New Year!'
    
    return [output_1, output_2, output_3]
    

if __name__ == "__main__":
    #example input for testing purposes
    seed_text_1 = ['Alice', 'friends']

    outputs = prosa_sentence(seed_text_1[0])
    
    for output in outputs:

        print(output)
