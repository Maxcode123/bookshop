from uuid import uuid4

from unittest_extensions import args

from tests.base import BookshopTestCase
from tests.factories import BookFactory, BookWithGenreFactory, BookWithAuthorFactory

uuids = {i: uuid4() for i in range(5)}


class TestListBooksView(BookshopTestCase):
    def subject(self, query_params):
        return self.get("/books/", query_params)

    def assert_response_count(self, count: int):
        self.assert_response_ok()
        self.assertEqual(self.cachedResult().data["count"], count)


class TestNoParamsListBooksView(TestListBooksView):
    @args({})
    def test_with_no_params(self):
        self.assert_response_count(0)

    @args({})
    def test_with_no_params_1_book(self):
        BookFactory.create()
        self.assert_response_count(1)

    @args({})
    def test_with_no_params_5_book(self):
        [BookFactory.create() for _ in range(5)]
        self.assert_response_count(5)


class TestGenreParamListBooksView(TestListBooksView):
    def setUp(self):
        BookWithGenreFactory.create(
            genre__genre__uuid=uuids[1], genre__genre__path="root.history"
        )
        book = BookWithGenreFactory.create(
            genre__genre__uuid=uuids[2], genre__genre__path="root.literature"
        )
        BookWithGenreFactory.create_with_genres(book.genres.all())
        BookWithGenreFactory.create(
            genre__genre__uuid=uuids[3],
            genre__genre__path="root.literature.greek_literature",
        )
        super().setUp()

    @args({"genre": uuids[1]})
    def test_with_genre_param(self):
        self.assert_response_count(1)

    @args({"genre": uuids[4]})
    def test_with_unknown_genre_param(self):
        self.assert_not_found()

    @args({"genre": "1234"})
    def test_with_invalid_genre_uuid_param(self):
        self.assert_unprocessable_content()

    @args({"genre": uuids[2]})
    def test_with_genre_parent(self):
        self.assert_response_count(3)

    @args({"genre": uuids[3]})
    def test_with_sole_genre_child(self):
        self.assert_response_count(1)


class TestAuthorParamListBooksView(TestListBooksView):
    def setUp(self):
        book1 = BookWithAuthorFactory.create(author__author__uuid=uuids[1])
        BookWithAuthorFactory.create_with_authors(book1.authors.all())
        BookWithAuthorFactory.create(author__author__uuid=uuids[2])
        super().setUp()

    @args({"author": uuids[1]})
    def test_with_author_of_two_books(self):
        self.assert_response_count(2)

    @args({"author": uuids[2]})
    def test_with_author_of_one_book(self):
        self.assert_response_count(1)

    @args({"author": uuids[3]})
    def test_with_nonexistent_author_uuid(self):
        self.assert_not_found()

    @args({"author": "not-a-valid-uuid"})
    def test_with_invalid_uuid(self):
        self.assert_unprocessable_content()


class TestPublisherParamListBooksView(TestListBooksView):
    def setUp(self):
        book = BookFactory.create(publisher__uuid=uuids[1])
        BookFactory.create(publisher=book.publisher)
        BookFactory.create(publisher__uuid=uuids[2])
        super().setUp()

    @args({"publisher": uuids[1]})
    def test_with_publisher_of_two_books(self):
        self.assert_response_count(2)

    @args({"publisher": uuids[2]})
    def test_with_publisher_of_one_books(self):
        self.assert_response_count(1)

    @args({"publisher": uuids[3]})
    def test_with_nonexistent_publisher_uuid(self):
        self.assert_not_found()

    @args({"publisher": "1231adsa"})
    def test_with_invalid_uuid(self):
        self.assert_unprocessable_content()
