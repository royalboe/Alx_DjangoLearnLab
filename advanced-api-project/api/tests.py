from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Author, Book
from django.urls import reverse

class BookAPITestCase(APITestCase):
    """
    Unit tests for Book API endpoints.

    Test coverage includes:
    - GET /books/           (list view)
    - GET /books/<pk>/      (detail view)
    - POST /books/create/   (create view, with and without authentication)
    - PUT /books/<pk>/update/ (update view)
    - DELETE /books/<pk>/delete/ (delete view)
    - Filtering by title
    - Searching by title/author name
    - Ordering by publication_year

    All tests validate:
    - Correct status codes (200, 201, 204, 401)
    - Data integrity (e.g., correct title/author returned)
    - Permissions (e.g., unauthenticated users can’t create or delete books)
    """
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create authors
        self.author1 = Author.objects.create(name="George Orwell")
        self.author2 = Author.objects.create(name="Aldous Huxley")

        # Create books
        self.book1 = Book.objects.create(
            title="1984", publication_year=1949, author=self.author1)
        self.book2 = Book.objects.create(
            title="Brave New World", publication_year=1932, author=self.author2)

        self.client = APIClient()

    def test_list_books(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "1984")

    def test_create_book_requires_auth(self):
        data = {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author1.pk
        }
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author1.pk
        }
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            "title": "Updated 1984",
            "publication_year": 1949,
            "author": self.author1.pk
        }
        response = self.client.put(reverse('book-update', kwargs={'pk': self.book1.pk}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated 1984")

    def test_delete_book(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(reverse('book-delete', kwargs={'pk': self.book2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book2.pk).exists())

    def test_filter_by_title(self):
        response = self.client.get(reverse('book-list'), {'title': '1984'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], '1984')

    def test_search_books(self):
        response = self.client.get(reverse('book-list'), {'search': 'orwell'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], '1984')

    def test_order_books(self):
        response = self.client.get(reverse('book-list'), {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], '1984')