from django.urls import path

from .views import SignUpView, register, CustomLoginView, CustomLogoutView
import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('register/', register, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('register/', views.register, name='signup'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path("post/new/", views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name='post-update'),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name='post-delete'),
     # comments (nested under posts)
    path("posts/<int:post_pk>/comments/new/", views.CommentCreateView.as_view(), name='comment-create'),
    path("posts/<int:post_pk>/comments/<int:pk>/edit/", views.CommentUpdateView.as_view(), name='comment-update'),
    path("posts/<int:post_pk>/comments/<int:pk>/delete/", views.CommentDeleteView.as_view(), name='comment-delete'),
]

[, "post/<int:pk>/update/", "post/new/", "post/<int:pk>/delete/", "posts/<int:pk>/", "posts/"]