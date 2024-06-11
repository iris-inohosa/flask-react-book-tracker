from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String(300), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "genre": self.genre,
            "description": self.description,
            "rating": self.rating,
            "imgUrl": self.img_url,
        }
