# apis/tests.py
from django.urls import reverse
from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book

class BookApiTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book=Book.objects.create(
            title="API Test Book",
            subtitle="API Subtitle",
            author="API Author",
            isbn="9876543210123"
        )

    def test_api_book_list(self):
        response=self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)
        self.assertEqual(response.data[0]['title'],"API Test Book")
        self.assertEqual(response.data[0]['subtitle'],"API Subtitle")
        self.assertEqual(response.data[0]['author'],"API Author")
        self.assertEqual(response.data[0]['isbn'],"9876543210123")