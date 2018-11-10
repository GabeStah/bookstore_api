from rest_framework import serializers
from bookstore.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('url', 'birth_date', 'first_name', 'last_name')


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('url', 'authors', 'publication_date', 'title')
