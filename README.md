# tweets-sentiments-recognition

This app detects tweets's sentiments using a Naive Bayes model. 
Tweets are fetch from the twitter's API using an specified hashtag to collect them.

## Run this project

#### 1. Create a virtual env using virtualenv and activate it

```sh
$ pip3 install virtualenv
$ virtualenv env
$ source ./env/bin/activate 
```
You should activate your virtual-env each time you restart your terminal

#### 2. Install all dependencies

```sh
$ pip3 install -r requirements.txt
```

#### 3. Create a .env file containing your Twitter's API Credentials. e.g:
```
CONSUMER_KEY = "YOUR CONSUMER KEY"
CONSUMER_SECRET = "YOUR CONSUMER SECRET KEY"
OAUTH_TOKEN = "YOUR OAUTH TOKEN"
OAUTH_TOKEN_SECRET = "YOUR OAUTH TOKEN SECRET"
```

#### 4. Run the project
```sh
$ flask run
```
