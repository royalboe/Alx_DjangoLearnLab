from rest_framework import serializers
from datetime import datetime
from .models import Author, Book

# Serializer for Book model.
# Serializes all fields and includes custom validation.
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation to ensure publication year is not in the future.
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer for Author model.
# Includes nested serialization of related books using BookSerializer.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested books (reverse relation from Author to Book)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']