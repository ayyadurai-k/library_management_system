from rest_framework.decorators import api_view
from rest_framework.response import Response
from author.models import Author
from author.serializers import AuthorSerializer


@api_view(["GET"])
def get_author(request, author_id):
    author = Author.objects.get(id=author_id)
    serializer = AuthorSerializer(author)
    return Response(serializer.data, status=200)


@api_view(["GET"])
def list_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data, status=200)


@api_view(["POST"])
def create_author(request):
    serializer = AuthorSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"message": "Author created successfully"}, status=201)


@api_view(["PATCH"])
def update_author(request, author_id):
    author = Author.objects.get(id=author_id)
    serializer = AuthorSerializer(instance=author, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(
        {"message": "Author updated successfully"}, status=200
    )


@api_view(["DELETE"])
def delete_author(request, author_id):
    author = Author.objects.get(id=author_id)
    author.delete()
    return Response(
        {"message": "Author deleted successfully"}, status=204
    )


