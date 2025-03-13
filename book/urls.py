from django.urls import path
from book.views import list_books,get_book


urlpatterns = [
    path("list/",list_books),
    path("get/<int:book_id>/",get_book)
]
