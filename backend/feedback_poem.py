import tensorflow as tf

from tensorflow import keras

import numpy as np

import random

import os

# import pandas as pd

from tensorflow.keras import Sequential

from tensorflow.keras.layers import Dense

from tensorflow.keras import regularizers

from tensorflow.keras.preprocessing.text import Tokenizer

from tensorflow.keras.preprocessing.sequence import pad_sequences

from tensorflow.keras.models import load_model


# alternative: train_sentences = pd.read_csv(" ")

# split data into lines


def Tokenizergenerator(data):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(data)
    return tokenizer


# Separate lines and each poem
# poems = ""
#
# for line in train_sentences:
#
#    if line[-1] != '/':
#
#        poems = poems + line + " endofline "
#
#    elif line[-1] == '/':
#
#        poems = poems + line[0:-1] + " endofpoem"
#
# poems = poems.lower().split("endofpoem")

data_file = open(r"Poems_New_Years.txt", "r")

train_sentences = data_file.read().replace('\xa0', ' ')

# alternative: train_sentences = pd.read_csv(" ")

# split data into lines

train_sentences = train_sentences.splitlines()

# start empty string, this part is to let the machine train to understand between verses and the end of poem

poems = ""

for line in train_sentences:

    if line[-1] != '/':

        poems = poems + line + " endofline "

    elif line[-1] == '/':

        poems = poems + line[0:-1] + " endofpoem"

poems = poems.lower().split("endofpoem")

tokenizer = Tokenizergenerator(poems)

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

# tokenizer = Tokenizergenerator(poems)
#
#
word_map = tokenizer.word_index.items()
#
reverse_word_map = dict(map(reversed, tokenizer.word_index.items()))


def sequence_to_text(list_of_indices):
    # Looking up words in dictionary
    words = [reverse_word_map.get(letter) for letter in list_of_indices]
    return (words)


seed_text_r1 = ""
seed_text_r2 = ""
seed_text_r3 = ""


def poet(Name, Relationship):
    # predicting the text by giving some seed text to choose the category to want
    # warning: the word in the seed_text should be in the training_data's vocabulary
    max_sequence_len = 15
    seed_text_1 = [Name, Relationship]
    # do not forget to import random library

    global seed_text_r1
    global seed_text_r2
    global seed_text_r3

    if seed_text_1[1] == 'Family':

        family_1 = ["appreciate", "care", "calm", "children"]

        family_2 = ["family", "happiness", "pray", "happy"]

        family_3 = ["hugs", "health", "beatiful", "dream"]

        seed_text_r1 = random.choice(family_1)  # first option of the seed word for the first example

        seed_text_r2 = random.choice(family_2)  # second option of the seed word for the second example

        seed_text_r3 = random.choice(family_3)  # third option of the seed word for the third example

    elif seed_text_1[1] == 'Friends':

        friends_1 = ["old", "embrace", "friend", "forget"]

        friends_2 = ["friendship", "studies", "hugs", "live"]

        friends_3 = ["enjoy", "help", "learn", "feel"]

        seed_text_r1 = random.choice(friends_1)

        seed_text_r2 = random.choice(friends_2)

        seed_text_r3 = random.choice(friends_3)

    elif seed_text_1[1] == 'Romantic':

        romantic_1 = ["kisses", "love", "sweet", "flowers"]

        romantic_2 = ["girlfriends", "boyfriends", "protect", "hug"]

        romantic_3 = ["hand", "valentine", "happy", "restore"]

        seed_text_r1 = random.choice(romantic_1)

        seed_text_r2 = random.choice(romantic_2)

        seed_text_r3 = random.choice(romantic_3)

    # print the first example

    token_list = tokenizer.texts_to_sequences([seed_text_r1])[0]

    lines = 4

    # expand list if you increase the number of lines:

    # Important!!!! first line also includes seed text, so select number of words accordingly

    next_words_per_line = [4, 5, 5, 5]

    # initializing an array for each line and counting how many words there are in eachline

    line_text = ([])

    words_per_line = ([])

    for i in range(lines):

        line_text.append(([]))

        if i == 0:

            words_per_line.append(len(token_list) + next_words_per_line[0])

        else:

            words_per_line.append(next_words_per_line[i])

    word_count = np.sum(next_words_per_line)

    # generate prediction

    for word in range(word_count):
        imput = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')

        predicted = int(model.predict_classes(imput, verbose=0))

        token_list.append(predicted)

    # arrange output in lines

    line_count = 0

    word_count = 0

    for words in range(len(token_list)):

        word_count += 1

        if word_count > sum(words_per_line[0:line_count + 1]):
            line_count += 1

        line_text[line_count].append(token_list[words])

    # translate back to text

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

    greeting_text = "Dear " + seed_text_1[0] + ":" + "\n"

    output = greeting_text + output

    # print(output)

    # print the second texts

    token_list = tokenizer.texts_to_sequences([seed_text_r2])[0]

    lines = 4

    # expand list if you increase the number of lines:

    # Important!!!! first line also includes seed text, so select number of words accordingly

    next_words_per_line = [4, 5, 5, 5]

    # initializing an array for each line and counting how many words there are in eachline

    line_text = ([])

    words_per_line = ([])

    for i in range(lines):

        line_text.append(([]))

        if i == 0:

            words_per_line.append(len(token_list) + next_words_per_line[0])

        else:

            words_per_line.append(next_words_per_line[i])

    word_count = np.sum(next_words_per_line)

    # generate prediction

    for word in range(word_count):
        imput = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')

        predicted = int(model.predict_classes(imput, verbose=0))

        token_list.append(predicted)

    # arrange output in lines

    line_count = 0

    word_count = 0

    for words in range(len(token_list)):

        word_count += 1

        if word_count > sum(words_per_line[0:line_count + 1]):
            line_count += 1

        line_text[line_count].append(token_list[words])

    # translate back to text

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

    greeting_text_2 = "Dear " + seed_text_1[0] + ":" + "\n"

    output_2 = greeting_text_2 + output_2

    # print(output_2)

    # print the third texts
    token_list = tokenizer.texts_to_sequences([seed_text_r3])[0]

    lines = 4

    # expand list if you increase the number of lines:

    # Important!!!! first line also includes seed text, so select number of words accordingly

    next_words_per_line = [4, 5, 5, 5]

    # initializing an array for each line and counting how many words there are in eachline

    line_text = ([])

    words_per_line = ([])

    for i in range(lines):

        line_text.append(([]))

        if i == 0:

            words_per_line.append(len(token_list) + next_words_per_line[0])

        else:

            words_per_line.append(next_words_per_line[i])

    word_count = np.sum(next_words_per_line)

    # generate prediction

    for word in range(word_count):
        imput = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')

        predicted = int(model.predict_classes(imput, verbose=0))

        token_list.append(predicted)

    # arrange output in lines

    line_count = 0

    word_count = 0

    for words in range(len(token_list)):

        word_count += 1

        if word_count > sum(words_per_line[0:line_count + 1]):
            line_count += 1

        line_text[line_count].append(token_list[words])

    # translate back to text

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

    greeting_text_3 = "Dear " + seed_text_1[0] + ":" + "\n"

    output_3 = greeting_text_3 + output_3

    return [output, output_2, output_3]


def feedbackPoem(feedback, new_line):
    # satisfied=input("Are you satisfied?")
    if feedback == "feedback":
        # print("How would you change the printed poe?(please write line by line)")
        with open("Poems_New_Years2.txt", "a+") as add_poem:

            '''line=input("Give line")
            add_poem.write(line)
            add_poem.write("\n")
            line=input("Give line")
            add_poem.write(line)
            add_poem.write("\n")
            line=input("Give line")
            add_poem.write(line)
            add_poem.write("\n")
            line=input("Give line")
            add_poem.write(line)
            add_poem.write("/")
            add_poem.write("\n")'''
            '''for line in new_lines:
                add_poem.write(line)
                add_poem.write("\n")'''
            add_poem.write(new_line)
            add_poem.write("\n")
        with open("Poems_New_Years2.txt", "r") as file:
            file_content = file.read().replace('\xa0', ' ')  # Saving the writen sentence to a seperate file.
            poems = file_content.count('/')

        if poems >= 50:

            with open("Poems_New_Years2.txt", "r") as add:  ###################################################
                data = add.read()  # Merging the temporary data file to the original.
                #
            with open("Poems_New_Years.txt", "a+") as dataset:  #
                #
                dataset.write('\n')  #
                dataset.write(data)
                dataset.close()

                # load data set and prepare format:
            data_file = open(r"Poems_New_Years.txt", "r")
            train_sentences = data_file.read()
            # split data into lines
            train_sentences = train_sentences.splitlines()

            # start empty string, this part is to let the machine train to understand between verses and the end of poem
            poems = ""
            for line in train_sentences:
                if line[-1] != '/':
                    poems = poems + line + " endofline "
                elif line[-1] == '/':
                    poems = poems + line[0:-1] + " endofpoem"
            poems = poems.lower().split("endofpoem")

            tokenizer = Tokenizergenerator(poems)
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

            # print(xs)
            # print(labels)
            # print(ys)
            '''checkpoint_path_poem = "training_6/cp.ckpt"
            checkpoint_dir = os.path.dirname(checkpoint_path_poem)
            cp_callback_poem = tf.keras.callbacks.ModelCheckpoint(
            filepath=checkpoint_path_poem, save_weights_only=True,
            monitor='loss',
            mode='min',
            save_best_only=True)

            model_poem = Sequential()
            model_poem.add(keras.layers.Embedding(total_words, 100, input_length=max_sequence_len-1))
            model_poem.add(keras.layers.Bidirectional(keras.layers.LSTM(150, return_sequences = True)))
            model_poem.add(keras.layers.Dropout(0.2))
            model_poem.add(keras.layers.LSTM(100))
            model_poem.add(Dense(total_words/2, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
            model_poem.add(Dense(total_words, activation='softmax'))
            model_poem.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])'''
            model_poem = load_model('poem_model')
            # history_poem=
            model_poem.fit(xs, ys, epochs=150, batch_size=10, verbose=1)

            f = open('Poems_New_Years2.txt', 'r+')  # Deleting the temporary save of the added sentences
            f.truncate(0)  #


if __name__ == "__main__":

    # data_file = open(r"Poems_New_Years.txt","r")
    data_file = open('Poems_New_Years.txt')
    train_sentences = data_file.read()
    # split data into lines
    train_sentences = train_sentences.splitlines()

    # start empty string, this part is to let the machine train to understand between verses and the end of poem
    poems = ""
    for line in train_sentences:
        if line[-1] != '/':
            poems = poems + line + " endofline "
        elif line[-1] == '/':
            poems = poems + line[0:-1] + " endofpoem"
    poems = poems.lower().split("endofpoem")

    tokenizer = Tokenizergenerator(poems)
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

    '''checkpoint_path_poem = "training_6/cp.ckpt"

    model = Sequential()
    model.add(keras.layers.Embedding(total_words, 100, input_length=max_sequence_len-1))
    model.add(keras.layers.Bidirectional(keras.layers.LSTM(150, return_sequences = True)))
    model.add(keras.layers.Dropout(0.2))
    model.add(keras.layers.LSTM(100))
    model.add(Dense(total_words/2, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
    model.add(Dense(total_words, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    model.load_weights(checkpoint_path_poem)'''

    model = load_model('poem_model')

    seeds = ["George", "friends"]

    # alternative: seed_text_1 = pd.read_csv(" ")

    seed_text_1 = seeds

    outputs = poet(seed_text_1[0], seed_text_1[1])

    for output in outputs:
        print(output)

    # feedback_poem()
    new_lines = ['hello', 'this', 'is', 'a', 'new', 'line']
    feedbackPoem("feedback", new_lines[0])
