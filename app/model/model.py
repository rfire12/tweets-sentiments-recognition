import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn.metrics import accuracy_score 
import numpy as np 
import copy 
import json
import os


def train_naive_bayes_model():
    df=pd.read_csv(os.path.join(os.path.dirname(__file__), "./final.csv"))
    vectorizer = TfidfVectorizer(use_idf=True, strip_accents='ascii')

    tweets = vectorizer.fit_transform(df.text.values.astype('U'))
    sentiments = df.sentiment_label

    tweets_train, tweets_test, sentiment_train, sentiment_test = train_test_split(tweets, sentiments, train_size=0.99, random_state=100) 

    classifier = naive_bayes.MultinomialNB()
    classifier.fit(tweets_train, sentiment_train)

    sentiment_predicted = classifier.predict(tweets_test)

    print(accuracy_score(sentiment_test, sentiment_predicted))
    return classifier, vectorizer

def format_data(tweets, predicted_sentiments):
    data = []
    for tweet, sentiment in zip(tweets, predicted_sentiments):
        data.append({"tweet": tweet, "sentiment": sentiment})
    return data

def predict_sentiment(tweets, classifier, vectorizer):
    tweets_array = np.array(tweets)
    vector = vectorizer.transform(tweets_array)
    predicted_sentiment = classifier.predict(vector)
    return format_data(tweets, predicted_sentiment)
    




