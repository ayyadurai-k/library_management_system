# urls.py
from django.urls import path
from author.views import get_author, list_authors, create_author, update_author, delete_author

urlpatterns = [
    path("get/<int:author_id>/", get_author),
    path("list/", list_authors),
    path("create/", create_author),
    path("update/<int:author_id>/", update_author),
    path("delete/<int:author_id>/", delete_author),
]