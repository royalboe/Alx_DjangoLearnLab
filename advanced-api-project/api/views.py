from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

# ListView: Handles GET /books/ to list all books
class BookListView(generics.ListAPIView):
    """
    API endpoint to list all books with support for filtering, searching, and ordering.

    - Filtering fields: title, author, publication_year
    - Search fields: title, author's name
    - Ordering fields: title, publication_year
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Enable filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # Fields that can be used for filtering
    filterset_fields = ['title', 'author', 'publication_year']

    # Fields that can be used for search
    search_fields = ['title', 'author__name']

    # Fields that can be used for ordering
    ordering_fields = ['title', 'publication_year']

    # Default ordering (optional)
    ordering = ['title']

# DetailView: Handles GET /books/<pk>/ to retrieve a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public access

# CreateView: Handles POST /books/ to create a book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users only


# UpdateView: Handles PUT/PATCH /books/<pk>/ to update a book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users only

# DeleteView: Handles DELETE /books/<pk>/ to delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Authenticated users only