from flask import request, jsonify, Blueprint
from models import Book

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    result = [book.to_json() for book in books]
    return jsonify(result)
