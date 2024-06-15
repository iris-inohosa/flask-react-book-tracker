from flask import request, jsonify, Blueprint
from project import db
from project.models import Book
from . import books_api


@books_api.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    result = [book.to_json() for book in books]
    return jsonify(result)


@books_api.route("/books", methods=["POST"])
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


@books_api.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    try:
        book = Book.query.get(id)
        if not book:
            return jsonify({"error": "Book doesn't exist"}), 404
        db.session.delete(book)
        db.session.commit()
        return jsonify({"msg": "Book deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@books_api.route("/books/<int:id>", methods=["PATCH"])
def update_book(id):
    try:
        book = Book.query.get(id)
        if not book:
            return jsonify({"error": "Book not found"}), 404
        data = request.json
        book.description = data.get("description", book.description)
        book.personal_rating = data.get(
            "personal_rating", book.personal_rating)

        db.session.commit()
        return jsonify(book.to_json()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
