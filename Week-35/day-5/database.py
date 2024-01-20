from dotenv import load_dotenv

load_dotenv()

from app import app, db
from app.models import User


with app.app_context():
    # Fresh start
    db.drop_all()
    db.create_all()

    # Initialize our seeders
    user1 = User(name="Margot", age=14, email="margot@demo.io")
    user2 = User(name="Ant", age=15, email="ant@demo.io")
    user3 = User(name="Bob", age=16, email="bob@demo.io")

    # Declaring items to add to our database
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    # Commit it and push it up to database. TIP: Only want one of these
    db.session.commit()
