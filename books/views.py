from rest_framework.generics import ListAPIView, RetrieveAPIView

from books.models import Book, Genre, Publisher, Author
from books.serializers import (
    BookSerializer,
    DetailedBookSerializer,
    GenreSerializer,
    PublisherSerializer,
    AuthorSerializer,
)
from books.filters import ListBooksFilterBackend


# GET /books/
class ListBooksView(ListAPIView):
    serializer_class = BookSerializer
    filter_backends = [ListBooksFilterBackend]
    queryset = Book.objects.prefetch_related("publisher", "genres", "authors")


# GET /books/<uuid>
class ShowBookView(RetrieveAPIView):
    serializer_class = DetailedBookSerializer
    lookup_field = "uuid"
    queryset = Book.objects.prefetch_related("publisher", "genres", "authors")


# GET /genres/
class ListGenresView(ListAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


# GET /publishers/
class ListPublishersView(ListAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


# GET /authors/
class ListAuthorsView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
