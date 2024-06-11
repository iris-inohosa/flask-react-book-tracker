from models import Book


def test_new_book():
    """
    GIVEN a Book model
    WHEN a new Book is created
    THEN check the title and personal_rating are defined correctly
    """
    book = Book(title="Harry Potter", personal_rating=5.0)
    assert book.title == "Harry Potter"
    assert book.personal_rating == 5.0
