from django.contrib.auth.models import User, Group
from rest_framework import serializers
from bookstore.models import Author, Book


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    birth_date = serializers.DateField()
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    last_name = serializers.CharField(required=True, allow_blank=False, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Author` instance, given the validated data.
        """
        books_data = validated_data.pop('books')
        author = Author.objects.create(**validated_data)
        for book_data in books_data:
            Book.objects.create(author=author, **book_data)
        return author

    def update(self, instance, validated_data):
        """
        Update and return an existing `Author` instance, given the validated data.
        """
        instance.books = validated_data.get('books', instance.books)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance

    class Meta:
        model = Author
        fields = ('url', 'birth_date', 'first_name', 'last_name', 'books')


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    authors = AuthorSerializer(many=True)
    publication_date = serializers.DateField()
    title = serializers.CharField(required=True, allow_blank=False, max_length=255)

    def create(self, validated_data):
        """
        Create and return a new `Book` instance, given the validated data.
        """
        authors_data = validated_data.pop('authors')
        book = Book.objects.create(**validated_data)
        for author_data in authors_data:
            Author.objects.create(book=book, **author_data)
        return book

    def update(self, instance, validated_data):
        """
        Update and return an existing `Book` instance, given the validated data.
        """
        instance.authors = validated_data.get('authors', instance.authors)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance

    class Meta:
        model = Book
        fields = ('url', 'authors', 'publication_date', 'title')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')