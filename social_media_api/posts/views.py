# Step 3: Create Views for CRUD Operations
# View Implementation:
# Using Django REST Framework’s viewsets, set up CRUD operations for both posts and comments in posts/views.py.
# Implement permissions to ensure users can only edit or delete their own posts and comments.


from rest_framework import filters
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .filters import PostFilter, CommentFilter

from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import status
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    filterset_class = PostFilter
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        elif self.action in ['create']:
            return [permissions.IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
        return super().get_permissions()
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def feed(self, request):
    #     user = request.user
    #     following_users = user.following.all()
    #     posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    #     serializer = PostSerializer(posts, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get_queryset(self):
        user = self.request.user
        qs = Post.objects.all()
        if user.is_authenticated:
            if user.is_superuser:
                return qs
            following_users = self.request.user.following.all()
            return qs.filter(author__in=list(following_users) + [self.request.user])
        else:
            qs = qs.none()
        return qs.order_by('-created_at')
