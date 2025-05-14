from uuid import uuid4
from datetime import date
from typing import Type, Any

from books.models import Book, Author, BookAuthor, BookGenre, Genre, Publisher


def run():
    create_genres()
    create_publishers()
    create_authors()
    create_books()
    create_book_genres()
    create_book_authors()


def create_genres() -> None:
    create_if_not_exists(1, Genre, dict(uuid=uuid4(), root_id=1, name="Λογοτεχνία"))
    create_if_not_exists(
        2, Genre, dict(uuid=uuid4(), parent_id=1, root_id=1, name="Ποίηση")
    )
    create_if_not_exists(
        3, Genre, dict(uuid=uuid4(), parent_id=2, root_id=1, name="Ελληνική Ποίηση")
    )
    create_if_not_exists(
        4, Genre, dict(uuid=uuid4(), parent_id=3, root_id=1, name="Νεοελληνική Ποίηση")
    )
    create_if_not_exists(5, Genre, dict(uuid=uuid4(), root_id=5, name="Λαογραφία"))
    create_if_not_exists(
        6, Genre, dict(uuid=uuid4(), parent_id=5, root_id=5, name="Δημοτικά Τραγούδια")
    )
    create_if_not_exists(7, Genre, dict(uuid=uuid4(), root_id=7, name="Ιστορία"))
    create_if_not_exists(8, Genre, dict(uuid=uuid4(), root_id=8, name="Κρήτη"))


def create_publishers() -> None:
    create_if_not_exists(1, Publisher, dict(uuid=uuid4(), name="Νέα Ελληνικά"))
    create_if_not_exists(
        2, Publisher, dict(uuid=uuid4(), name="Καραβίας Δ. Ν. Αναστατικές Εκδόσεις")
    )


def create_authors() -> None:
    create_if_not_exists(
        1,
        Author,
        dict(
            uuid=uuid4(),
            first_names="Ρένος",
            last_name="Αποστολίδης",
            date_of_birth=date(1924, 3, 2),
            date_of_death=date(2004, 3, 10),
        ),
    )
    create_if_not_exists(
        2,
        Author,
        dict(
            uuid=uuid4(),
            first_names="Στάντης",
            last_name="Αποστολίδης",
            date_of_birth=date(1961, 1, 1),
        ),
    )
    create_if_not_exists(
        3,
        Author,
        dict(
            uuid=uuid4(),
            first_names="Ήρκος",
            last_name="Αποστολίδης",
            date_of_birth=date(1957, 1, 1),
        ),
    )
    create_if_not_exists(
        4, Author, dict(uuid=uuid4(), first_names="Παύλος", last_name="Φαφουτάκης")
    )
    create_if_not_exists(
        5,
        Author,
        dict(
            uuid=uuid4(),
            first_names="Εμμανουήλ",
            last_name="Βερνάρδος",
            date_of_birth=date(1777, 1, 1),
            date_of_death=date(1852, 1, 1),
        ),
    )


def create_books() -> None:
    create_if_not_exists(
        1,
        Book,
        dict(
            uuid=uuid4(),
            title="Ανθολογία της Νεοελληνικής Γραμματείας - Ποίηση",
            pages=568,
            introductory_pages="λ'",
            width_in_cm=17,
            length_in_cm=24,
            edition=12,
            series="Ανθολογία της Νεοελληνικής Γραμματείας",
            volume=1,
            publication_date=date(2009, 12, 1),
            language="GR",
            publisher_id=1,
        ),
    )
    create_if_not_exists(
        2,
        Book,
        dict(
            uuid=uuid4(),
            title="Ανθολογία της Νεοελληνικής Γραμματείας - Ποίηση",
            pages=538,
            width_in_cm=17,
            length_in_cm=24,
            edition=12,
            series="Ανθολογία της Νεοελληνικής Γραμματείας",
            volume=2,
            publication_date=date(2009, 12, 1),
            language="GR",
            publisher_id=1,
        ),
    )
    create_if_not_exists(
        3,
        Book,
        dict(
            uuid=uuid4(),
            title="Ανθολογία της Νεοελληνικής Γραμματείας - Ποίηση",
            pages=605,
            width_in_cm=17,
            length_in_cm=24,
            edition=12,
            series="Ανθολογία της Νεοελληνικής Γραμματείας",
            volume=3,
            publication_date=date(2009, 12, 1),
            language="GR",
            publisher_id=1,
        ),
    )
    create_if_not_exists(
        4,
        Book,
        dict(
            uuid=uuid4(),
            title="Συλλογή Ηρωικών Κρητικών Ασμάτων",
            pages=128,
            introductory_pages="ιε'",
            publication_date=date(1889, 1, 1),
            isbn="9602580372",
            language="GR",
            publisher_id=2,
        ),
    )
    create_if_not_exists(
        5,
        Book,
        dict(
            uuid=uuid4(),
            title="Ιστορία της Κρήτης",
            pages=168,
            publication_date=date(1846, 1, 1),
            isbn="9602580771",
            language="GR",
            publisher_id=2,
        ),
    )


def create_book_genres() -> None:
    create_if_not_exists(1, BookGenre, dict(book_id=1, genre_id=4))
    create_if_not_exists(2, BookGenre, dict(book_id=2, genre_id=4))
    create_if_not_exists(3, BookGenre, dict(book_id=3, genre_id=4))
    create_if_not_exists(4, BookGenre, dict(book_id=4, genre_id=6))
    create_if_not_exists(5, BookGenre, dict(book_id=4, genre_id=8))
    create_if_not_exists(6, BookGenre, dict(book_id=5, genre_id=7))
    create_if_not_exists(7, BookGenre, dict(book_id=5, genre_id=8))


def create_book_authors() -> None:
    create_if_not_exists(1, BookAuthor, dict(role=6, author_id=1, book_id=1))
    create_if_not_exists(2, BookAuthor, dict(role=6, author_id=2, book_id=1))
    create_if_not_exists(3, BookAuthor, dict(role=6, author_id=3, book_id=1))
    create_if_not_exists(4, BookAuthor, dict(role=6, author_id=1, book_id=2))
    create_if_not_exists(5, BookAuthor, dict(role=6, author_id=2, book_id=2))
    create_if_not_exists(6, BookAuthor, dict(role=6, author_id=3, book_id=2))
    create_if_not_exists(7, BookAuthor, dict(role=6, author_id=1, book_id=3))
    create_if_not_exists(8, BookAuthor, dict(role=6, author_id=2, book_id=3))
    create_if_not_exists(9, BookAuthor, dict(role=6, author_id=3, book_id=3))
    create_if_not_exists(10, BookAuthor, dict(role=3, author_id=4, book_id=4))
    create_if_not_exists(11, BookAuthor, dict(role=2, author_id=5, book_id=5))


def create_if_not_exists(id: int, model_cls: Type, values: dict[str, Any]) -> None:
    if model_cls.find(id) is None:
        model_cls(id=id, **values).save()
