from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token

from posts.models import Post
from posts.serializers import PostSerializer


# Create your views here.
from .serializers import RegisterSerializer, LoginSerializer, UserProfileSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes

User = get_user_model()
CustomUser = get_user_model()


class RegisterViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)
            return Response({"message": "User registered successfully", "token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                {
                    "message": "Login successful",
                    "token": serializer.validated_data['token']
                },
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return the current user's profile
        return User.objects.filter(id=self.request.user.id)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(detail=False, methods=['put', 'patch'])
    def update_profile(self, request):
        serializer = self.get_serializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Profile updated successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def get_user_by_id(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    allowed_methods = ['POST']

    def post(self, request, user_id):
        if request.user.id == user_id:
            return Response({"message": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        user_to_follow = get_user_by_id(user_id)
        if not user_to_follow:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        if user_to_follow in request.user.following.all():
            return Response({"message": "You are already following this user"}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    allowed_methods = ['POST']
    def post(self, request, user_id):
        if request.user.id == user_id:
            return Response({"message": "You cannot unfollow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        user_to_unfollow = get_user_by_id(user_id)
        if not user_to_unfollow:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        if user_to_unfollow not in request.user.following.all():
            return Response({"message": "You are not following this user"}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
