from uuid import UUID
from typing import Iterable
from operator import or_

from django.db.models import Q
from rest_framework.generics import ListAPIView, RetrieveAPIView

from books.models import Book, Genre, Publisher, Author
from books.serializers import (
    BookSerializer,
    DetailedBookSerializer,
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
        filters = {}

        genre_uuids = self.request.query_params.getlist("genre")
        if len(genre_uuids) > 0:
            filters.update(genres__uuid__in=self._get_genre_children_uuids(genre_uuids))

        author_uuids = self.request.query_params.getlist("author")
        if len(author_uuids) > 0:
            filters.update(authors__uuid__in=author_uuids)

        publisher_uuids = self.request.query_params.getlist("publisher")
        if len(publisher_uuids) > 0:
            filters.update(publisher__uuid__in=publisher_uuids)

        return filters

    def _get_genre_children_uuids(self, genre_uuids: Iterable[UUID]) -> Iterable[UUID]:
        parents = Genre.objects.filter(uuid__in=genre_uuids)
        queries = list(map(lambda p: Q(path__descendants=p.path), parents))

        if len(queries) > 1:
            # create a merged OR query like so: Q | Q | Q ...
            merged = queries[0]
            for q in queries[1:]:
                merged = or_(merged, q)
            queries = merged
        elif len(queries) == 1:
            queries = queries[0]
        else:
            queries = Q()

        children = Genre.objects.filter(queries)
        uuids = map(lambda g: g.uuid, children)
        return uuids


class ShowBookView(RetrieveAPIView):
    serializer_class = DetailedBookSerializer
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
