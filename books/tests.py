from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book=Book.objects.create(
            title="Test Book",
            subtitle="A Subtitle",
            author="Author Name",
            isbn="1234567890123"
        )
    def test_book_content(self):
        self.assertEqual(self.book.title,"Test Book")
        self.assertEqual(self.book.subtitle,"A Subtitle")
        self.assertEqual(self.book.author,"Author Name")
        self.assertEqual(self.book.isbn,"1234567890123")

    def test_book_list_view(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Test Book")
        self.assertTemplateUsed(response,'books/book_list.html')

# Create your tests here.
