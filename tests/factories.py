from factory.django import DjangoModelFactory
from factory import SubFactory, RelatedFactory, LazyFunction
from faker import Faker
from faker_books import BookProvider

from books.models import Genre, Author, Publisher, Book, BookGenre, BookAuthor

fake = Faker()
fake.add_provider(BookProvider)


class GenreFactory(DjangoModelFactory):
    class Meta:
        model = Genre

    uuid = LazyFunction(fake.uuid4)
    name = LazyFunction(fake.book_genre)
    path = LazyFunction(fake.word)


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    uuid = LazyFunction(fake.uuid4)
    first_names = LazyFunction(fake.first_name)
    last_name = LazyFunction(fake.last_name)
    date_of_birth = LazyFunction(fake.date)
    date_of_death = LazyFunction(fake.date)
    summary = LazyFunction(fake.paragraph)


class PublisherFactory(DjangoModelFactory):
    class Meta:
        model = Publisher

    uuid = LazyFunction(fake.uuid4)
    name = LazyFunction(fake.book_publisher)


class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    uuid = LazyFunction(fake.uuid4)
    title = LazyFunction(fake.book_title)
    pages = LazyFunction(lambda: fake.pyint(10, 1000))
    cover = LazyFunction(lambda: fake.pyint(1, 2))
    paper = LazyFunction(lambda: fake.pyint(1, 2))
    language = LazyFunction(lambda: fake.word(ext_word_list=["GR", "EN"]))
    publication_date = LazyFunction(fake.date)
    weight_in_gr = LazyFunction(lambda: fake.pyint(50, 1500))
    edition = LazyFunction(lambda: fake.pyint(1, 25))
    series = LazyFunction(fake.word)
    volume = LazyFunction(lambda: fake.pyint(1, 50))
    isbn = LazyFunction(lambda: fake.isbn13().replace("-", ""))
    publisher = SubFactory(PublisherFactory)


class BookGenreFactory(DjangoModelFactory):
    class Meta:
        model = BookGenre

    book = SubFactory(BookFactory)
    genre = SubFactory(GenreFactory)


class BookAuthorFactory(DjangoModelFactory):
    class Meta:
        model = BookAuthor

    book = SubFactory(BookFactory)
    author = SubFactory(AuthorFactory)
    role = LazyFunction(lambda: fake.pyint(1, 6))


class BookWithGenreFactory(BookFactory):
    genre = RelatedFactory(BookGenreFactory, factory_related_name="book")

    @classmethod
    def create_with_genres(cls, genres):
        book = cls.create()
        [BookGenreFactory.create(book=book, genre=g) for g in genres]
        return book


class BookWithAuthorFactory(BookFactory):
    author = RelatedFactory(BookAuthorFactory, factory_related_name="book")

    @classmethod
    def create_with_authors(cls, authors):
        book = cls.create()
        [BookAuthorFactory.create(book=book, author=a) for a in authors]
        return book
