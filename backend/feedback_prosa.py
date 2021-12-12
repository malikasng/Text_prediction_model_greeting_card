import tensorflow as tf

from tensorflow import keras

import numpy as np

import random

import re

import os

# import pandas as pd

from tensorflow.keras import Sequential

from tensorflow.keras.layers import Dense

from tensorflow.keras import regularizers

from tensorflow.keras.preprocessing.text import Tokenizer

from tensorflow.keras.preprocessing.sequence import pad_sequences

from tensorflow.keras.models import load_model

import string


def Tokenizergenerator(data):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(data)
    return tokenizer

    # encoding input and ouput sentences


def sequence_to_text(list_of_indices):
    # Looking up words in dictionary
    words = [reverse_word_map.get(letter) for letter in list_of_indices]
    return (words)


data_file = open(r"text_prosa_greetings2.txt", "r")

train_sentences = data_file.read().replace('\xa0', ' ')

train_sentences = train_sentences.lower().split("/")

tokenizer = Tokenizergenerator(train_sentences)

input_sequences = []

for line in train_sentences:

    token_list = tokenizer.texts_to_sequences([line])[0]

    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i + 1]

        input_sequences.append(n_gram_sequence)

max_sequence_len = max([len(x) for x in input_sequences])

input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))

xs = input_sequences[:, :-1]

labels = input_sequences[:, -1]

total_words = len(tokenizer.word_index) + 1

# ys = tf.keras.utils.to_categorical(labels, num_classes=total_words)

word_map = tokenizer.word_index.items()

reverse_word_map = dict(map(reversed, tokenizer.word_index.items()))

model = load_model('text_prosa_model')

'''checkpoint_path_prosa = "training_4/cp.ckpt"

model = Sequential()
model.add(tf.keras.layers.Embedding(total_words,100,input_length = max_sequence_len-1))
model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(150)))
model.add(Dense(total_words,activation='softmax'))
adam = keras.optimizers.Adam(lr=0.01)
model.compile(loss='categorical_crossentropy',optimizer=adam,metrics=['accuracy'])

model.load_weights(checkpoint_path_prosa)'''


def prosa(Name, Relationship):
    # predicting the text by giving some seed text to choose the category to want
    # warning: the word in the seed_text should be in the training_data's vocabulary
    max_sequence_len = 50
    seed_text_1 = ["George", "family"]
    # do not forget to import random library

    if seed_text_1[1] == 'family':
        family_1 = ["family", "let", "may this", "families are", "i hope"]
        family_2 = ["i wish", "years come", "may our family", "cheers to"]
        family_3 = ["to my", "happy new year", "hope this", "as i look"]
        seed_text_r1 = random.choice(family_1)  # first option of the seed word for the first example
        seed_text_r2 = random.choice(family_2)  # second option of the seed word for the second example
        seed_text_r3 = random.choice(family_3)  # third option of the seed word for the third example
    elif seed_text_1[1] == 'friends':
        friends_1 = ["wishing you", "true friendship", "every year", "remember when"]
        friends_2 = ["i wish", "gather friends", "genuine friendship", "happy new year"]
        friends_3 = ["may you", "thank you", "to my", "friend"]
        seed_text_r1 = random.choice(friends_1)
        seed_text_r2 = random.choice(friends_2)
        seed_text_r3 = random.choice(friends_3)
    elif seed_text_1[1] == 'romantic':
        romantic_1 = ["my love", "darling", "babe", "my princess", "wishing the happiest"]
        romantic_2 = ["billion", "love", "happy new year", "you are the most"]
        romantic_3 = ["i want", "starting another year with you", " to the", "to my"]
        seed_text_r1 = random.choice(romantic_1)
        seed_text_r2 = random.choice(romantic_2)
        seed_text_r3 = random.choice(romantic_3)
    elif seed_text_1[1] == 'colleagues':
        colleagues_1 = ["we are wishing you all", "happy holidays", "wishing you", "thank you"]
        colleagues_2 = ["wish you and your family", "your support", "we want to", "cheers to the"]
        colleagues_3 = ["wish you", "happy new year", "have a joyous holiday", "may this new year"]
        seed_text_r1 = random.choice(colleagues_1)
        seed_text_r2 = random.choice(colleagues_2)
        seed_text_r3 = random.choice(colleagues_3)

    # frist print

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
    greeting_text_1 = "Dear " + seed_text_1[0] + "," + "\n"
    output = greeting_text_1 + prediction_string_1

    # second print

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
    greeting_text_2 = "Dear " + seed_text_1[0] + "," + "\n"
    output_2 = greeting_text_2 + prediction_string_2

    # second print
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
    greeting_text_3 = "Dear " + seed_text_1[0] + "," + "\n"
    output_3 = greeting_text_3 + prediction_string_3

    return [output, output_2, output_3]


# model=keras.models.load_model('C:/Users/wanal/Desktop')

# alternative: train_sentences = pd.read_csv(" ")

# split data


def feedbackProsa(feedback, new_line):
    # satisfied=input("Are you satisfied?")
    if feedback == "feedback":
        # sentence=input("How would you change the printed sentence?")
        with open("Prosa_greetings2.txt", "a+") as add_greeting:
            add_greeting.write(new_line)
            add_greeting.write("/")
            add_greeting.write("\n")
        with open("Prosa_greetings2.txt", "r") as file:
            file_content = file.read().replace('\xa0', ' ')  # Saving the writen sentence to a seperate file.
            sentences = file_content.count('/')

        if sentences >= 50:
            with open("Prosa_greetings2.txt", "r") as add:  ###################################################
                data = add.read()  # Merging the temporary data file to the original.
                #
            with open("text_prosa_greetings2.txt", "a+") as dataset:  #
                #
                dataset.write('\n')  #
                dataset.write(data)
                dataset.close()

            data_file = open(r"text_prosa_greetings2.txt", "r")
            train_sentences = data_file.read().replace('\xa0', ' ')
            train_sentences = train_sentences.lower().split("/")
            tokenizer = Tokenizergenerator(train_sentences)
            # encoding input and ouput sentences
            input_sequences = []
            for line in train_sentences:
                token_list = tokenizer.texts_to_sequences([line])[0]
                for i in range(1, len(token_list)):
                    n_gram_sequence = token_list[:i + 1]
                    input_sequences.append(n_gram_sequence)
            max_sequence_len = max([len(x) for x in input_sequences])
            input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))
            xs = input_sequences[:, :-1]
            labels = input_sequences[:, -1]
            total_words = len(tokenizer.word_index) + 1
            ys = tf.keras.utils.to_categorical(labels, num_classes=total_words)

            '''checkpoint_path_prosa = "training_4/cp.ckpt"
            checkpoint_dir = os.path.dirname(checkpoint_path_prosa)
            cp_callback_prosa = tf.keras.callbacks.ModelCheckpoint(
                    filepath=checkpoint_path_prosa, save_weights_only=True,
                    monitor='loss',
                    mode='min',
                    save_best_only=True)

            model = Sequential()
            model.add(tf.keras.layers.Embedding(total_words,100,input_length = max_sequence_len-1))
            model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(150)))
            model.add(Dense(total_words,activation='softmax'))
            adam = keras.optimizers.Adam(lr=0.01)
            model.compile(loss='categorical_crossentropy',optimizer=adam,metrics=['accuracy'])'''
            model = load_model('text_prosa_model')

            model.fit(xs, ys, epochs=15, batch_size=30, verbose=1)  # Retraining the model based on the
            # merged dataset.

            f = open('Prosa_greetings2.txt', 'r+')  # Deleting the temporary save of the added sentences
            f.truncate(0)  #


if __name__ == "__main__":

    # seed_file = open(r"Prosa_greetings2.txt","r")

    # seeds = seed_file.read()
    #
    # seed_text_1 = seeds.lower().split("/")
    # alternative: seed_text_1 = pd.read_csv(" ")

    outputs = prosa("George", "family")

    for output in outputs:
        print(output)

    feedbackProsa("feedback", "new sentence")
