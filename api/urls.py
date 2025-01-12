from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import UserViewSet, ProductViewSet, CategoryViewSet, OrderViewSet, OrderItemViewSet, ReviewListCreateView
from .views import register_user, login_user, WishlistListCreateView, WishlistDeleteView
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/register/', register_user, name='register'),
    path('auth/login/', login_user, name='login'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('wishlist/', WishlistListCreateView.as_view(), name='wishlist-list-create'),
    path('wishlist/<int:id>/', WishlistDeleteView.as_view(), name='wishlist-delete'),
] + router.urls