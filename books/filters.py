from uuid import UUID
from typing import Iterable, Any, Type
from operator import or_

from django.db.models import Q
from rest_framework.filters import BaseFilterBackend

from books.models import Genre, Author, Publisher
from utils.base_model import UUIDMixin


class ListBooksFilterBackend(BaseFilterBackend):
    """
    Filter by genre, author and publisher.
    The filter expands the given genres to all the descendants of the genre, this
    enables displaying all books with children genres of the given genre.
    """

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(**self._create_filters(request.query_params))

    def _create_filters(self, params) -> dict[str, Any]:
        filters = {}

        genre_uuids = params.getlist("genre")
        self._validate_existance(genre_uuids, Genre)
        subgenre_uuids = self._get_genre_children_uuids(genre_uuids)
        if len(genre_uuids) > 0:
            filters.update(genres__uuid__in=subgenre_uuids)

        author_uuids = params.getlist("author")
        self._validate_existance(author_uuids, Author)
        if len(author_uuids) > 0:
            filters.update(authors__uuid__in=author_uuids)

        publisher_uuids = params.getlist("publisher")
        self._validate_existance(publisher_uuids, Publisher)
        if len(publisher_uuids) > 0:
            filters.update(publisher__uuid__in=publisher_uuids)

        return filters

    @staticmethod
    def _get_genre_children_uuids(genre_uuids: Iterable[UUID]) -> Iterable[UUID]:
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

    @staticmethod
    def _validate_existance(uuids: Iterable[UUID], model_cls: Type[UUIDMixin]) -> None:
        for uuid in uuids:
            model_cls.find_by_uuid(uuid)
