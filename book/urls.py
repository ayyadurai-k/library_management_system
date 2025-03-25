from django.urls import path
from book.views import get_book, list_books, create_book


urlpatterns = [
    path("get/<int:book_id>/", get_book),
    path("list/", list_books),
    path("create/", create_book),
]
