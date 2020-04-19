from flask import Flask, request
from model.model import train_naive_bayes_model, predict_sentiment
import os

app = Flask(__name__)
# Load Twitter API Credentials
app.config["CONSUMER_KEY"] = os.environ.get("CONSUMER_KEY")
app.config["CONSUMER_SECRET"] = os.environ.get("CONSUMER_SECRET")
app.config["OAUTH_TOKEN"] = os.environ.get("OAUTH_TOKEN")
app.config["OAUTH_TOKEN_SECRET"] = os.environ.get("OAUTH_TOKEN_SECRET")


@app.route("/")
def index():
    classifier, vectorizer = train_naive_bayes_model()
    predict_sentiment(classifier, vectorizer)
    return "This is the homepage"


if __name__ == "__main__":
    app.run(debug=True)
