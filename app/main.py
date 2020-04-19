from flask import Flask, request
import os

app = Flask(__name__)
#Load Twitter API Credentials
app.config["CONSUMER_KEY"] = os.environ.get("CONSUMER_KEY")
app.config["CONSUMER_SECRET"] = os.environ.get("CONSUMER_SECRET")
app.config["OAUTH_TOKEN"] = os.environ.get("OAUTH_TOKEN")
app.config["OAUTH_TOKEN_SECRET"] = os.environ.get("OAUTH_TOKEN_SECRET")


@app.route("/")
def index():
    print(app.config["CONSUMER_KEY"])
    return "This is the homepage"

if __name__ == "__main__":
    app.run(debug=True)
    

