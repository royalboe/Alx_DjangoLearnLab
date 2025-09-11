#!/usr/bin/python

# This script demonstrates various Django ORM queries on models with relationships.
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return []

# List all books in the library
def get_all_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []
    
# Find the librarian of a specific library
def get_librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
        # librarian = Librarian.objects.get(library=library)
        # return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None