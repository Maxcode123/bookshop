from rest_framework.generics import ListAPIView, RetrieveAPIView

from books.models import Book, Genre, Publisher, Author
from books.serializers import (
    BookSerializer,
    GenreSerializer,
    PublisherSerializer,
    AuthorSerializer,
)


class ListBooksView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.prefetch_related("publisher", "genres", "authors")
        queryset = queryset.filter(**self._permitted_params())
        return queryset

    def _permitted_params(self):
        permitted = {"genre": "genres__uuid"}
        return {
            permitted[k]: v
            for k, v in self.request.query_params.items()
            if k in permitted
        }


class ShowBookView(RetrieveAPIView):
    serializer_class = BookSerializer
    lookup_field = "uuid"
    queryset = Book.objects.prefetch_related("publisher", "genres", "authors")


class ListGenresView(ListAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class ListPublishersView(ListAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


class ListAuthorsView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
