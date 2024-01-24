from flask import Flask, render_template
from .config import Config
from .models import db, User, Tweet, Tweet_Image
from flask_migrate import Migrate

# CONFIG SECTION
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)  # This connects our database to our flask application
Migrate(app, db)  # connects our migrations with our app and out database

# Query all the tweets

# @app.route("/")
# def index():
#     tweets = Tweet.query.all()
#     print(tweets, "This tweets")
#     return render_template("index.html", tweets=tweets)


# One tweet by specific paramater

# @app.route("/")
# def index():
#     tweet_id = 2
#     tweet = Tweet.query.get(tweet_id)
#     print(tweet, "This tweet 2")
#     return render_template("one_tweet.html", tweet=tweet)


# Querying all the tweets by checking column user_id on tweets, uses filter_by and we get all()
# @app.route("/")
# def index():
#     user_id = 1
#     tweets = Tweet.query.filter_by(user_id=user_id).all()
#     print(tweets, "This tweets belonging to user 1")
#     return render_template("index.html", tweets=tweets)


# # Query using case sensistive and case insenstive to see if user.name starts with something
# @app.route("/")
# def index():
#     # users = User.query.filter(User.name.ilike("w%")).all() # Case insenstive start with "w"
#     users = User.query.filter(User.name.like("w%")).all() # Case sensetivie start with lowercase "w"
#     print(users)
#     return render_template("index.html", users=users)


# Include other tables within a query
@app.route("/")
def index():
    tweets = db.session.query(Tweet, User).join(User).all()
    # print(tweets)
    for tweet in tweets:
        print(tweet[0].body, "This is tweet")
        print(tweet[1].name, "this is user")

    return render_template("index.html", tweets=tweets)
