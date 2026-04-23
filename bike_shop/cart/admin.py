# cart/admin.py
from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1
    raw_id_fields = ('product',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'total_price_display')
    search_fields = ('user__username',)
    inlines = [CartItemInline]
    
    def total_price_display(self, obj):
        return f"{obj.get_total_price():.2f} rub."
    total_price_display.short_description = 'Total price'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity', 'item_price_display')
    search_fields = ('product__name',)
    
    def item_price_display(self, obj):
        return f"{obj.get_item_price():.2f} rub."
    item_price_display.short_description = 'Item price'