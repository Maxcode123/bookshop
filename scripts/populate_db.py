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


def create_if_not_exists(id: int, model_cls: Type, values: dict[str, Any]) -> None:
    if model_cls.find(id) is None:
        model_cls(id=id, **values).save()


def create_genres() -> None:
    create_if_not_exists(1, Genre, dict(name="root", path="root"))
    create_if_not_exists(2, Genre, dict(name="Λογοτεχνία", path="root.literature"))
    create_if_not_exists(3, Genre, dict(name="Ποίηση", path="root.literature.poetry"))
    create_if_not_exists(
        4,
        Genre,
        dict(name="Ελληνική Ποίηση", path="root.literature.poetry.greek_poetry"),
    )
    create_if_not_exists(
        5,
        Genre,
        dict(
            name="Νεοελληνική Ποίηση",
            path="root.literature.poetry.greek_poetry.contemporary_greek_poetry",
        ),
    )
    create_if_not_exists(6, Genre, dict(name="Λαογραφία", path="root.folklore"))
    create_if_not_exists(
        7, Genre, dict(name="Δημοτικά Τραγούδια", path="root.folklore.folk_songs")
    )
    create_if_not_exists(8, Genre, dict(name="Ιστορία", path="root.history"))
    create_if_not_exists(9, Genre, dict(name="Κρήτη", path="root.crete"))
    create_if_not_exists(
        10, Genre, dict(name="Κλασσική Γραμματεία", path="root.classics")
    )
    create_if_not_exists(
        11, Genre, dict(name="Διηγηματογραφία", path="root.literature.short_stories")
    )


def create_publishers() -> None:
    create_if_not_exists(1, Publisher, dict(uuid=uuid4(), name="Νέα Ελληνικά"))
    create_if_not_exists(
        2, Publisher, dict(uuid=uuid4(), name="Καραβίας Δ. Ν. Αναστατικές Εκδόσεις")
    )
    create_if_not_exists(3, Publisher, dict(uuid=uuid4(), name="Στιγμή"))


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
    create_if_not_exists(
        6,
        Author,
        dict(
            uuid=uuid4(),
            first_names="Γεώργιος",
            last_name="Βιζυηνός",
            date_of_birth=date(1849, 3, 8),
            date_of_death=date(1896, 4, 15),
        ),
    )
    create_if_not_exists(
        7,
        Author,
        dict(
            uuid=uuid4(),
            first_names="Κωνσταντίνος",
            last_name="Καβάφης",
            date_of_birth=date(1863, 4, 29),
            date_of_death=date(1933, 4, 29),
        ),
    )
    create_if_not_exists(
        8,
        Author,
        dict(
            uuid=uuid4(),
            first_names="Στυλιανός",
            last_name="Αλεξίου",
            date_of_birth=date(1921, 2, 13),
            date_of_death=date(2013, 11, 12),
        ),
    )
    create_if_not_exists(
        9,
        Author,
        dict(
            uuid=uuid4(),
            first_names="Γρηγόριος",
            last_name="Παπαδοπετράκης",
            date_of_birth=date(1828, 1, 1),
            date_of_death=date(1889, 1, 1),
        ),
    )
    create_if_not_exists(
        10,
        Author,
        dict(
            uuid=uuid4(),
            first_names="Διονύσιος",
            last_name="Σολωμός",
            date_of_birth=date(1798, 4, 8),
            date_of_death=date(1857, 2, 9),
        ),
    )
    create_if_not_exists(
        11,
        Author,
        dict(
            uuid=uuid4(),
            first_names="Αριστείδης",
            last_name="Κριάρης",
            date_of_birth=date(1858, 1, 1),
            date_of_death=date(1924, 1, 1),
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
    create_if_not_exists(
        6,
        Book,
        dict(
            uuid=uuid4(),
            title="Άπαντα τα δημοσιευμένα ποίηματα",
            introductory_pages="XXX",
            pages=431,
            publication_date=date(2023, 1, 1),
            edition=6,
            language="GR",
            publisher_id=1,
        ),
    )
    create_if_not_exists(
        7,
        Book,
        dict(
            uuid=uuid4(),
            title="Άπαντα τα διηγήματα",
            introductory_pages="LXI",
            pages=461,
            publication_date=date(2013, 1, 1),
            language="GR",
            publisher_id=1,
        ),
    )
    create_if_not_exists(
        8,
        Book,
        dict(
            uuid=uuid4(),
            title="Ποίηματα και πεζά",
            pages=515,
            publication_date=date(2007, 2, 1),
            language="GR",
            publisher_id=3,
        ),
    )


def create_book_genres() -> None:
    create_if_not_exists(1, BookGenre, dict(book_id=1, genre_id=5))
    create_if_not_exists(2, BookGenre, dict(book_id=2, genre_id=5))
    create_if_not_exists(3, BookGenre, dict(book_id=3, genre_id=5))
    create_if_not_exists(4, BookGenre, dict(book_id=4, genre_id=7))
    create_if_not_exists(5, BookGenre, dict(book_id=4, genre_id=9))
    create_if_not_exists(6, BookGenre, dict(book_id=5, genre_id=8))
    create_if_not_exists(7, BookGenre, dict(book_id=5, genre_id=9))
    create_if_not_exists(8, BookGenre, dict(book_id=6, genre_id=5))
    create_if_not_exists(9, BookGenre, dict(book_id=7, genre_id=11))
    create_if_not_exists(10, BookGenre, dict(book_id=8, genre_id=5))


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
    create_if_not_exists(12, BookAuthor, dict(role=1, author_id=7, book_id=6))
    create_if_not_exists(13, BookAuthor, dict(role=3, author_id=1, book_id=6))
    create_if_not_exists(14, BookAuthor, dict(role=3, author_id=2, book_id=6))
    create_if_not_exists(15, BookAuthor, dict(role=3, author_id=3, book_id=6))
    create_if_not_exists(16, BookAuthor, dict(role=1, author_id=6, book_id=7))
    create_if_not_exists(17, BookAuthor, dict(role=3, author_id=2, book_id=7))
    create_if_not_exists(18, BookAuthor, dict(role=3, author_id=3, book_id=7))
    create_if_not_exists(19, BookAuthor, dict(role=1, author_id=10, book_id=8))
    create_if_not_exists(20, BookAuthor, dict(role=3, author_id=8, book_id=8))
