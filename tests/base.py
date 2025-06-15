from http import HTTPStatus

from unittest_extensions import TestCase
from django.test import TestCase as DjangoTestCase
from rest_framework.test import APIClient


class BookshopTestCase(TestCase, DjangoTestCase):
    def setUp(self):
        self.client = APIClient()

    def get(self, url, query_params={}, headers={}):
        return self.client.get(url, query_params=query_params, headers=headers)

    def assert_response_ok(self):
        self.assertEqual(self.result().status_code, 200)

    def assert_not_found(self):
        self.assertEqual(self.result().status_code, HTTPStatus.NOT_FOUND)

    def assert_unprocessable_content(self):
        self.assertEqual(self.result().status_code, HTTPStatus.UNPROCESSABLE_CONTENT)
