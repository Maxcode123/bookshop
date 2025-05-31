from uuid import UUID
from typing import Iterable

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
        queryset = queryset.filter(**self._create_filters())
        return queryset

    def _create_filters(self):
        genre_uuid = self.request.query_params.get("genre", None)
        if genre_uuid is not None:
            return {"genres__uuid__in": self._get_genre_children_uuids(genre_uuid)}

        return {}

    def _get_genre_children_uuids(self, genre_uuid: UUID) -> Iterable[UUID]:
        parent = Genre.find_by_uuid(genre_uuid)
        children = Genre.objects.filter(path__descendants=parent.path)
        uuids = map(lambda g: g.uuid, children)
        return uuids


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
