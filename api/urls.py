from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import UserViewSet, ProductViewSet, CategoryViewSet
from .views import register_user, login_user
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/register/', register_user, name='register'),
    path('auth/login/', login_user, name='login'),
] + router.urls