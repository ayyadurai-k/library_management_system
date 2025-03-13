from django.shortcuts import render
from book.models import Book
from django.http import JsonResponse


# Create your views here.
def list_books(request):
    books = Book.objects.all().values("id","name", "description")
    return JsonResponse(list(books), safe=False)
