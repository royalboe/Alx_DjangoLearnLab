from django.urls import path
import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'register/', views.RegisterViewSet, basename='register')
router.register(r'login/', views.LoginViewSet, basename='login')
router.register(r'profile/', views.ProfileViewSet, basename='profile')

urlpatterns = router.urls