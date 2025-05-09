from rest_framework.serializers import ModelSerializer, StringRelatedField

from books.models import Genre, Publisher, Author, Book


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "uuid", "parent_id", "root_id", "name")


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = ("id", "uuid", "name")


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "id",
            "uuid",
            "first_names",
            "last_name",
            "date_of_birth",
            "date_of_death",
            "summary",
        )


class BookSerializer(ModelSerializer):
    publisher = StringRelatedField(many=False)
    genres = StringRelatedField(many=True)
    authors = StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = (
            "id",
            "uuid",
            "title",
            "pages",
            "introductory_pages",
            "width_in_cm",
            "length_in_cm",
            "cover",
            "weight_in_gr",
            "paper",
            "isbn",
            "edition",
            "series",
            "volume",
            "publication_date",
            "language",
            "publisher",
            "genres",
            "authors",
        )
