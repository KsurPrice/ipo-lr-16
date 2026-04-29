from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'total_price', 'phone', 'email')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'phone', 'email')
    readonly_fields = ('created_at', 'total_price')
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price', 'get_total')
    list_filter = ('order',)
    search_fields = ('product__name',)

    def get_total(self, obj):
        return obj.get_total()
    get_total.short_description = 'Сумма'