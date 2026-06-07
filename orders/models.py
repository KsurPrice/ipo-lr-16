from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    """Модель заказа"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    address = models.TextField(verbose_name='Адрес доставки')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email для чека')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Итого')
    
    def __str__(self):
        return f'Заказ #{self.id} от {self.user.username}'
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class OrderItem(models.Model):
    """Товары в заказе"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    
    def get_total(self):
        return self.price * self.quantity
    
    def __str__(self):
        return f'{self.product.name} x {self.quantity}'
    
    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'