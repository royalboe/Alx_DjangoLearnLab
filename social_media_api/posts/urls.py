# Define URL patterns in posts/urls.py that map to the viewsets using Django REST Framework’s routers. This includes routes for listing, creating, editing, and deleting both posts and comments.

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, FeedViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('comments', CommentViewSet, basename='comment')
router.register("feed", FeedViewSet, basename='feed')

urlpatterns = [
    path('', include(router.urls)),
]