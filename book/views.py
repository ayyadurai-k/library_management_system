from asyncio import IocpProactor
from django.shortcuts import render
from book.models import Book
from django.http import JsonResponse
import json 
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def create_book(request):
    data = json.loads(request.body) # CONVERT JSON INTO DICTIONARY
    
    name = data.get("name") # EXTRACT VALUE FROM DICTIONARY
    description = data.get("description") # EXTRACT VALUE FROM DICTIONARY
    
    book = Book.objects.create(name=name,description=description)
    
    return JsonResponse({"message": "Book created successfully"})

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

def update_book(request,book_id):
    book = Book.objects.get(id=book_id)
    data = json.loads(request.body)
    
    book.name = data.get("name")
    book.description = data.get("description")
    
    book.save()
    
    return JsonResponse({"message": "Book updated successfully"})

def delete_book(request,book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return JsonResponse({"message": "Book deleted successfully"})