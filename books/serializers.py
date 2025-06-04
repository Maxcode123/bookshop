from rest_framework.serializers import ModelSerializer, StringRelatedField, RelatedField

from books.models import Genre, Publisher, Author, Book, BookAuthor


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "uuid", "name")


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


class DetailedPublisherField(RelatedField):
    def to_representation(self, value) -> list[dict[str, str]]:
        return {"name": value.name, "uuid": value.uuid}


class DetailedGenreField(RelatedField):
    def to_representation(self, value) -> list[dict[str, str]]:
        return [{"name": g.name, "uuid": g.uuid} for g in value.instance.genres.all()]


class DetailedAuthorField(RelatedField):
    def to_representation(self, value) -> list[dict[str, str]]:
        book_authors = BookAuthor.objects.select_related("author").filter(
            book_id=value.instance.id
        )
        authors = []
        for book_author in book_authors:
            author = {
                "name": book_author.author.full_name(),
                "role": book_author.role_str(),
                "uuid": book_author.author.uuid,
            }
            authors.append(author)

        return authors


class DetailedBookSerializer(ModelSerializer):
    publisher = DetailedPublisherField(read_only=True)
    genres = DetailedGenreField(read_only=True)
    authors = DetailedAuthorField(read_only=True)

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
