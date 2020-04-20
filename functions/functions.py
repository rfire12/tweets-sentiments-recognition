import tweepy
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

def deEmojify(text):
    return text.encode('ascii', 'ignore').decode('ascii')

def pre_process_string(text):
    text = deEmojify(text)

    text = re.sub(r'http\S+','', text, flags=re.MULTILINE)
    text = re.sub(
        r'https?:\/\/(www\.)?[-a-zA-Z0–9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0–9@:%_\+.~#?&//=]*)', '', text, flags=re.MULTILINE)
    text = re.sub(
        r'[-a-zA-Z0–9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0–9@:%_\+.~#?&//=]*)', '', text, flags=re.MULTILINE)
    text = re.sub(r"#(\w+)", '', text, flags=re.MULTILINE)
    text = re.sub(r"@(\w+)", '', text, flags=re.MULTILINE)
    text = re.sub(r"[0-9]", '', text, flags=re.MULTILINE)

    text = text.lower()

    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(text)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    text = ' '.join(filtered_sentence)

    text = ' '.join(re.split(r'\W+', text))

    return text


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

    for tweet in tweepy.Cursor(api.search, q=hashtag, lang="en", tweet_mode='extended').items(50):
        tweet_text = ""
        try:
            tweet_text = tweet.retweeted_status.full_text if hasattr(tweet, 'retweeted_status') else tweet.full_text
        except:
            tweet_text = tweet.full_text
        tweets.append(tweet_text)

    return tweets, process_tweets(tweets)