from django.db.models import (
    ForeignKey,
    TextField,
    CharField,
    IntegerField,
    DateField,
    IntegerChoices,
    SmallIntegerField,
    TextChoices,
    CASCADE,
)

from utils.base_model import register_admin, BaseModel, UUIDMixin


@register_admin
class Genre(BaseModel, UUIDMixin):
    class Meta:
        db_table = "genres"

    parent_id = IntegerField(null=True, blank=True)
    root_id = IntegerField()
    name = CharField(max_length=100)


@register_admin
class Publisher(BaseModel, UUIDMixin):
    class Meta:
        db_table = "publishers"

    name = CharField(max_length=200)


@register_admin
class Author(BaseModel, UUIDMixin):
    class Meta:
        db_table = "authors"

    first_names = CharField(max_length=200)
    last_name = CharField(max_length=200)
    date_of_birth = DateField()
    date_of_death = DateField(null=True, blank=True)
    summary = TextField()


@register_admin
class Book(BaseModel, UUIDMixin):
    class Meta:
        db_table = "books"

    class Cover(IntegerChoices):
        PAPERBACK = 1
        HARDBACK = 2

    class Paper(IntegerChoices):
        CHAMOIS = 1
        PALATINA = 2

    class Language(TextChoices):
        GREEK = "GR"
        ENGLISH = "EN"

    title = CharField(max_length=200)
    pages = IntegerField()
    introductory_pages = CharField(max_length=50, null=True, blank=True)
    width_in_cm = IntegerField(null=True, blank=True)
    length_in_cm = IntegerField(null=True, blank=True)
    cover = IntegerField(null=True, choices=Cover, blank=True)
    weight_in_gr = IntegerField(null=True, blank=True)
    paper = IntegerField(null=True, choices=Paper, blank=True)
    isbn = CharField(max_length=13, null=True, blank=True)
    edition = SmallIntegerField(null=True, blank=True)
    series = CharField(max_length=200, null=True, blank=True)
    volume = SmallIntegerField(null=True, blank=True)
    publication_date = DateField()
    language = CharField(max_length=2, choices=Language)
    publisher = ForeignKey(Publisher, on_delete=CASCADE)


@register_admin
class BookAuthor(BaseModel):
    class Meta:
        db_table = "book_authors"

    class Role(IntegerChoices):
        AUTHOR = 1
        TRANSLATOR = 2
        EDITOR = 3
        SERIES_EDITOR = 4
        INTRODUCTION = 5
        ANTHOLOGIST = 6

    author = ForeignKey(Author, on_delete=CASCADE)
    book = ForeignKey(Book, on_delete=CASCADE)
    role = IntegerField(choices=Role)


@register_admin
class BookGenre(BaseModel):
    class Meta:
        db_table = "book_genres"

    book = ForeignKey(Book, on_delete=CASCADE)
    genre = ForeignKey(Genre, on_delete=CASCADE)
