from django.contrib.auth.models import User, Group
from rest_framework import serializers
from bookstore.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    # books = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='book-detail'
    # )

    class Meta:
        model = Author
        #fields = ('url', 'books', 'birth_date', 'first_name', 'last_name')
        fields = ('url', 'birth_date', 'first_name', 'last_name')


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('url', 'authors', 'publication_date', 'title')


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')
