from django.urls import path
from book.views import list_books,get_book,create_book


urlpatterns = [
    path("create/",create_book),
    path("list/",list_books),
    path("get/<int:book_id>/",get_book)
]
