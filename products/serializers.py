from rest_framework import serializers
from .models import Product, Category, Manufacturer
from cart.models import Cart, CartItem
from orders.models import Order, OrderItem
from django.contrib.auth.models import User

# ========== КАТЕГОРИЯ ==========
class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категории товаров"""
    products_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'products_count']
    
    def get_products_count(self, obj):
        return obj.products.count()

# ========== ПРОИЗВОДИТЕЛЬ ==========
class ManufacturerSerializer(serializers.ModelSerializer):
    """Сериализатор для производителя"""
    products_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'country', 'description', 'products_count']
    
    def get_products_count(self, obj):
        return obj.products.count()

# ========== ТОВАР ==========
class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для товара"""
    category_name = serializers.ReadOnlyField(source='category.name')
    manufacturer_name = serializers.ReadOnlyField(source='manufacturer.name')
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'photo', 'price', 
                  'stock_quantity', 'category', 'category_name',
                  'manufacturer', 'manufacturer_name']
    
    def validate_price(self, value):
        """Валидация цены"""
        if value < 0:
            raise serializers.ValidationError("Цена не может быть отрицательной")
        return value
    
    def validate_stock_quantity(self, value):
        """Валидация количества на складе"""
        if value < 0:
            raise serializers.ValidationError("Количество не может быть отрицательным")
        return value

# ========== ЭЛЕМЕНТ КОРЗИНЫ ==========
class CartItemSerializer(serializers.ModelSerializer):
    """Сериализатор для элемента корзины"""
    product_name = serializers.ReadOnlyField(source='product.name')
    product_price = serializers.ReadOnlyField(source='product.price')
    total = serializers.SerializerMethodField()
    
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_name', 'product_price', 'quantity', 'total']
    
    def get_total(self, obj):
        return obj.get_item_price()
    
    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Количество должно быть не менее 1")
        return value

# ========== КОРЗИНА ==========
class CartSerializer(serializers.ModelSerializer):
    """Сериализатор для корзины"""
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    items_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'items', 'total_price', 'items_count']
    
    def get_total_price(self, obj):
        return obj.get_total_price()
    
    def get_items_count(self, obj):
        return obj.items.count()

# ========== ЭЛЕМЕНТ ЗАКАЗА ==========
class OrderItemSerializer(serializers.ModelSerializer):
    """Сериализатор для элемента заказа"""
    product_name = serializers.ReadOnlyField(source='product.name')
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price', 'get_total']

# ========== ЗАКАЗ ==========
class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор для заказа"""
    items = OrderItemSerializer(many=True, read_only=True)
    user_name = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'user_name', 'created_at', 'address', 
                  'phone', 'email', 'total_price', 'items']

# ========== ПОЛЬЗОВАТЕЛЬ ==========
class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователя"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']