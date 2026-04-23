# cart/models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from products.models import Product

class Cart(models.Model):
    """Модель 'Корзина'"""
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='User'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    
    def __str__(self):
        return f"Cart of {self.user.username}"
    
    def get_total_price(self):
        """Вычисляет общую стоимость корзины"""
        return sum(item.get_item_price() for item in self.items.all())
    
    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

class CartItem(models.Model):
    """Модель 'Элемент корзины'"""
    cart = models.ForeignKey(
        Cart, 
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Cart'
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
        verbose_name='Product'
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name='Quantity')
    
    def __str__(self):
        return f"{self.product.name} ({self.quantity} pcs)"
    
    def get_item_price(self):
        """Возвращает стоимость позиции: цена товара * количество"""
        return self.product.price * self.quantity
    
    def clean(self):
        """Валидация: количество не должно превышать остаток на складе"""
        if self.quantity > self.product.stock_quantity:
            raise ValidationError(f'Not enough stock. Available: {self.product.stock_quantity}')
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Cart item'
        verbose_name_plural = 'Cart items'