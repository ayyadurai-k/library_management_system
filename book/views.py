from rest_framework.decorators import api_view
import book
from book.models import Book
from book.serializers import BookSerializer
from rest_framework.response import Response

@api_view(["GET"]) # TO SPECIFY THE REQUEST METHOD
def get_book(request,book_id):
    book = Book.objects.get(id=book_id)
    serializer = BookSerializer(book) # CONVERT MODEL OBJECT INTO JSON
    return Response(serializer.data) # SEND RESPONSE TO USER


@api_view(["GET"])
def list_books(request):    
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"message":"Book created successfully"}, status=201)