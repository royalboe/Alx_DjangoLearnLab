from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, SignUpView, CustomLoginView, CustomLogoutView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('register/', views.register, name='signup'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', views.librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', views.member_dashboard, name='member_dashboard'),
    path('books/add_book/', views.add_book, name='add_book'),
    path('books/<int:book_id>/edit_book/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]
