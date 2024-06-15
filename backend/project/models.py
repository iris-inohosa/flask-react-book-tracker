import datetime

from project import db


class Book(db.Model):
    """
    Class that represents the Book that has been read
    Contains following attributes:
        * title - book title
        
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(100), nullable=True)
    author = db.Column(db.String(100), nullable=True)
    publish_date = db.Column(db.DateTime)
    added_on = db.Column(db.DateTime, default=datetime.datetime.now)
    genre = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    personal_rating = db.Column(db.Float, default=0.0)
    img_url = db.Column(
        db.String(300), default="https://img.icons8.com/plasticine/100/book.png")

    def to_json(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
