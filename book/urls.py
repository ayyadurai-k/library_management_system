from django.urls import path
from book.views import list_books


urlpatterns = [
    path("list/",list_books)
]
