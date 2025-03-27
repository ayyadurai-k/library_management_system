from book.models import Book
from book.serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

