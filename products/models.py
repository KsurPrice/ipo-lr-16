# products/models.py
from django.db import models
from django.core.exceptions import ValidationError

def validate_non_negative(value):
    """Проверяет, что значение не отрицательное"""
    if value < 0:
        raise ValidationError('Value cannot be negative')

class Category(models.Model):
    """Модель 'Категория товара'"""
    name = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Manufacturer(models.Model):
    """Модель 'Производитель'"""
    name = models.CharField(max_length=100, verbose_name='Название')
    country = models.CharField(max_length=100, verbose_name='Страна')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'

class Product(models.Model):
    """Модель 'Товар'"""
    name = models.CharField(max_length=200, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Фото')
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[validate_non_negative],
        verbose_name='Price'
    )
    stock_quantity = models.IntegerField(
        validators=[validate_non_negative],
        verbose_name='Stock quantity'
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Category'
    )
    manufacturer = models.ForeignKey(
        Manufacturer, 
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Manufacturer'
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'