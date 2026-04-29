from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from orders.views import OrderViewSet

# Создаем роутер
router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='api-category')
router.register(r'manufacturers', views.ManufacturerViewSet, basename='api-manufacturer')
router.register(r'products', views.ProductViewSet, basename='api-product')
router.register(r'cart', views.CartViewSet, basename='api-cart')
router.register(r'cart-items', views.CartItemViewSet, basename='api-cart-item')

# URL-маршруты для API
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]