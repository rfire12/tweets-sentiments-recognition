from flask import Flask, request, render_template
from model.model import train_naive_bayes_model, predict_sentiment
from functions.functions import get_tweets_from_hashtag
import os

app = Flask(__name__)
# Load Twitter API Credentials

app.config["credentials"] = {
    "CONSUMER_KEY": os.environ.get("CONSUMER_KEY"),
    "CONSUMER_SECRET": os.environ.get("CONSUMER_SECRET"),
    "OAUTH_TOKEN": os.environ.get("OAUTH_TOKEN"),
    "OAUTH_TOKEN_SECRET": os.environ.get("OAUTH_TOKEN_SECRET")}


@app.route("/", methods=['GET'])
def index():
    classifier, vectorizer = train_naive_bayes_model()
    predict_sentiment(classifier, vectorizer)
    tweets = [{'tweet': 'TEST', 'sentiment': 'positive'}]
    amount = len(tweets)
    return render_template('home.html', tweets = tweets, amount = amount)

@app.route("/tweets", methods=['GET'])
def tweets():
    tweets, pre_processed_tweets = get_tweets_from_hashtag("#hey", app.config["credentials"] )
    classifier, vectorizer = train_naive_bayes_model()
    tweets_predicted = predict_sentiment(pre_processed_tweets, tweets, classifier, vectorizer) 
    print(tweets_predicted)
    return "none"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
