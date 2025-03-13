from django.shortcuts import render
from book.models import Book
from django.http import JsonResponse


# Create your views here.
def list_books(request):
    books = Book.objects.all().values("id","name", "description")
    return JsonResponse(list(books), safe=False)


def get_book(request,book_id):
    book = Book.objects.get(id=book_id)
    data = {
        "id": book.id,
        "name": book.name,
        "description": book.description
    }
    return JsonResponse(data,safe=False)
    