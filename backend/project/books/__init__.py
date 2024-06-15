"""
The book Blueprint
"""
from flask import Blueprint

books_api = Blueprint("books_api", __name__, url_prefix="/api")

from . import routes