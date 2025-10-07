from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'/register', views.RegisterViewSet, basename='register')
router.register(r'/login', views.LoginViewSet, basename='login')
router.register(r'/profile', views.ProfileViewSet, basename='profile')

urlpatterns = {
    path('', include(router.urls)),
    path('follow/<int:user_id>/', views.FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', views.UnfollowUserView.as_view(), name='unfollow_user'),
}

urlpatterns = router.urls
