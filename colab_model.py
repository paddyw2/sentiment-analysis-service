# -*- coding: utf-8 -*-
"""Keras Sentiment Example.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pDWTqG6s9Tn68MO-qagBxB9P_iQR-TJL

From: https://keras.io/examples/imdb_lstm/ with epochs reduced to 3 to speed up training
"""

from __future__ import print_function

from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding
from tensorflow.keras.layers import LSTM
from tensorflow.keras.datasets import imdb

max_features = 20000
# cut texts after this number of words (among top max_features most common words)
maxlen = 80
batch_size = 32

print('Loading data...')
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
print(len(x_train), 'train sequences')
print(len(x_test), 'test sequences')

print('Pad sequences (samples x time)')
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)

print('Build model...')
model = Sequential()
model.add(Embedding(max_features, 128))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))

# try using different optimizers and different optimizer configs
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=3,
          validation_data=(x_test, y_test))
score, acc = model.evaluate(x_test, y_test,
                            batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)
print('Saving model...')
model_file_name = 'my_model.h5'
model.save(model_file_name)
print('Model saved')

"""Some example text cleaning functions sourced from: https://www.stackabuse.com/python-for-nlp-movie-sentiment-analysis-using-deep-learning-in-keras/"""

import re

def preprocess_text(sen):
    # Removing html tags
    sentence = remove_tags(sen)

    # Remove punctuations and numbers
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)

    # Single character removal
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)

    # Removing multiple spaces
    sentence = re.sub(r'\s+', ' ', sentence)

    return sentence

def remove_tags(text):
    return re.sub('', text)

"""Now the model is trained, we need a way to convert a review to the numerical input the model expects.

1. Get the word index used by the dataset, which is a dictionary that maps strings to numbers
"""

word_index = imdb.get_word_index()

"""Get a sample from the imdb dataset (i.e. x_train[0]) along with it's text version (generated using the method below)"""

expected_nums = [1, 14, 22, 16, 43, 530, 973, 1622, 1385, 65, 458, 4468, 66, 3941, 4, 173, 36, 256, 5, 25, 100, 43, 838, 112, 50, 670, 2, 9, 35, 480, 284, 5, 150, 4, 172, 112, 167, 2, 336, 385, 39, 4, 172, 4536, 1111, 17, 546, 38, 13, 447, 4, 192, 50, 16, 6, 147, 2025, 19, 14, 22, 4, 1920, 4613, 469, 4, 22, 71, 87, 12, 16, 43, 530, 38, 76, 15, 13, 1247, 4, 22, 17, 515, 17, 12, 16, 626, 18, 19193, 5, 62, 386, 12, 8, 316, 8, 106, 5, 4, 2223, 5244, 16, 480, 66, 3785, 33, 4, 130, 12, 16, 38, 619, 5, 25, 124, 51, 36, 135, 48, 25, 1415, 33, 6, 22, 12, 215, 28, 77, 52, 5, 14, 407, 16, 82, 10311, 8, 4, 107, 117, 5952, 15, 256, 4, 2, 7, 3766, 5, 723, 36, 71, 43, 530, 476, 26, 400, 317, 46, 7, 4, 12118, 1029, 13, 104, 88, 4, 381, 15, 297, 98, 32, 2071, 56, 26, 141, 6, 194, 7486, 18, 4, 226, 22, 21, 134, 476, 26, 480, 5, 144, 30, 5535, 18, 51, 36, 28, 224, 92, 25, 104, 4, 226, 65, 16, 38, 1334, 88, 12, 16, 283, 5, 16, 4472, 113, 103, 32, 15, 16, 5345, 19, 178, 32]
input_review = "this film was just brilliant casting location scenery story direction everyone's really suited the part they played and you could just imagine being there robert is an amazing actor and now the same being director father came from the same scottish island as myself so i loved the fact there was a real connection with this film the witty remarks throughout the film were great it was just brilliant so much that i bought the film as soon as it was released for retail and would recommend it to everyone to watch and the fly fishing was amazing really cried at the end it was so sad and you know what they say if you cry at a film it must have been good and this definitely was also congratulations to the two little boy's that played the of norman and paul they were just brilliant children are often left out of the praising list i think because the stars that play them all grown up are such a big profile for the whole film but these children are amazing and should be praised for what they have done don't you think the whole story was so lovely because it was true and was someone's life after all that was shared with us all"

"""Create a review to numeric array function using the dictionary, plus a increment of 3, as per:

https://datascience.stackexchange.com/a/52128

and:

https://github.com/keras-team/keras/blob/master/keras/datasets/imdb.py#L14
"""

import nltk
nltk.download('punkt')

def convert_review_to_num_seq(review):
  review_word_list = nltk.word_tokenize(review)
  num_seq = [1]
  for word in review_word_list:
    num = word_index[word]
    num += 3
    num_seq.append(num)
  return num_seq

"""Validate that converting the example review string generates it's numeric representation. Alternatively you can select a random value from x_train and perform the reverse and check to see if the result is properly ordered and makes sense."""

seq = convert_review_to_num_seq(input_review)
print(seq)

"""Test out the model with some example reviews"""

test_review_good = "i have seen better movies but to be honest this was still pretty great"
test_review_bad = "i did not really like the movie that much"
result = model.predict([convert_review_to_num_seq(test_review_good)])
print(result)
if result[0][0] > 0.5:
  print('Positive')
else:
  print('Negative')
