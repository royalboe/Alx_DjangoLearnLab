from django_filters import rest_framework as filters
from .models import Post, Comment

class PostFilter(filters.FilterSet):
    author = filters.CharFilter(field_name='author__username', lookup_expr='iexact')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Post
        fields = ['author', 'title', 'created_at']

class CommentFilter(filters.FilterSet):
    author = filters.CharFilter(field_name='author__username', lookup_expr='iexact')
    post = filters.NumberFilter(field_name='post__id')
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Comment
        fields = ['author', 'post', 'created_at']