# products/admin.py
from django.contrib import admin
from .models import Category, Manufacturer, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'description')
    search_fields = ('name', 'country')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock_quantity', 'category', 'manufacturer')
    list_filter = ('category', 'manufacturer')
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock_quantity')