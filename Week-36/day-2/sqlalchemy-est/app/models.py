from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# One USER has many tweets / a tweet belongs to 1 user
# one Tweet has many images / a tweet_image belongs to a tweet


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(
        db.Integer, primary_key=True
    )  # It will auto increment, and used for references
    name = db.Column(db.String(30), nullable=False)
    profile_url = db.Column(db.String(1000))  # This is allowed to be null

    # plural tweets, on user should mean we have one user with many tweets
    tweets = db.relationship("Tweet", back_populates="user")


class Tweet(db.Model):
    __tablename__ = "tweets"

    id = db.Column(
        db.Integer, primary_key=True
    )  # It will auto increment, and used for references
    body = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    user = db.relationship("User", back_populates="tweets")
    tweet_images = db.relationship("Tweet_Image", back_populates="tweet")


class Tweet_Image(db.Model):
    __tablename__ = "tweet_images"

    id = db.Column(
        db.Integer, primary_key=True
    )  # It will auto increment, and used for references
    url = db.Column(db.String(1000), nullable=False)

    # How do we create a reference on tweet_image to relate to Tweet
    # Creating a column called tweet_id, that inherits a FK from Tweet
    tweet_id = db.Column(db.Integer, db.ForeignKey("tweets.id"), nullable=False)

    # Relationship for querying
    tweet = db.relationship("Tweet", back_populates="tweet_images")
