# -*- coding: utf-8 -*-
"""Keras Sentiment Example.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pDWTqG6s9Tn68MO-qagBxB9P_iQR-TJL

From: https://keras.io/examples/imdb_lstm/ with epochs reduced to 3 to speed up training
"""
import re
import json
from tensorflow.keras.models import load_model
from bs4 import BeautifulSoup
import nltk

nltk.download("punkt")

MODEL = load_model("my_model.h5")
with open("word_index.json") as f:
    WORD_INDEX = json.load(f)
NUM_WORDS = 20000


def preprocess_text(text):
    # Removing html tags
    processed_text = BeautifulSoup(text, features="html.parser").get_text()
    # Remove capitalization
    processed_text = processed_text.lower()
    # Remove punctuations and numbers
    processed_text = re.sub(r"[^a-z'\s]", "", processed_text)
    # Remove quotations
    processed_text = re.sub(r"([^a-z])\'|\'([^a-z])", r"\1\2", processed_text)
    # Remove excessive whitespace
    processed_text = re.sub(r"\s+", r" ", processed_text)
    return processed_text


def convert_text_to_num_seq(text):
    text_word_list = nltk.word_tokenize(text)
    num_seq = [1]
    for word in text_word_list:
        try:
            num = WORD_INDEX[word]
            num += 3
        except KeyError:
            num = 0
        if num >= NUM_WORDS:
            num = 0
        num_seq.append(num)
    return num_seq


def predict_sentiment(text):
    processed_text = preprocess_text(text)
    text_as_vectors = convert_text_to_num_seq(processed_text)
    prediction = MODEL.predict([text_as_vectors])
    if prediction[0][0] > 0.5:
        sentiment = "Positive"
    else:
        sentiment = "Negative"
    result = [str(prediction[0][0]), sentiment]
    return result
