import tweepy
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')

def pre_process_string(inputString):
    inputString = deEmojify(inputString)

    inputString = re.sub(r'http\S+','', inputString, flags=re.MULTILINE)
    inputString = re.sub(
        r'https?:\/\/(www\.)?[-a-zA-Z0–9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0–9@:%_\+.~#?&//=]*)', '', inputString, flags=re.MULTILINE)
    inputString = re.sub(
        r'[-a-zA-Z0–9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0–9@:%_\+.~#?&//=]*)', '', inputString, flags=re.MULTILINE)
    inputString = re.sub(r"#(\w+)", '', inputString, flags=re.MULTILINE)
    inputString = re.sub(r"@(\w+)", '', inputString, flags=re.MULTILINE)
    inputString = re.sub(r"[0-9]", '', inputString, flags=re.MULTILINE)

    inputString = inputString.lower()

    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(inputString)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    inputString = ' '.join(filtered_sentence)

    inputString = ' '.join(re.split(r'\W+', inputString))

    return inputString


def process_tweets(tweets):
    data = []

    for tweet in tweets:
        data.append(pre_process_string(tweet))
    
    return data


def get_tweets_from_hashtag(hashtag, credentials):
    auth = tweepy.OAuthHandler(credentials.get("CONSUMER_KEY", ""), credentials.get("CONSUMER_SECRET", ""))
    auth.set_access_token(credentials.get("OAUTH_TOKEN", ""), credentials.get("OAUTH_TOKEN_SECRET", ""))
    api = tweepy.API(auth)
    tweets = []

    for tweet in tweepy.Cursor(api.search, q=hashtag, lang="en").items(50):
        tweets.append(tweet.text)

    return tweets, process_tweets(tweets)