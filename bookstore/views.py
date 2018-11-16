from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bookstore.models import Author, Book
from bookstore.serializers import AuthorSerializer, BookSerializer
from django.conf import settings
from decouple import config


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# def test_view(request):
#     request.statsd.timings.start('test_view_timer')
#     response = Response({'environment': config('ENVIRONMENT'), 'version': settings.VERSION})
#     request.statsd.timings.stop('test_view_timer')
#     return response


@api_view()
def get_version(request):
    request.statsd.timings.start('get_version_timer')
    response = Response({'environment': config('ENVIRONMENT'), 'version': settings.VERSION})
    request.statsd.timings.stop('get_version_timer')
    return response

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

