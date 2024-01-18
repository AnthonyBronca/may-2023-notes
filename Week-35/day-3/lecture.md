# Flask

## Announcements

1. 100% passing on the test!! LETS GOOOOOOO!!!! YOU ALL GET A CELEBRATORY TRAIN!
On top of that, this was your penultimate assessment, and also your last test to include MC!
2. Adjustments to the week. As there was no class on Monday, and an assessment Tuesday it may seem like we are slightly behind. Luckily there isn't a lot of different content, just 3 key things to know so we will cover them on Wednesday, Thursday, and Friday. With that though, we may not have time to go over all the projects, so I recommend going over some of these on your own time, and making sure you come to class prepared to work with pairs
3. We will be pairing a lot more these next 2 weeks as this stuff is content heavy and you all should feel comfortable enough writing python now



## Topics we will cover this week:

1. Flask (building a server with Python)
2. Jinja (templating framework)
3. WTForms
4. Try to get to SQLAlchemy, but we also have all week to do that if needed

-----------------------------------------------


## Flask

Flask is a server-side development framework built using Python. It allows us to quickly set up starter applications, and use Python's easy-to-read pros to make very readable backends

### What it is used for

While you can make a production level backend with Flask (which we will do with Group projects),
Flask is not the greatest for scaling. As an example, Flask can handle about 30k GET requests a minute, and Express can do about 65k GET requests a minute.

So why would we want to use Flask?

If you go in to backend engineering you will want to be able to test the skeleton for some design implementations without having to commit to writing more complex code.

If you have to build a small scale project that won't really grow much (think like an office, restaurant, small business)

A Basic Flask application needs a few things:

1. an init.py file (don't forget the dunders)
2. A config file
3. a .flaskenv file
4. setting up an app with passed in config
5. a .venv
6. some routes

We will be learning about adding Forms and Jinja to make this more advanced and dynamic
