# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:12:41 2021

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

from collections import Counter 


def Tokenizergenerator(data):
    #label each word and provide a dictionary of the words being used in the sentences
    tokenizer = Tokenizer()    
    tokenizer.fit_on_texts(data)
    return tokenizer
    
def sequence_to_text(list_of_indices):
    # Looking up words in dictionary
    words = [reverse_word_map.get(letter) for letter in list_of_indices]
    return(words)

def remov_duplicates(input): 
  
    # split input string separated by space 
    input = input.split(" ") 
  
    # joins two adjacent elements in iterable way 
    for i in range(0, len(input)): 
        input[i] = "".join(input[i]) 
  
    # now create dictionary using counter method 
    # which will have strings as key and their  
    # frequencies as value 
    UniqW = Counter(input) 
  
    # joins two adjacent elements in iterable way 
    s = " ".join(UniqW.keys()) 
    return s

#load the model that already saved
model=keras.models.load_model('haiku_model')

data_file = open("haiku_dataset.txt","r")

train_sentences = data_file.read()

#make the word not capitalized
train_sentences = train_sentences.lower()

#replace all occurrences of the required string
train_sentences = train_sentences.replace('christmas', 'new year')

#alternative: train_sentences = pd.read_csv(" ")

#split data into lines
train_sentences = train_sentences.splitlines()

tokenizer = Tokenizergenerator(train_sentences)

word_map = tokenizer.word_index.items()

reverse_word_map = dict(map(reversed, tokenizer.word_index.items()))
  
def haiku(Name, Relationship):

    #predicting the text by giving some seed text to choose the category to want
    #warning: the word in the seed_text should be in the training_data's vocabulary
    max_sequence_len = 10
    seed_text_1 = [Name, Relationship]
    #do not forget to import random library
    if seed_text_1[1].lower() == 'family':
    #if seed_text_1[1] == 'True' && seed_text_2[2]== 'True'
        family_1 = ["children with", "new year", "to live","happy and"]
        family_2 = ["the birth", "one year", "everything is","3 generations"]
        family_3 = ["the kitchen","one day","take time","dream","a year","happy"]
        seed_text_r1 = random.choice(family_1) # first option of the seed word for the first example
        seed_text_r2 = random.choice(family_2) # second option of the seed word for the second example
        seed_text_r3 = random.choice(family_3) # third option of the seed word for the third example 
    elif seed_text_1[1].lower() == 'friends':
        friends_1 = ["new year", "happy and","hope is","everything is","time for"]
        friends_2 = ["thank you" ,"our hearts" ,"new morning","time is"]
        friends_3 = ["be careful" ,"happy new", "happy", "when" ,"breathe" ,"with ease"]
        seed_text_r1 = random.choice(friends_1)
        seed_text_r2 = random.choice(friends_2)
        seed_text_r3 = random.choice(friends_3)
    elif seed_text_1[1].lower() == 'romantic':
        romantic_1 = ["happy new","new year","everything is","of dawn","peace love","the night"]
        romantic_2 = ["the new","our hearts","a new","beautiful to"]
        romantic_3 = ["let passion","as","keep","i","like yesterday","to share", "let us"]
        seed_text_r1 = random.choice(romantic_1)
        seed_text_r2 = random.choice(romantic_2)
        seed_text_r3 = random.choice(romantic_3)

     
 #print the first example

    token_list = tokenizer.texts_to_sequences([seed_text_r1])[0]

    lines = 3

    #expand list if you increase the number of lines:

    #Important!!!! first line also includes seed text, so select number of words accordingly

    next_words_per_line = [3,7,5]

    

    #initializing an array for each line and counting how many words there are in eachline

    line_text = ([])

    words_per_line = ([])

    for i in range(lines):

        line_text.append(([]))

        if i == 0:

            words_per_line.append(len(token_list)+next_words_per_line[0])

        else:

            words_per_line.append(next_words_per_line[i])

    word_count = np.sum(next_words_per_line)

    

    #generate prediction

    for word in range(word_count):

        imput = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')

        predicted = int(model.predict_classes(imput,verbose=0))

        token_list.append(predicted)

        

    #arrange output in lines  

    line_count = 0

    word_count = 0

    for words in range(len(token_list)):

        word_count += 1

        if word_count > sum(words_per_line[0:line_count+1]):

            line_count += 1

        line_text[line_count].append(token_list[words])

        


    #translate back to text

    prediction = ([])

    for i in range(len(line_text)):

        prediction.append(sequence_to_text(line_text[i]))

    

    output = ""

    for i in range(lines):

        for j in range(words_per_line[i]):

            if j == 0:

                output = output + prediction[i][j].capitalize()

            else:

                output = output + " " + prediction[i][j]

        output = output + "\n"



    greeting_text = "Dear " + seed_text_1[0] + "," + "\n"

    output = greeting_text + output

    #print(output)

    

    #print the second texts
    token_list = tokenizer.texts_to_sequences([seed_text_r2])[0]

    lines = 3

    #expand list if you increase the number of lines:

    #Important!!!! first line also includes seed text, so select number of words accordingly

    next_words_per_line = [3,7,5]

    

    #initializing an array for each line and counting how many words there are in eachline

    line_text = ([])

    words_per_line = ([])

    for i in range(lines):

        line_text.append(([]))

        if i == 0:

            words_per_line.append(len(token_list)+next_words_per_line[0])

        else:

            words_per_line.append(next_words_per_line[i])

    word_count = np.sum(next_words_per_line)

    

    #generate prediction

    for word in range(word_count):

        imput = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')

        predicted = int(model.predict_classes(imput,verbose=0))

        token_list.append(predicted)

        

    #arrange output in lines  

    line_count = 0

    word_count = 0

    for words in range(len(token_list)):

        word_count += 1

        if word_count > sum(words_per_line[0:line_count+1]):

            line_count += 1

        line_text[line_count].append(token_list[words])
        
    #translate back to text

    prediction = ([])

    for i in range(len(line_text)):

        prediction.append(sequence_to_text(line_text[i]))


    output_2 = ""

    for i in range(lines):

        for j in range(words_per_line[i]):

            if j == 0:

                output_2 = output_2 + prediction[i][j].capitalize()

            else:

                output_2 = output_2 + " " + prediction[i][j]

        output_2 = output_2 + "\n"



    greeting_text_2 = "Dear " + seed_text_1[0] + "," + "\n"

    output_2 = greeting_text_2 + output_2

    #print(output_2)

    

    #print the third texts
    token_list = tokenizer.texts_to_sequences([seed_text_r3])[0]

    lines = 3

    #expand list if you increase the number of lines:

    #Important!!!! first line also includes seed text, so select number of words accordingly

    next_words_per_line = [3,7,5]

    

    #initializing an array for each line and counting how many words there are in eachline

    line_text = ([])

    words_per_line = ([])

    for i in range(lines):

        line_text.append(([]))

        if i == 0:

            words_per_line.append(len(token_list)+next_words_per_line[0])

        else:

            words_per_line.append(next_words_per_line[i])

    word_count = np.sum(next_words_per_line)

    

    #generate prediction

    for word in range(word_count):

        imput = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')

        predicted = int(model.predict_classes(imput,verbose=0))

        token_list.append(predicted)

    #arrange output in lines  

    line_count = 0

    word_count = 0

    for words in range(len(token_list)):

        word_count += 1

        if word_count > sum(words_per_line[0:line_count+1]):

            line_count += 1

        line_text[line_count].append(token_list[words])

    #translate back to text

    prediction = ([])

    for i in range(len(line_text)):

        prediction.append(sequence_to_text(line_text[i]))

    output_3 = ""

    for i in range(lines):

        for j in range(words_per_line[i]):

            if j == 0:

                output_3 = output_3 + prediction[i][j].capitalize()

            else:

                output_3 = output_3 + " " + prediction[i][j]

        output_3 = output_3 + "\n"



    greeting_text_3 = "Dear " + seed_text_1[0] + "," + "\n"

    output_3 = greeting_text_3 + output_3

    return [output, output_2, output_3]


if __name__ == "__main__":
    #example input for testing purposes
    seed_text_1 = ['Alice', 'friends']
    #predict and produce the haiku
    outputs = haiku(seed_text_1[0], seed_text_1[1])
    
    for output in outputs:

        remov_duplicates(output) 
       
        print(output)
