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

from bookshop.utils.base_model import register_admin, BaseModel, UUIDMixin


@register_admin
class Genre(BaseModel, UUIDMixin):
    parent_id = IntegerField(null=True)
    root_id = IntegerField()
    name = CharField(max_length=100)


@register_admin
class Publisher(BaseModel, UUIDMixin):
    name = CharField(max_field=200)


@register_admin
class Author(BaseModel, UUIDMixin):
    first_names = CharField(max_length=200)
    last_name = CharField(max_length=200)
    date_of_birth = DateField()
    date_of_death = DateField(null=True)
    summary = TextField()


@register_admin
class Book(BaseModel, UUIDMixin):
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
    introductory_pages = CharField(max_length=50, null=True)
    width_in_cm = IntegerField(null=True)
    length_in_cm = IntegerField(null=True)
    cover = IntegerField(null=True, choices=Cover)
    weight_in_gr = IntegerField(null=True)
    paper = IntegerField(null=True, choices=Paper)
    isbn = CharField(max_length=13, null=True)
    edition = SmallIntegerField(null=True)
    series = CharField(max_length=200, null=True)
    volume = SmallIntegerField(null=True)
    publication_date = DateField()
    language = CharField(max_length=2, choices=Language)
    publisher = ForeignKey(Publisher, on_delete=CASCADE)


@register_admin
class BookAuthor(BaseModel):
    class Role(IntegerChoices):
        AUTHOR = 1
        TRANSLATOR = 2
        EDITOR = 3
        SERIES_EDITOR = 4
        INTRODUCTION = 5
        ANTHOLOGIST = 6

    author = ForeignKey(Author)
    book = ForeignKey(Book)
    role = IntegerField(choices=Role)


@register_admin
class BookGenre(BaseModel):
    book = ForeignKey(Book)
    genre = ForeignKey(Genre)
