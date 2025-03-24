from django.urls import path
from book.views import get_book,list_books


urlpatterns = [
    path("get/<int:book_id>/", get_book),
    path("list/",list_books)
]
