from flask import request, jsonify, Blueprint
from models import Book, db

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    result = [book.to_json() for book in books]
    return jsonify(result)


@api.route("/books", methods=["POST"])
def add_book():
    try:
        book = request.json
        title = book.get("title")
        personal_rating = book.get("personal_rating")

        new_book = Book(title=title, personal_rating=personal_rating)
        db.session.add(new_book)
        db.session.commit()

        return jsonify({"msg": "Book added successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
